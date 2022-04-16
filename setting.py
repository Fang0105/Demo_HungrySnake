import pygame as pg
import pandas as pd

pg.init()
windowsSize=(1000,777.5)
gameName='Hungry Snake'

imageBackGround = pg.image.load('background.png')
imageBackGroundLocation = (222.5,0)
latticeSize = 777.5/16

score = 0

font = pg.font.Font(None,70)

txtLabelTime = font.render("TIME",True,(255,255,0))
rectTimeText = pg.Rect(0,0,222.5,50)

txtLabelScore = font.render("SCORE",True,(255,255,0))
rectScoreText = pg.Rect(0,200,222.5,50)

txtLabelRank = font.render("RANK",True,(255,255,0))
rectRankText = pg.Rect(0,400,222.5,50)

def transformLocationToCoordinate(location):
    location = (222.5+latticeSize*location[0],latticeSize*location[1])
    return location

def drawScore(sf,wd):
    fontScore = pg.font.Font(None, 190)
    txtScore = fontScore.render(str(score), True, (255, 255, 0))
    rectScore = pg.Rect(0, 250, 222.5, 150)
    pg.draw.rect(sf, (255, 0, 255), rectScore)
    sf.blit(txtScore,txtScore.get_rect(center=rectScore.center))
    wd.blit(sf, (0, 0))

imageApple = pg.image.load('apple.png')
imageApple = pg.transform.scale(imageApple,(latticeSize,latticeSize))
imageAppleLocation = (None,None)

imageSnakeHead = pg.image.load('snakeHead.png')
imageSnakeHead = pg.transform.scale(imageSnakeHead,(latticeSize,latticeSize))
imageSnakeHead = pg.transform.rotate(imageSnakeHead,270)
imageSnakeBody = pg.image.load('snakeBody.png')
imageSnakeBody = pg.transform.scale(imageSnakeBody,(latticeSize,latticeSize))

listSnake = []

direction = "right"

def rotateSnakeHead(degree):
    listSnake[0].image = pg.transform.rotate(listSnake[0].image, degree)

setLocation = set()

shouldGenerateNewApple = False

gameStop = False

hasMoved = False

minute = 0
second = 0
def getClock():
    strSecond = str(second)
    strMinute = str(minute)
    if second<10:
        strSecond = "0"+strSecond
    if minute<10:
        strMinute = "0"+strMinute
    return (strMinute+":"+strSecond)

def addOneSecond():
    global second
    global minute
    second += 1
    if second == 60:
        second = 0
        minute += 1
def drawClock(sf):
    fontClock = pg.font.Font(None, 120)
    txtClock = fontClock.render(getClock(), True, (255, 255, 0))
    rectClock = pg.Rect(0, 50, 222.5, 150)
    pg.draw.rect(sf, (255, 0, 255), rectClock)
    sf.blit(txtClock,txtClock.get_rect(center=rectClock.center))

def drawRank(sf):
    record = pd.read_csv("record.csv")
    fontRank = pg.font.Font(None,30)
    txtRankRank = fontRank.render("rank",True,(0,0,0))
    rectRankRank = pg.Rect(0,450,50,27.5)
    pg.draw.rect(sf,(0,255,0),rectRankRank)
    sf.blit(txtRankRank,txtRankRank.get_rect(center=rectRankRank.center))
    txtRankScore = fontRank.render("score",True,(0,0,0))
    rectRankScore = pg.Rect(50, 450, 80, 27.5)
    pg.draw.rect(sf, (255, 255, 255), rectRankScore)
    sf.blit(txtRankScore, txtRankScore.get_rect(center=rectRankScore.center))
    txtRankTime = fontRank.render("time", True, (0, 0, 0))
    rectRankTime = pg.Rect(130, 450, 92.5, 27.5)
    pg.draw.rect(sf, (0, 255, 255), rectRankTime)
    sf.blit(txtRankTime, txtRankTime.get_rect(center=rectRankTime.center))
    for i in range(0,6):
        rank = str(i+1)
        score = str(record.at[i,"score"])
        time = record.at[i,"time"]
        txtRecordRank = fontRank.render(rank, True, (0, 0, 0))
        rectRecordRank = pg.Rect(0, 477.5+50*i, 50, 50)
        pg.draw.rect(sf, (250, 255, 0), rectRecordRank)
        sf.blit(txtRecordRank, txtRecordRank.get_rect(center=rectRecordRank.center))
        txtRecordScore = fontRank.render(score, True, (0, 0, 0))
        rectRecordScore = pg.Rect(50, 477.5+50*i, 80, 50)
        pg.draw.rect(sf, (250, 0, 255), rectRecordScore)
        sf.blit(txtRecordScore, txtRecordScore.get_rect(center=rectRecordScore.center))
        txtRecordTime = fontRank.render(time, True, (0, 0, 0))
        rectRecordTime = pg.Rect(130, 477.5+50*i, 92.5, 50)
        pg.draw.rect(sf, (255, 0, 0), rectRecordTime)
        sf.blit(txtRecordTime, txtRecordTime.get_rect(center=rectRecordTime.center))

newSurfaceSize = (windowsSize[0]/4,windowsSize[1]/4)
newSurfaceLocation = (windowsSize[0]*3/8,windowsSize[1]*3/8)