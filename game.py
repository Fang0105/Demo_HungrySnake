import snake
import setting as st
import apple
import event
import pygame as pg
import frame

def init():
    st.listSnake.clear()
    st.setLocation.clear()
    st.gameStop = False
    st.hasMoved = False
    st.listSnake.append(snake.SnakeHead((2,7), st.direction))
    st.listSnake.append(snake.SnakeBody((1, 7)))
    st.listSnake.append(snake.SnakeBody((0, 7)))
    for i in st.listSnake:
        frame.sf.blit(i.image,st.transformLocationToCoordinate(i.location))
        st.setLocation.add(i.location)
    apple.drawApple()
    frame.wd.blit(frame.sf, (0, 0))


pg.draw.rect(frame.sf, (255, 0, 0), st.rectTime)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectScore)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectRank)
frame.sf.blit(st.txtTime, st.txtTime.get_rect(center=st.rectTime.center))
frame.sf.blit(st.txtScore, st.txtScore.get_rect(center=st.rectScore.center))
frame.sf.blit(st.txtRank, st.txtRank.get_rect(center=st.rectRank.center))
frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)

init()
pg.display.update()

event.event()



