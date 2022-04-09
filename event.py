import pygame as pg
import sys
import setting as st
from pygame import *
from pygame.locals import QUIT
import frame



CHECKHASMOVEDEVENT = pg.USEREVENT + 1
pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))

SNAKEMOVEEVENT = pg.USEREVENT + 0

def event():
    while True:
        for ev in pg.event.get():
            if ev.type == CHECKHASMOVEDEVENT:
                if st.hasMoved == False:
                    pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))
                else:
                    pg.time.set_timer(SNAKEMOVEEVENT,150)
            elif ev.type == SNAKEMOVEEVENT:
                if st.gameStop == True:
                    pg.time.set_timer(SNAKEMOVEEVENT,0)
                    pg.event.clear()
                else:
                    st.listSnake[0].move()
                    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
                    frame.sf.blit(st.imageApple, st.transformLocationToCoordinate(st.imageAppleLocation))
                    frame.sf.blit(st.listSnake[0].image, st.transformLocationToCoordinate(st.listSnake[0].location))
                    frame.sf.blit(st.listSnake[1].image, st.transformLocationToCoordinate(st.listSnake[1].location))
                    frame.sf.blit(st.listSnake[2].image, st.transformLocationToCoordinate(st.listSnake[2].location))
                    frame.wd.blit(frame.sf, (0, 0))
                    pg.display.update()
            elif ev.type == QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == KEYDOWN:
                if ev.key == K_RIGHT:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "left":
                        pass
                    else:
                        if st.listSnake[0].direction == "up":
                            st.rotateSnakeHead(270,frame.sf,frame.wd)
                        elif st.listSnake[0].direction == "down":
                            st.rotateSnakeHead(90,frame.sf,frame.wd)
                        st.listSnake[0].direction = "right"
                elif ev.key == K_LEFT:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "right":
                        pass
                    else:
                        if st.listSnake[0].direction == "up":
                            st.rotateSnakeHead(90,frame.sf,frame.wd)
                        elif st.listSnake[0].direction == "down":
                            st.rotateSnakeHead(270,frame.sf,frame.wd)
                        st.listSnake[0].direction = "left"
                elif ev.key == K_UP:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "down":
                        pass
                    else:
                        if st.listSnake[0].direction == "right":
                            st.rotateSnakeHead(90,frame.sf,frame.wd)
                        elif st.listSnake[0].direction == "left":
                            st.rotateSnakeHead(270,frame.sf,frame.wd)
                        st.listSnake[0].direction = "up"
                elif ev.key == K_DOWN:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "up":
                        pass
                    else:
                        if st.listSnake[0].direction == "right":
                            st.rotateSnakeHead(270,frame.sf,frame.wd)
                        elif st.listSnake[0].direction == "left":
                            st.rotateSnakeHead(90,frame.sf,frame.wd)
                        st.listSnake[0].direction = "down"
                #print(st.listSnake[0].direction)