import pygame as pg
import sys
import setting as st
from pygame import *
from pygame.locals import QUIT
import frame

SNAKEMOVEEVENT = pg.USEREVENT + 0
pg.time.set_timer(SNAKEMOVEEVENT,150)

def event(listSnake):
    while True:
        for ev in pg.event.get():
            if ev.type == SNAKEMOVEEVENT:
                if st.gameStop == True:
                    pg.time.set_timer(SNAKEMOVEEVENT,0)
                    pg.event.clear()
                else:
                    listSnake[0].move()
                    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
                    frame.sf.blit(st.imageApple, st.transformLocationToCoordinate(st.imageAppleLocation))
                    frame.sf.blit(listSnake[0].image, st.transformLocationToCoordinate(listSnake[0].location))
                    frame.sf.blit(listSnake[1].image, st.transformLocationToCoordinate(listSnake[1].location))
                    frame.sf.blit(listSnake[2].image, st.transformLocationToCoordinate(listSnake[2].location))
                    frame.wd.blit(frame.sf, (0, 0))
                    pg.display.update()
            elif ev.type == QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == KEYDOWN:
                if ev.key == K_RIGHT:
                    if listSnake[0].direction == "left":
                        pass
                    else:
                        if listSnake[0].direction == "up":
                            st.rotateSnakeHead(270,listSnake,frame.sf,frame.wd)
                        elif listSnake[0].direction == "down":
                            st.rotateSnakeHead(90,listSnake,frame.sf,frame.wd)
                        listSnake[0].direction = "right"
                elif ev.key == K_LEFT:
                    if listSnake[0].direction == "right":
                        pass
                    else:
                        if listSnake[0].direction == "up":
                            st.rotateSnakeHead(90,listSnake,frame.sf,frame.wd)
                        elif listSnake[0].direction == "down":
                            st.rotateSnakeHead(270,listSnake,frame.sf,frame.wd)
                        listSnake[0].direction = "left"
                elif ev.key == K_UP:
                    if listSnake[0].direction == "down":
                        pass
                    else:
                        if listSnake[0].direction == "right":
                            st.rotateSnakeHead(90,listSnake,frame.sf,frame.wd)
                        elif listSnake[0].direction == "left":
                            st.rotateSnakeHead(270,listSnake,frame.sf,frame.wd)
                        listSnake[0].direction = "up"
                elif ev.key == K_DOWN:
                    if listSnake[0].direction == "up":
                        pass
                    else:
                        if listSnake[0].direction == "right":
                            st.rotateSnakeHead(270,listSnake,frame.sf,frame.wd)
                        elif listSnake[0].direction == "left":
                            st.rotateSnakeHead(90,listSnake,frame.sf,frame.wd)
                        listSnake[0].direction = "down"
                print(listSnake[0].direction)