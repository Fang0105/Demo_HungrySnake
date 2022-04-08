import pygame as pg
import setting as st

pg.init()

#設定視窗
pg.display.set_caption(st.gameName)
wd = pg.display.set_mode(st.windowsSize)

#設定Surface
sf = pg.Surface(wd.get_size())

