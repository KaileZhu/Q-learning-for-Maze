from algorithm.QLearning import Q_learning
from env.GridStaticEnv import Env
import numpy as np


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
    action_space = [0, 1, 2, 3]
    state_dim = [height, width]
    GAMMA = 0.6
    ALPHA = 0.1
    EPISILON = 0.2
    EPISODE = 10000
    ############################

    env = Env(height, width, radius=radius)
    env.p = 0.9
    agent = Q_learning(action_space, state_dim)

    #############################

    state = env.reset()
    env.render()
    done = False
    print("Initialize the map...")
    print("==============================")
    rewards = [0]
    avg_reward = []
    for i in range(EPISODE):
        env.reset()
        rewards = []

        while not done:
            # action = 0
            action = agent.choose_action(state, episilon= EPISILON)
            state = env.get_state();
            # env.render()
            next_state, reward, done = env.step(action)
            agent.update_q_table(state, next_state, action, reward, gamma=GAMMA, alpha=ALPHA)
            # print("==============================")
            rewards.append(reward)
        avg_reward.append(np.round(sum(rewards)/env.count,2))
        done = False
        if (i % 50 == 0):
            print("i =", i, "reward = ", avg_reward[-1])

    agent.save_q_table(file_name = 'q_table')
    np.save('result/reward.npy', avg_reward)
    np.save('result/map.npy', env.map)

    print("==============================")
    print("length:", len(rewards))
    print("rewards:", rewards)
    print("avg_rewards:", avg_reward)


    # ## show results here
    # import matplotlib.pyplot as plt
    #
    # step_avg_reward = [0]
    # step = 50
    # for i in range(len(avg_reward)):
    #     if (i % step == 0):
    #         step_avg_reward.append(sum(avg_reward[i:i+step-1])/step)
    # x = list(range(0, len(step_avg_reward)))
    # plt.plot(x, step_avg_reward,'b-')
    # plt.show()


