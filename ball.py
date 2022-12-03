import pygame as pg
import random
import constants as c

class Ball:
    def __init__(self):
        self.pos = pg.math.Vector2(random.random()*800, 700)
        # keep a normalized velocity vector (for direction) and a float for speed.
        self.speed = 3.0
        self.radius = 10
        self.vNormal = pg.math.Vector2(1,-1).normalize()

    def render(self, screen):
        pg.draw.circle(screen, c.GREEN,self.pos, self.radius)

    # this is quite complicated.  It would be easy enough to just add the velocity vector
    # to the position, but oh no...I had to do it right.  The velocity vector, dependingon magnitude,
    # can carry you partway through the wall so I have to scale it by a fractional factor if a
    # collision has occurred.  So for each collision we calculate a fraction which represents how
    # much of the full movement can be used before collding.  We pick the smallest fraction when
    # multiple collisions occur, and then just move a fractional amount.
    def update(self, paddleRect:pg.Rect):
        frac = 1.0
        retval = True
        refVec = None
        if self.vNormal.x < 0:
            # going left?  Check for left wall collision
            frac2 = abs((self.pos.x - self.radius) / (self.vNormal * self.speed).x)
            if frac2 < frac:
                frac = frac2
                refVec = pg.math.Vector2(1,0)
                print("bounce left")

        if self.vNormal.x > 0:
            # going right?  Check for right wall collision
            frac2 = abs(((self.pos.x + self.radius)-1000) / (self.vNormal * self.speed).x)
            if frac2 < frac:
                frac = frac2
                refVec = pg.math.Vector2(-1,0)
                print("bounce right")

        if self.vNormal.y < 0:
            # going up?  Check for roof collision
            frac2 = abs(((self.pos.y - self.radius) - 0) / (self.vNormal * self.speed).y)
            if frac2 < frac:
                frac = frac2
                refVec = pg.math.Vector2(0,1)

        if self.vNormal.y > 0:
            # going down?  Check for collision with the paddle
            frac2 = abs(((self.pos.y + self.radius) - paddleRect.y) / (self.vNormal * self.speed).y)
            if frac2 < frac:
                # possible collision with the paddle
                frac = frac2
                if paddleRect.x <= (self.pos + (self.vNormal * self.speed * frac2)).x <= paddleRect.x+paddleRect.w:
                    refVec = pg.math.Vector2(0,-1)
                else:
                    retval = False
        self.pos += self.vNormal * self.speed * frac
        if refVec:
            self.vNormal = self.vNormal.reflect(refVec)
        return retval
