import matplotlib.pyplot as plt
import numpy as np

# self.action_name = ['up', 'down', 'left', 'right']
# self.action_space = [0, 1, 2, 3]

def get_action_idx(q_table, colunm, x, y):
    state_idx = colunm * x + y
    action_idx = np.argmax(q_table[state_idx])
    return action_idx;

if __name__=="__main__":

    map = np.load('result/map.npy')
    q_table = np.load('result/q_table.npy')

    render_map = np.copy(map)

    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            action_idx = get_action_idx(q_table, map.shape[1], i, j)
            render_map[i][j] = action_idx

    print(map)
    print(render_map)
    print(np.round(q_table,2))

    ax1 = plt.subplot(2, 2, 1)
    plt.imshow(map, cmap = 'gray')

    ax2 = plt.subplot(2, 2, 2)
    plt.imshow(render_map)

    plt.show()


