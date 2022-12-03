import pygame as pg
import paddle
import ball
import constants as c

pg.init()
disp = pg.display.set_mode((1000, 800))
clock = pg.time.Clock()


run = True

p = paddle.Paddle()
b = ball.Ball()
# main game loop
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    disp.fill(c.WHITE)
    p.update()
    run = run and b.update(p.rect())
    p.render(disp)
    b.render(disp)
    pg.display.flip()
    clock.tick(100)

