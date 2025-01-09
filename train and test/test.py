from algorithm.QLearning import Q_learning
from env.GridStaticEnv import Env
import numpy as np

## TODOLIST: VIS V_TABLE: V = max(Q(s,a)

if __name__=="__main__":
    ############################
    # height = 5
    # width = 5
    # radius = 2
    ############################
    height = 10
    width = 10
    radius = 3
    ############################
    # height = 20
    # width = 20
    # radius = 3
    ############################
    action_space = [0, 1, 2, 3]
    state_dim = [height, width]
    GAMMA = 0.6
    ALPHA = 0.1
    EPISILON = 0.01
    EPISODE = 1000
    ############################

    env = Env(height, width, radius=radius)
    agent = Q_learning(action_space, state_dim)

    ############################
    # LOAD THE MAP AND LOAD THE Q_TABLE
    env.map = np.load('result/map.npy')
    agent.load_q_table('q_table')

    #############################


    env.render()

    done = False
    print("Initialize the map...")
    print("==============================")
    rewards = [0]
    avg_reward = []
    states = []


    for i in range(EPISODE):
        state = env.reset()
        rewards = []
        current_states = []

        while not done:
            # action = 0
            action = agent.choose_action(state, episilon= EPISILON)
            state = env.get_state()
            current_states.append((state[0], state[1]))
            # env.render()
            next_state, reward, done = env.step(action)
            # agent.update_q_table(state, next_state, action, reward, gamma=GAMMA, alpha=ALPHA)
            # print("==============================")
            rewards.append(reward)
        avg_reward.append(np.round(sum(rewards)/env.count,2))
        states.append(current_states)
        done = False
        if (i % 50 == 0):
            print("i =", i, "reward = ", avg_reward[-1])

    # agent.save_q_table(file_name = 'q_table')
    print("Saving the result...")
    print(states)
    np.save('result/reward_test.npy', avg_reward)
    np.save('result/route_test.npy', states)
    # np.save('result/map.npy', env.map)
    print("Done.")

    print("==============================")
    print("length:", len(rewards))
    print("rewards:", rewards)
    print("avg_rewards:", avg_reward)




