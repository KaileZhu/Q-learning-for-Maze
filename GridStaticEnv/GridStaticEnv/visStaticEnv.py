import pygame as pg  # 命名为pg
import numpy as np
import sys
from GridStaticEnv import Env
from QLearning import Q_learning

def cal_pos(position):  # 得到实际尺度对应的可视化尺度
    m = (position[0] + 0.5) * pixel / height
    n = (position[1] + 0.5) * pixel / width
    radius_fake = radius * pixel / height
    pos_fake = [m, n]
    return pos_fake, radius_fake

height = 20
width = 20
radius = 5
env = Env(height, width, radius=radius)
epsilon = 0.1
episode = 5000  # 调试结束后期尽可能增大训练回合以获得较好训练效果
pixel = 500  # 像素

# pg.init()  # 初始化pygame，并检查pygame包是否完整
# pg.display.set_caption("可视化俯视图")  # 命名

# screen = pg.display.set_mode((pixel, pixel))  # 创建新的Surface对象，图形显示与此(宽高)，即像素
clock = pg.time.Clock()  # 设置帧率
colors = np.array([[255, 255, 255], [100, 149, 237], [173, 255, 47], [128, 0, 128]])  # 将列表转化为数组
                 #  [255 255 255] 普通地面 ——0
                 #  [100 149 237] 地面用户 ——1
                 #  [  0   0 142]   UAV  ——2
                 #  [128   0 128] 重叠位置 ——3

# gridarray = np.random.choice(a=[0,1], size=((height,width)), p=[p, 1 - p])

done = False
running = True
state = env.reset()  # 重置UAV并获取当前位置

while running:
    # for event in pg.event.get():  # 监视键盘和鼠标事件
    #     if event.type == pg.QUIT:
    #         pg.display.quit()
    #         pg.quit()  # 与init（）相反，pg.QUIT会使pygame停止运行
    #         sys.exit()  # 终止程序
    for i in range(episode):  # 如果事件不是quit就执行移动程序
        env.reset()  # 重置UAV的位置
        gridarray = env.render(0)  # 输出带UAV的地图
        rewards = []
        time = []
        # surface = pg.surfarray.make_surface(colors[gridarray])  # 中间是为栅栏网格染色

        while not done:
            # action = 0
            action = np.random.choice([0, 1, 2, 3])  # 第一步随机探索
            action = env.getLegalAction(action)
            time.append(action)
            # print(len(time))
            gridarray = env.render(len(time))  # 输出带UAV的地图
            # surface = pg.surfarray.make_surface(colors[gridarray])  # 将新数组赋值给surface
            # surface = pg.transform.scale(surface, (pixel, pixel))  # Scaled a bit. 改变游戏界面的尺寸
            # screen.fill((192, 192, 192))  # 设置背景颜色
            # screen.blit(surface, (0, 0))

            current_state = env.get_state()
            pos_fake, radius_fake = cal_pos(current_state)
            # pg.draw.circle(screen, [255, 97, 0], pos_fake, radius_fake, width=1)
            # pg.display.flip()  # 让最近绘制的屏幕可见
            # pg.display.update()

            next_state, reward, done = env.step(action)  # 改用ppo的算法

            # clock.tick(1000)  # 设置帧率
            # pg.time.delay(80)

        done = False
    running = False