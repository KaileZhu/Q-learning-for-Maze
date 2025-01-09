from QLearning import Q_learning
from GridStaticEnv import Env
import numpy as np

if __name__ == "__main__":
    ############################
    height = 20
    width = 20
    radius = 5
    ############################
    action_space = [0, 1, 2, 3]
    # 分别代表上下左右
    state_dim = [height, width]   # 地图尺寸
    GAMMA = 0.6    # 奖励递减值
    ALPHA = 0.1    # 学习率，决定多少误差需要被学习
    EPSILON = 0.6    # 贪婪度，决定多少情况UAV会按Q表最优值选择行为，剩余为随机
    EPISODE = 20    # 最大回合数
    ############################
    env = Env(height, width, radius=radius)
    env.p = 0.9   # 1-p为人出现概率
    agent = Q_learning(action_space, state_dim)
    #############################

    state = env.reset()  # 也就是地图坐标
    env.render(0)
    done = False
    print("Initialize the map...")
    print("==============================")
    rewards = [0]
    avg_reward = []
    for i in range(EPISODE):
        env.reset()
        rewards = []
        epsilon = EPSILON + i * (1 - EPSILON) / EPISODE  # 随训练次数的增大，q表接近收敛，action准则需更多地依赖q表
        while not done:
            # action = 0
            action = agent.choose_action(state, epsilon)
            state = env.get_state();
            env.render(len(rewards))
            next_state, reward, done = env.step(action)
            agent.update_q_table(state, next_state, action, reward, gamma=GAMMA, alpha=ALPHA)
            # print("==============================")
            rewards.append(reward)
        avg_reward.append(np.round(sum(rewards)/env.count,2))
        done = False
        if (i % 50 == 0):
            print("i =", i, "reward = ", avg_reward[-1])

    # agent.save_q_table(file_name = 'q_table')
    # np.save('result/reward.npy', avg_reward)
    # np.save('result/map.npy', env.map)

    print("==============================")
    print("length:", len(rewards))
    print("rewards:", rewards)
    print("avg_rewards:", avg_reward)


    # show results here
    import matplotlib.pyplot as plt

    # step_avg_reward = [0]
    # step = 50
    # for i in range(len(avg_reward)):
    #     if (i % step == 0):
    #         step_avg_reward.append(sum(avg_reward[i:i+step-1])/step)
    # x = list(range(0, len(step_avg_reward)))
    # plt.plot(x, step_avg_reward,'b-')
    # plt.show()

    x = list(range(0,EPISODE))
    plt.plot(x, avg_reward)
    plt.show()















