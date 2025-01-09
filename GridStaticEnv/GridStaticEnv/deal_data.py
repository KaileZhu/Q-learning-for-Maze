import csv

class DateDeal():
    def __init__(self):
        self.data_set_x = []  # 最初数据集的集合（x坐标）
        self.data_set_y = []  # 最初数据集的集合（y坐标）
        self.num_users = 3  # 共三个用户
        self.file_name_x = "data/trans_data_Train1th_User{}th-x.csv"
        self.file_name_y = "data/trans_data_Train1th_User{}th-y.csv"
        for i in range(self.num_users):
            data_x = open(self.file_name_x.format(i+1, "r"))
            data_y = open(self.file_name_y.format(i+1, "r"))
            self.data_set_x.append(data_x)  # 读取数据文件夹
            self.data_set_y.append(data_y)

    def gain_data(self):
        user_1_x = []
        user_1_y = []
        user_2_x = []
        user_2_y = []
        user_3_x = []
        user_3_y = []
        data_x = [user_1_x, user_2_x, user_3_x]
        data_y = [user_1_y, user_2_y, user_3_y]

        for i in range(self.num_users):
            rows = csv.reader(self.data_set_x[i])
            for row in rows:
                data_x[i].append(row[0])
            data_x[i].remove(data_x[i][0])

        for i in range(self.num_users):
            rows = csv.reader(self.data_set_y[i])
            for row in rows:
                data_y[i].append(row[0])
            data_y[i].remove(data_y[i][0])
        return data_x, data_y

if __name__ == "__main__":
    trans = DateDeal()
    data_x, data_y = trans.gain_data()
    # for i in range(3):
    #     print(data_x[i])
    #     print(data_y[i])
    print(len(data_x[0]))

