import pygame as pg

import setting
import setting as st
import sys
from pygame.locals import QUIT

pg.init()
display=pg.display.set_mode(st.windowsSize)
pg.display.set_caption(st.gameName)
display.blit(setting.imageBackGround,st.imageBackGroundLocation)

pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()