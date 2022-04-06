import pygame as pg
import sys
from pygame.locals import QUIT

def event():
    while True:
        for ev in pg.event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
