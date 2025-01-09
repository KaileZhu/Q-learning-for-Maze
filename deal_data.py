import csv

class Date_deal():
    def __init__(self):
        self.data_set = []  # 最初数据集的集合
        self.data_len = 3  # 数据集数量
        self.num_users = 3  # 共三个用户
        self.num_dataSet = 2 * self.num_users
        file_name = "data/trans_data_Train1th_User{}th.csv"
        for i in range(self.data_len):
            data = open(file_name.format(i+1, "r"))
            self.data_set.append(data)

    def gain_data(self):
        get_data = []
        user_1_x = []
        user_1_y = []
        user_2_x = []
        user_2_y = []
        user_3_x = []
        user_3_y = []
        users_data = [user_1_x, user_1_y, user_2_x,
                      user_2_y, user_3_x, user_3_y]

        for i in range(self.num_dataSet):  # i从0-5分别代表users_data的六个空数据集
            j = int(i/2)  # j代表从0-2的三个用户
            m = i - 2*j  # m代表是x坐标还是y坐标
            rows = csv.reader(self.data_set[j])  # 读取对应用户的数据
            for row in rows:
                data_now = users_data[i]
                data_now.append(row[m])
            get_data.append(data_now)
        return get_data

    def gain_legal_date(self, users_data):  # 为数据集删掉0位置处标签
        real_data = []
        for i in range(self.num_dataSet):  # i从0-5代表users_data的六个空数据集
            data_legal = users_data[i]
            data_legal.remove(data_legal[0])
            real_data.append(data_legal)
        return real_data

if __name__ == "__main__":
    trans = Date_deal()
    fake_users_data = trans.gain_data()
    real_data = trans.gain_legal_date(fake_users_data)
    # print(len(real_data))
    # print(real_data)
