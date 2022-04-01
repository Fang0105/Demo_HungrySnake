import pygame as pg
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
sf.blit(st.imageApple,st.getRandomAppleLocation())
wd.blit(sf,(0,0))

pg.draw.rect(sf,(255,0,0),st.rectTime)
pg.draw.rect(sf,(255,0,0),st.rectScore)
pg.draw.rect(sf,(255,0,0),st.rectRank)
sf.blit(st.txtTime,st.txtTime.get_rect(center=st.rectTime.center))
sf.blit(st.txtScore,st.txtScore.get_rect(center=st.rectScore.center))
sf.blit(st.txtRank,st.txtRank.get_rect(center=st.rectRank.center))

wd.blit(sf,(0,0))

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()