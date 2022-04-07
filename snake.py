import setting as st

class Snake:
    location = (None,None)
    image = None
    def __init__(self,location):
        self.location = location

class SnakeHead(Snake):
    direction = None
    image = st.imageSnakeHead
    def __init__(self,location,direction):
        super().__init__(location)
        self.direction = direction

class SnakeBody(Snake):
    image = st.imageSnakeBody
    def __init__(self,location):
        super().__init__(location)