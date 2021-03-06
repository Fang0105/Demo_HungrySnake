import snake
import setting as st
import apple
import event
import pygame as pg
import frame
import rank
import pandas as pd

'''
繪製基本文字
開始一局遊戲
'''

pg.draw.rect(frame.sf, (255, 0, 0), st.rectTimeText)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectScoreText)
pg.draw.rect(frame.sf, (255, 0, 0), st.rectRankText)
frame.sf.blit(st.txtLabelTime, st.txtLabelTime.get_rect(center=st.rectTimeText.center))
frame.sf.blit(st.txtLabelScore, st.txtLabelScore.get_rect(center=st.rectScoreText.center))
frame.sf.blit(st.txtLabelRank, st.txtLabelRank.get_rect(center=st.rectRankText.center))
frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)

#開始一局新遊戲
def init():
    st.listSnake.clear()
    st.setLocation.clear()
    st.gameStop = False
    st.hasMoved = False
    st.shouldGenerateNewApple = False
    st.direction = "right"
    st.score = 0
    st.minute = 0
    st.second = 0
    st.listSnake.append(snake.SnakeHead((2,7), st.direction,0))
    st.listSnake.append(snake.SnakeBody((1, 7),1))
    st.listSnake.append(snake.SnakeBody((0, 7),2))
    frame.sf.blit(st.imageBackGround, st.imageBackGroundLocation)
    for i in st.listSnake:
        frame.sf.blit(i.image,st.transformLocationToCoordinate(i.location))
        st.setLocation.add(i.location)
    apple.drawApple()
    st.drawRank(frame.sf)
    frame.wd.blit(frame.sf, (0, 0))
    st.drawClock(frame.sf)
    st.drawScore(frame.sf,frame.wd)
    pg.display.update()
    pg.event.set_allowed(pg.KEYDOWN)
    rank.rank = {
        "score" : [],
        "time" : []
    }
    rank.df = pd.DataFrame(rank.rank)
    return event.event()


while init():
    pass
    


