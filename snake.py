import setting as st
import abc
import apple
import snake
import pygame as pg
from pygame import *

'''
定義snake的class
實作有關蛇移動的相關方法
'''

#定義snake的class
class Snake:
    location = (None,None)
    image = None
    id = None
    formerLocation = None
    def __init__(self,location,id):
        self.location = location
        self.id = id

    #蛇移動的方法(虛擬)
    @abc.abstractmethod
    def move(self):
        return NotImplemented

#定義snakehead的class繼承snake
class SnakeHead(Snake):
    direction = None
    image = st.imageSnakeHead
    def __init__(self,location,direction,id):
        super().__init__(location,id)
        self.direction = direction
    
    #判斷蛇頭是否碰撞自己身體或是邊界
    def isCollision(self):
       global boolIsCollision
       boolIsCollision = None
       if self.location[0]>15 or self.location[1]>15 or self.location[0]<0 or self.location[1]<0:
           boolIsCollision = True
       else:
           if self.location in st.setLocation:
               if self.location == st.imageAppleLocation:
                   st.shouldGenerateNewApple = True
                   boolIsCollision = False
               else:
                   boolIsCollision =  True
           else:
               boolIsCollision = False
       if boolIsCollision == False:
           return boolIsCollision
       else:
           st.gameStop = True
           pg.event.set_blocked(KEYDOWN)
           return boolIsCollision

    #實作蛇頭的移動
    def move(self):
        self.formerLocation = self.location
        if self.direction == "right":
            self.location = (self.location[0]+1,self.location[1])
        elif self.direction == "left":
            self.location = (self.location[0]-1,self.location[1])
        elif self.direction == "up":
            self.location = (self.location[0],self.location[1]-1)
        elif self.direction == "down":
            self.location = (self.location[0],self.location[1]+1)
        if self.isCollision():
            self.location = self.formerLocation
        else:
            st.setLocation.add(self.location)

#定義snakebody的class繼承snake
class SnakeBody(Snake):
    image = st.imageSnakeBody
    def __init__(self,location,id):
        super().__init__(location,id)
    
    #實作snakebody的移動
    def move(self):
        if st.gameStop:
            pass
        else:
            self.formerLocation = self.location
            #st.setLocation.remove(self.location)
            if self.id == len(st.listSnake)-1:
                st.setLocation.remove(self.location)
            self.location = st.listSnake[self.id-1].formerLocation
            st.setLocation.add(self.location)

#整條蛇的移動
def snakeMove():
    for i in st.listSnake:
        i.move()
    if st.shouldGenerateNewApple:
        eatApple()

#吃掉蘋果的方法
def eatApple():
    st.setLocation.add(st.listSnake[len(st.listSnake) - 1].formerLocation)
    st.listSnake.append(snake.SnakeBody(st.listSnake[len(st.listSnake)-1].formerLocation,len(st.listSnake)))
    st.score += 1
    apple.generateNewApple()


