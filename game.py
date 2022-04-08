import snake
import setting as st
import apple
import event
import pygame as pg
import frame

listSnake = []

pg.draw.rect(frame.sf, (255, 0, 0), st.rectTime)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectScore)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectRank)
frame.sf.blit(st.txtTime, st.txtTime.get_rect(center=st.rectTime.center))
frame.sf.blit(st.txtScore, st.txtScore.get_rect(center=st.rectScore.center))
frame.sf.blit(st.txtRank, st.txtRank.get_rect(center=st.rectRank.center))
frame.wd.blit(frame.sf, (0, 0))

pg.display.update()

def init(sf,wd):
    listSnake.clear()
    st.setLocation.clear()
    apple.drawApple(sf, wd)
    listSnake.append(snake.SnakeHead((2,7), st.direction))
    listSnake.append(snake.SnakeBody((0, 7)))
    listSnake.append(snake.SnakeBody((1, 7)))
    for i in listSnake:
        st.setLocation.add(i.location)


init(frame.sf,frame.wd)

event.event(listSnake)



