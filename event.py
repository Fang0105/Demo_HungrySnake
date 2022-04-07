import pygame as pg
import sys
import setting as st
from pygame import *
from pygame.locals import QUIT
import game
import apple

def event(wd,sf):
    while True:
        for ev in pg.event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == KEYDOWN:
                if ev.key == K_RIGHT:
                    if st.direction == "left":
                        pass
                    else:
                        if st.direction == "up":
                            st.rotateSnakeHead(270,game.listSnake,sf,wd)
                        elif st.direction == "down":
                            st.rotateSnakeHead(90,game.listSnake,sf,wd)
                        st.direction = "right"
                elif ev.key == K_LEFT:
                    if st.direction == "right":
                        pass
                    else:
                        if st.direction == "up":
                            st.rotateSnakeHead(90,game.listSnake,sf,wd)
                        elif st.direction == "down":
                            st.rotateSnakeHead(270,game.listSnake,sf,wd)
                        st.direction = "left"
                elif ev.key == K_UP:
                    if st.direction == "down":
                        pass
                    else:
                        if st.direction == "right":
                            st.rotateSnakeHead(90,game.listSnake,sf,wd)
                        elif st.direction == "left":
                            st.rotateSnakeHead(270,game.listSnake,sf,wd)
                        st.direction = "up"
                elif ev.key == K_DOWN:
                    if st.direction == "up":
                        pass
                    else:
                        if st.direction == "right":
                            st.rotateSnakeHead(270,game.listSnake,sf,wd)
                        elif st.direction == "left":
                            st.rotateSnakeHead(90,game.listSnake,sf,wd)
                        st.direction = "down"
                print(st.direction)