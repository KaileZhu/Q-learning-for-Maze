import numpy as np
import os
class Q_learning():
    def __init__(self, action_space, state_dim):
        self.action_space = action_space
        self.action_dim = len(action_space)
        ## state_dim = [10, 10]
        self.state_dim = state_dim
        self.q_table = self.build_q_table()

    def build_q_table(self, pretrained = False, file_name = 'q_table'):
        if pretrained:
            q_table = self.load_q_table(file_name)
        else:
            q_table = np.zeros((self.state_dim[0] * self.state_dim[1], self.action_dim))
        return q_table

    def choose_action(self, state, episilon = 0.1):
        state_idx = self.state2idx(state, self.state_dim[1])
        ## avoid [0, 0, 0, 0] ,which lead to np.argmax always return 0 action
        if np.random.uniform(0, 1) < episilon or np.all(self.q_table[state_idx] == 0):
            action_idx = np.random.choice(self.action_dim)
        else:
            action_idx = np.argmax(self.q_table[state_idx])
        # return self.action_space[action_idx]
        return action_idx

    def update_q_table(self, state, next_state, action_idx, reward, alpha = 0.1, gamma = 0.6):
        state_idx = self.state2idx(state, self.state_dim[1])
        next_state_idx = self.state2idx(next_state, self.state_dim[1])
        old_value = self.q_table[state_idx][action_idx]
        next_max = np.max(self.q_table[next_state_idx])
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        self.q_table[state_idx][action_idx] = new_value

    def state2idx(self, state, column):
        ## 2D : matrix: row * column , matrix[i][j]
        ## 1D : res = i * column + j
        ## https://stackoverflow.com/questions/1730961/convert-a-2d-array-index-into-a-1d-index
        x = state[0]
        y = state[1]
        return column * x + y

    def save_q_table(self, file_name = 'q_table'):
        abs_dir = os.path.dirname(__file__);
        file_dir = os.path.join(abs_dir, '../result/' + file_name + '.npy');
        np.save(file_dir, self.q_table)

    def load_q_table(self, file_name = 'q_table'):
        abs_dir = os.path.dirname(__file__);
        file_dir = os.path.join(abs_dir, '../result/' + file_name + '.npy');
        return np.load(file_dir)


if __name__=="__main__":
    agent = Q_learning(action_space=[0,1,2,3], state_dim=[2, 2]);
    print(agent.build_q_table())

    agent.save_q_table('test')
    q_table = agent.load_q_table('test')
    print(q_table)

