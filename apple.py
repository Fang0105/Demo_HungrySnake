import setting as st
import frame
import random
import pygame as pg

'''
實作蘋果的相關方法
'''

#隨機取得蘋果的螢幕座標
def getRandomAppleCoordinate():
    st.imageAppleLocation = (random.randint(0, 15),random.randint(0, 15))
    while st.imageAppleLocation in st.setLocation:
        st.imageAppleLocation = (random.randint(0, 15), random.randint(0, 15))
    st.setLocation.add(st.imageAppleLocation)
    return st.transformLocationToCoordinate(st.imageAppleLocation)

#繪製蘋果
def drawApple():
    frame.sf.blit(st.imageApple, getRandomAppleCoordinate())

#隨機生成蘋果
def generateNewApple():
    st.shouldGenerateNewApple = False
    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
    frame.sf.blit(st.imageApple, getRandomAppleCoordinate())
    frame.wd.blit(frame.sf, (0, 0))
    st.setLocation.add(st.imageAppleLocation)
    pg.display.update()