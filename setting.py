import random

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

imageApple = pg.image.load('apple.png')
imageApple = pg.transform.scale(imageApple,(latticeSize,latticeSize))
imageAppleLocation = ""

imageSnakeHead = pg.image.load('snakeHead.png')
imageSnakeHead = pg.transform.scale(imageSnakeHead,(latticeSize,latticeSize))
imageSnakeBody = pg.image.load('snakeBody.png')
imageSnakeBody = pg.transform.scale(imageSnakeBody,(latticeSize,latticeSize))

