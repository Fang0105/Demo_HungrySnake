import setting as st
import abc
import apple
import snake
import pygame as pg
from pygame import *

class Snake:
    location = (None,None)
    image = None
    id = None
    formerLocation = None
    def __init__(self,location,id):
        self.location = location
        self.id = id
    @abc.abstractmethod
    def move(self):
        return NotImplemented

class SnakeHead(Snake):
    direction = None
    image = st.imageSnakeHead
    def __init__(self,location,direction,id):
        super().__init__(location,id)
        self.direction = direction
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
    def move(self):
        self.formerLocation = self.location
        #st.setLocation.remove(self.location)
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

class SnakeBody(Snake):
    image = st.imageSnakeBody
    def __init__(self,location,id):
        super().__init__(location,id)
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

def snakeMove():
    for i in st.listSnake:
        i.move()
    if st.shouldGenerateNewApple:
        eatApple()


def eatApple():
    st.setLocation.add(st.listSnake[len(st.listSnake) - 1].formerLocation)
    st.listSnake.append(snake.SnakeBody(st.listSnake[len(st.listSnake)-1].formerLocation,len(st.listSnake)))
    st.score += 1
    apple.generateNewApple()


