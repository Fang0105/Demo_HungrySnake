import pygame as pg
import sys
import setting as st
from pygame import *
from pygame.locals import QUIT
import frame
import snake



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
                    pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
            elif ev.type == SNAKEMOVEEVENT:
                if st.gameStop == True:
                    pg.time.set_timer(SNAKEMOVEEVENT,0)
                    pg.event.clear()
                    print(st.score)
                    print(len(st.listSnake))
                else:
                    snake.snakeMove()
                    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
                    frame.sf.blit(st.imageApple, st.transformLocationToCoordinate(st.imageAppleLocation))
                    for i in st.listSnake:
                        frame.sf.blit(i.image,st.transformLocationToCoordinate(i.location))
                    st.drawScore(frame.sf,frame.wd)
                    frame.wd.blit(frame.sf,(0,0))
                    pg.display.update()
                    pg.time.set_timer(SNAKEMOVEEVENT,130)
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