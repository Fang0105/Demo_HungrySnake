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
    st.shouldGenerateNewApple = False
    st.listSnake.append(snake.SnakeHead((2,7), st.direction,0))
    st.listSnake.append(snake.SnakeBody((1, 7),1))
    st.listSnake.append(snake.SnakeBody((0, 7),2))
    for i in st.listSnake:
        frame.sf.blit(i.image,st.transformLocationToCoordinate(i.location))
        st.setLocation.add(i.location)
    apple.drawApple()
    frame.wd.blit(frame.sf, (0, 0))


pg.draw.rect(frame.sf, (255, 0, 0), st.rectTimeText)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectScoreText)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectRankText)
frame.sf.blit(st.txtLabelTime, st.txtLabelTime.get_rect(center=st.rectTimeText.center))
frame.sf.blit(st.txtLabelScore, st.txtLabelScore.get_rect(center=st.rectScoreText.center))
frame.sf.blit(st.txtLabelRank, st.txtLabelRank.get_rect(center=st.rectRankText.center))
frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)

st.drawScore(frame.sf,frame.wd)

init()
pg.display.update()

event.event()



