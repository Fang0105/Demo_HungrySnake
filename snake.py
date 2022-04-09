import setting as st
import abc
import apple

class Snake:
    location = (None,None)
    image = None
    def __init__(self,location):
        self.location = location

    @abc.abstractmethod
    def move(self):
        return NotImplemented

class SnakeHead(Snake):
    direction = None
    image = st.imageSnakeHead
    def __init__(self,location,direction):
        super().__init__(location)
        self.direction = direction
    def isCollision(self):
       global boolIsCollision
       boolIsCollision = None
       if self.location[0]>15 or self.location[1]>15 or self.location[0]<0 or self.location[1]<0:
           boolIsCollision = True
       else:
           if self.location in st.setLocation:
               if self.location == st.imageAppleLocation:
                   apple.generateNewApple()
                   boolIsCollision =  False
               else:
                   print("hit body")
                   boolIsCollision =  True
           else:
               boolIsCollision = False
       if boolIsCollision == False:
           return boolIsCollision
       else:
           st.gameStop = True
           return boolIsCollision
    def move(self):
        tmp = self.location
        st.setLocation.remove(tmp)
        if self.direction == "right":
            self.location = (self.location[0]+1,self.location[1])
        elif self.direction == "left":
            self.location = (self.location[0]-1,self.location[1])
        elif self.direction == "up":
            self.location = (self.location[0],self.location[1]-1)
        elif self.direction == "down":
            self.location = (self.location[0],self.location[1]+1)
        if self.isCollision():
            print("gameStop : ",end="")
            print(st.gameStop)
            self.location = tmp
        else:
            st.setLocation.add(self.location)
class SnakeBody(Snake):
    image = st.imageSnakeBody
    def __init__(self,location):
        super().__init__(location)
    def move(self):
        pass
