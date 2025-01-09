import pygame as pg
import numpy as np
import sys
from env.GridStaticEnv import Env

height = 10
width = 10
radius = 2
env = Env(height, width, radius=radius)

pg.init()

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
colors = np.array([[255, 255, 255], [220, 20, 60], [0, 0, 142], [128, 0, 128]])

# gridarray = np.random.choice(a=[0,1], size=((height,width)), p=[p, 1 - p])

done = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            pg.quit()
            sys.exit()
    for i in range(100):
        env.reset()
        gridarray = env.render()
        rewards = []
        surface = pg.surfarray.make_surface(colors[gridarray])
        while not done:
            # action = 0
            action = np.random.choice([0, 1, 2, 3])
            gridarray = env.render()
            ## gridarray = np.random.randint(3, size=(20, 20))
            surface = pg.surfarray.make_surface(colors[gridarray])
            surface = pg.transform.scale(surface, (400, 400))  # Scaled a bit.
            next_state, reward, done = env.step(action)
            # screen.fill((30, 30, 30))
            screen.blit(surface, (0, 0))
            pg.display.flip()
            clock.tick(5)
            pg.time.delay(100)
        done = False

    running = False





