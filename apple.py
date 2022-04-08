import setting as st
import random
import pygame as pg

def getRandomAppleCoordinate():
    st.imageAppleLocation = (random.randint(0, 15),random.randint(0, 15))
    while st.imageAppleLocation in st.setLocation == True:
        st.imageAppleLocation = (random.randint(0, 15), random.randint(0, 15))
    st.setLocation.add(st.imageAppleLocation)
    return st.transformLocationToCoordinate(st.imageAppleLocation)

def drawApple(sf,wd):

    sf.blit(st.imageBackGround, st.imageBackGroundLocation)
    sf.blit(st.imageApple, getRandomAppleCoordinate())
    wd.blit(sf, (0, 0))

def generateNewApple(sf,wd):
    st.setLocation.remove(st.imageAppleLocation)
    sf.blit(st.imageBackGround, st.imageBackGroundLocation)
    sf.blit(st.imageApple, getRandomAppleCoordinate())
    wd.blit(sf, (0, 0))
    st.setLocation.add(st.imageAppleLocation)
    pg.display.update()