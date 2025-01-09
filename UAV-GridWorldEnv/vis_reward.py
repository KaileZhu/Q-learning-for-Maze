import matplotlib.pyplot as plt
import numpy as np


def get_step_reward(avg_reward, step):
    step_reward = [0]
    for i in range(len(avg_reward)):
        if i % step == 0:
            step_reward.append(sum(avg_reward[i:i + step - 1]) / step)
    x = np.linspace(0, len(avg_reward), int(len(avg_reward) / step) + 1)
    return x, step_reward


def get_weighted_moving_reward(avg_reward, weight):
    # x = np.linspace(0, len(avg_reward) - 1, len(avg_reward))
    return np.convolve(avg_reward, np.ones(weight), 'same') / weight


if __name__=="__main__":
    avg_reward = np.load('result/reward.npy')
    # print(avg_reward)
    print(len(avg_reward))

    plt.figure()


    x, step_avg_reward = get_step_reward(avg_reward, step=10)
    plt.plot(x, step_avg_reward, 'r-', linewidth=3, alpha = 0.3)

    x, step_avg_reward = get_step_reward(avg_reward, step=20)
    plt.plot(x, step_avg_reward, 'r-', linewidth=1.5, alpha = 0.7)

    x, step_avg_reward = get_step_reward(avg_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)

    plt.plot(x, step_avg_reward, 'b-', linewidth=3, alpha = 0.3)
    plt.plot(x, weighted_moving_reward , 'b-', linewidth=3, alpha = 0.7)


    plt.show()
