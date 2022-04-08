import pygame as pg

pg.init()
windowsSize=(1000,777.5)
gameName='Hungry Snake'

imageBackGround = pg.image.load('background.png')
imageBackGroundLocation = (222.5,0)
latticeSize = 777.5/16

font = pg.font.Font(None,70)
txtTime = font.render("TIME",True,(255,255,0))
rectTime = pg.Rect(0,0,222.5,50)
txtScore = font.render("SCORE",True,(255,255,0))
rectScore = pg.Rect(0,200,222.5,50)
txtRank = font.render("Rank",True,(255,255,0))
rectRank = pg.Rect(0,400,222.5,50)

def transformLocationToCoordinate(location):
    location = (222.5+latticeSize*location[0],latticeSize*location[1])
    return location

imageApple = pg.image.load('apple.png')
imageApple = pg.transform.scale(imageApple,(latticeSize,latticeSize))
imageAppleLocation = (None,None)

imageSnakeHead = pg.image.load('snakeHead.png')
imageSnakeHead = pg.transform.scale(imageSnakeHead,(latticeSize,latticeSize))
imageSnakeHead = pg.transform.rotate(imageSnakeHead,270)
imageSnakeBody = pg.image.load('snakeBody.png')
imageSnakeBody = pg.transform.scale(imageSnakeBody,(latticeSize,latticeSize))

direction = "right"

def rotateSnakeHead(degree,ls,sf,wd):
    ls[0].image = pg.transform.rotate(ls[0].image, degree)
    sf.blit(imageBackGround, imageBackGroundLocation)
    sf.blit(imageApple, transformLocationToCoordinate(imageAppleLocation))
    sf.blit(ls[0].image, transformLocationToCoordinate(ls[0].location))
    sf.blit(ls[1].image, transformLocationToCoordinate(ls[1].location))
    sf.blit(ls[2].image, transformLocationToCoordinate(ls[2].location))
    wd.blit(sf, (0, 0))
    pg.display.update()

setLocation = set()

gameStop = False
