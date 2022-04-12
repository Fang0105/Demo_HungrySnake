import pygame as pg
import sys
import setting as st
import pandas as pd
from pygame import *
from pygame.locals import QUIT
import frame
import snake
import rank

SNAKEMOVEEVENT = pg.USEREVENT + 0

CHECKHASMOVEDEVENT = pg.USEREVENT + 1
pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))

CLOCKEVENT = pg.USEREVENT + 2

def event():
    while True:
        for ev in pg.event.get():
            if ev.type == CLOCKEVENT:
                st.addOneSecond()
                st.drawClock(frame.sf)
                frame.wd.blit(frame.sf,(0,0))
                pg.display.update()
            elif ev.type == CHECKHASMOVEDEVENT:
                if st.hasMoved == False:
                    pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))
                else:
                    pg.time.set_timer(CLOCKEVENT, 1000)
                    pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
            elif ev.type == SNAKEMOVEEVENT:
                if st.gameStop == True:
                    pg.time.set_timer(SNAKEMOVEEVENT,0)
                    pg.time.set_timer(CLOCKEVENT,0)
                    pg.event.clear()
                    rank.df = pd.concat([rank.df,pd.DataFrame({
                        "score":[st.score],
                        "time":[st.getClock()]
                    })],axis=0)
                    rank.sort()
                    rank.doRecord()
                    st.drawRank(frame.sf)
                    frame.wd.blit(frame.sf,(0,0))
                    pg.display.update()
                else:
                    snake.snakeMove()
                    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
                    frame.sf.blit(st.imageApple, st.transformLocationToCoordinate(st.imageAppleLocation))
                    for i in st.listSnake:
                        frame.sf.blit(i.image,st.transformLocationToCoordinate(i.location))
                    st.drawScore(frame.sf,frame.wd)
                    frame.wd.blit(frame.sf,(0,0))
                    pg.display.update()
                    pg.time.set_timer(SNAKEMOVEEVENT,150)
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
                            st.rotateSnakeHead(270)
                        elif st.listSnake[0].direction == "down":
                            st.rotateSnakeHead(90)
                        st.listSnake[0].direction = "right"
                        pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
                elif ev.key == K_LEFT:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "right":
                        pass
                    else:
                        if st.listSnake[0].direction == "up":
                            st.rotateSnakeHead(90)
                        elif st.listSnake[0].direction == "down":
                            st.rotateSnakeHead(270)
                        st.listSnake[0].direction = "left"
                        pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
                elif ev.key == K_UP:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "down":
                        pass
                    else:
                        if st.listSnake[0].direction == "right":
                            st.rotateSnakeHead(90)
                        elif st.listSnake[0].direction == "left":
                            st.rotateSnakeHead(270)
                        st.listSnake[0].direction = "up"
                        pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
                elif ev.key == K_DOWN:
                    st.hasMoved = True
                    if st.listSnake[0].direction == "up":
                        pass
                    else:
                        if st.listSnake[0].direction == "right":
                            st.rotateSnakeHead(270)
                        elif st.listSnake[0].direction == "left":
                            st.rotateSnakeHead(90)
                        st.listSnake[0].direction = "down"
                        pg.event.post(pg.event.Event(SNAKEMOVEEVENT))