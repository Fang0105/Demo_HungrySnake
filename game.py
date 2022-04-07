import snake
import setting as st

listSnake = []

def init():
    listSnake.clear()
    listSnake.append(snake.SnakeHead(st.transformCoordinateTolocation(2, 7), st.direction))
    listSnake.append(snake.SnakeBody(st.transformCoordinateTolocation(0, 7)))
    listSnake.append(snake.SnakeBody(st.transformCoordinateTolocation(1, 7)))


