import pygame as pg
import constants as c

class Paddle:
    def __init__(self):
        self.pos = pg.math.Vector2(500, 750)
        self.height = 20
        self.width = 100

    def update(self):
        self.pos = (pg.mouse.get_pos()[0] - 50, 750)

    def render(self, s):
        pg.draw.rect(s,c.GREEN, self.rect())

    def rect(self):
        return pg.Rect(self.pos[0], 750, self.width, self.height)