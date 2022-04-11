import pygame as pg

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

txtLabelRank = font.render("Rank",True,(255,255,0))
rectRankText = pg.Rect(0,400,222.5,50)

def transformLocationToCoordinate(location):
    location = (222.5+latticeSize*location[0],latticeSize*location[1])
    return location

def drawScore(sf,wd):
    fontScore = pg.font.Font(None, 200)
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

