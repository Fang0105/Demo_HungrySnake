import pygame as pg
import sys
import regame
import setting as st
import pandas as pd
from pygame import *
from pygame.locals import QUIT
import frame
import snake
import rank

'''
處理所有事件
'''

#蛇移動
SNAKEMOVEEVENT = pg.USEREVENT + 0

#檢查蛇是否已經移動
CHECKHASMOVEDEVENT = pg.USEREVENT + 1

#增加遊戲時間
CLOCKEVENT = pg.USEREVENT + 2

#處理事件的迴圈並回傳是否再來一局
def event():
    pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))
    while True:
        for ev in pg.event.get():
            #判斷是否在來一局
            if ev.type == pg.MOUSEBUTTONDOWN:
                if st.gameStop == True:
                    pos = (ev.pos[0]-373,ev.pos[1]-290)
                    if regame.rectYes.collidepoint(pos):
                        return True
                    if regame.rectNo.collidepoint(pos):
                        return False
            #增加遊戲時間
            elif ev.type == CLOCKEVENT:
                st.addOneSecond()
                st.drawClock(frame.sf)
                frame.wd.blit(frame.sf,(0,0))
                pg.display.update()
            #檢查蛇是否已經移動
            elif ev.type == CHECKHASMOVEDEVENT:
                if st.hasMoved == False:
                    pg.event.post(pg.event.Event(CHECKHASMOVEDEVENT))
                else:
                    pg.time.set_timer(CLOCKEVENT, 1000)
                    pg.event.post(pg.event.Event(SNAKEMOVEEVENT))
            #蛇往行進方向移動一格
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
                    frame.wd.blit(regame.renew(st.score==253),st.newSurfaceLocation)
                    pg.display.update()
                else:
                    if st.score==253:
                        st.gameStop = True
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
            #蛇的轉向
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