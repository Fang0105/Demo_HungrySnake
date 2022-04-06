import pygame as pg
import setting as st
import event
import apple

pg.init()

#設定視窗
pg.display.set_caption(st.gameName)
wd = pg.display.set_mode(st.windowsSize)

#設定Surface
sf = pg.Surface(wd.get_size())
sf.blit(st.imageBackGround,st.imageBackGroundLocation)
sf.blit(st.imageApple,apple.getRandomAppleLocation())
'''
sf.blit(st.imageSnakeHead,(222.5+st.latticeSize*5,st.latticeSize*5))
sf.blit(st.imageSnakeBody,(222.5+st.latticeSize*5,st.latticeSize*6))
'''
wd.blit(sf,(0,0))

pg.draw.rect(sf,(255,0,0),st.rectTime)
pg.draw.rect(sf,(255,0,0),st.rectScore)
pg.draw.rect(sf,(255,0,0),st.rectRank)
sf.blit(st.txtTime,st.txtTime.get_rect(center=st.rectTime.center))
sf.blit(st.txtScore,st.txtScore.get_rect(center=st.rectScore.center))
sf.blit(st.txtRank,st.txtRank.get_rect(center=st.rectRank.center))

wd.blit(sf,(0,0))

pg.display.update()

event.event()