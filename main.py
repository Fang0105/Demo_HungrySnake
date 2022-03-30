import pygame as pg
import setting
import setting as st
import sys
from pygame.locals import QUIT

pg.init()

#設定視窗
pg.display.set_caption(st.gameName)
wd = pg.display.set_mode(st.windowsSize)

#設定Surface
sf = pg.Surface(wd.get_size())
sf.blit(st.imageBackGround,st.imageBackGroundLocation)

wd.blit(sf,(0,0))



pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()