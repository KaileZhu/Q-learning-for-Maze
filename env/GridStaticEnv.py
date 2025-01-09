import numpy as np

class Env():
    def __init__(self, height, width, radius):
        super(Env, self).__init__()
        # self.action_name = ['up', 'down', 'left', 'right']
        self.action_space = [0, 1, 2, 3]
        self.height = height
        self.width = width
        self.p = 0.95  # 地图中人的比例
        self.radius = radius
        # self.fake_data = data.Date_deal.gain_data()
        # self.data = data.Date_deal.gain_legal_date(self.fake_data)
        # print(self.data)
        # self.map = np.zeros([height, width])

        # TODOLIST: if human <= 2 we need to random this map again, to ensure the reward can converge...
        self.map = np.random.choice(a=[0, 1], size=((self.height, self.width)), p=[self.p, 1 - self.p])

        ## self.position = [height - 1, width - 1]
        ## start from the left and donw side
        self.position = [self.height - 1, 0]
        self.mode = 'edge'  # UAV从地图边缘随机生成
        self.max_steps = 200

        ## TODOLIST: fix error about the step_len out of boundary. DO NOT MODIFY HERE
        self.x_step_len = 1
        self.y_step_len = 1

    def step(self, action):
        self.update_position(action)
        next_state = self.position
        reward, done = self.get_reward()
        return next_state, reward, done

    def get_state(self):
        return self.position

    def reset(self):  # 重置UAV位置
        self.count = 0;
        ## TODOLISt: a random position for this agent!
        if self.mode == 'random':
            self.position = [np.random.randint(self.height), np.random.randint(self.width)]
        elif self.mode =='edge':
            up = [0, np.random.randint(self.width)]
            left = [np.random.randint(self.height),0]
            down = [self.height-1,np.random.randint(self.width)]
            right = [np.random.randint(self.height),self.width-1]
            choices =[up,down,right,left]
            self.position = choices[np.random.choice([0,1,2,3])]
        return self.position

    def render(self):  # 给出带UAV的地图输出为Render
        ## 这里还应该去除上一个时刻的状态
        render_map = np.copy(self.map)  # 赋值环境
        x = self.position[0]
        y = self.position[1]
        real_position = self.map[x][y]  # 读取地图上无人机位置处的数据
        print("     UAV Position:",x,y)
        if (real_position == 1):
            ## print("x = ", x, "y = ", y)
            render_map[x][y] = 3
        else:
            render_map[x][y] = 2
        print(render_map)
        return render_map

    def get_reward(self):
        reward = 0
        done = False;
        # time step penalty
        reward -= 0.5  # 随时间减少reward，使更短的步数得以被期待
        if (self.numsInCircle() > 0):
            reward += 1
        if (self.numsInCircle() > 1):
            reward += 2
        if (self.numsInCircle() > 2):
            reward += 4
        if (self.numsInCircle() >= 3):
            reward += 7
        if (self.numsInCircle() >= 4):
            reward += 11
            done = True
        if (self.count >= self.max_steps):
            ## we also need to add the count nums, if count > max nums done == true;
            reward -= 5
            done = True
        return reward, done

    def update_position(self, action):
        ## TODOLIST
        ## [height, width]
        ## left bound:0, right bound: width
        ## up bound: 0, down bound: height
        ## if the position is the corner...lead to bug
        x = self.position[0]
        y = self.position[1]
        # print("     Current action:", self.action_name[action])
        action = self.getLegalAction(action)
        # print("     Real action:", self.action_name[action])
        if (action == 0):
            self.position[0] = x - self.x_step_len
        elif (action == 1):
            self.position[0] = x + self.x_step_len
        elif (action == 2):
            self.position[1] = y - self.y_step_len
        elif (action == 3):
            self.position[1] = y + self.y_step_len
        self.count += 1
        return self.position

    def getLegalAction(self, action):
        x = self.position[0]
        y = self.position[1]
        if (x == 0 and action == 0):
            action = np.random.choice([1,2,3])
        if (x == self.height - 1 and action == 1):
            action = np.random.choice([0,2,3])
        if (y == 0 and action == 2):
            action = np.random.choice([0,1,3])
        if (y == self.width - 1 and action == 3):
            action = np.random.choice([0,1,2])

        if (x == 0 and y == 0 and (action == 0 or action == 2)):
            action = np.random.choice([1,3])
        if (x == 0 and y == self.width - 1 and (action == 0 or action == 3)):
            action = np.random.choice([1,2])
        if (x == self.height - 1 and y == 0 and (action == 1 or action == 2)):
            action = np.random.choice([0,3])
        if (x == self.height - 1 and y == self.width - 1 and (action == 1 or action == 3)):
            action = np.random.choice([0,2])

        return action

    def numsInCircle(self):
        ## how many points are inside the circle
        dists = self.getAllDistance()
        count = 0
        for i in range(len(dists)):
            if dists[i] < self.radius:
                count += 1
        return count

    def getAllDistance(self):
        ## calculate the distance of UAV and  each human
        human_pos = self.matrix2Coordinate()
        dists = []
        for i in range(len(human_pos)):
            dist = self.getDistance(human_pos[i])
            dists.append(dist)

        return dists

    def getDistance(self, point):
        return np.round( np.sqrt( (self.position[0] - point[0]) ** 2 +
                        (self.position[1] - point[1]) ** 2 ) , 2)

    def matrix2Coordinate(self):
        ## find the 1 in the map and convert them to coordinate
        ## [h, w] --> [[x0,y0],[x1,y1]...]
        coordinate = []
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == 1:
                    coordinate.append([i, j])
        return coordinate

    def map_create(self):
        pass


if __name__=="__main__":
    ###### Initialize ######
    env = Env(height=20, width=20, radius=5)
    env.p = 0.9
    # ###### Map test  #######
    # env.reset()
    #
    # print(env.map)
    # print(env.matrix2Coordinate())
    # print(env.getAllDistance())
    # print(env.numsInCircle())
    #
    # #########################
    #
    # next_state, reward = env.step(0)
    # print("next state:", next_state, ", reward:", reward)
    ##########################

    print("==============================")
    print("LOOP TEST:")

    ######### loop test #####

    env.reset()
    done = False
    print("Initialize the map...")
    print("==============================")
    rewards = []
    avg_reward = []
    for i in range(100):
        env.reset()
        rewards = []
        while not done:
            # action = 0
            action = np.random.choice([0, 1, 2, 3])
            env.render()
            next_state, reward, done = env.step(action)
             #print("next state:", next_state, ", reward:", reward)
            print("==============================")
            rewards.append(reward)
        avg_reward.append(np.round(sum(rewards)/env.count,2))
        done = False
    print("==============================")


