import pygame as pg
import setting as st

'''
繪製"是否重來一局"的surface
'''

global rectYes
rectYes = pg.Rect(37.5,120.78125,50,50)
global rectNo
rectNo = pg.Rect(162.5,120.78125,50,50)

#繪製"是否重來一局"的surface
def renew(win):
    regameSf = pg.Surface(st.newSurfaceSize)
    regameSf.fill((255,255,255))
    fontMessage = pg.font.Font(None,25)
    strMessage = ""
    if win:
        strMessage = "WIN!!!"
    else:
        strMessage = "LOSE..."
    txtMessage = fontMessage.render(strMessage,True,(0,0,0))
    regameSf.blit(txtMessage,(100,10))
    regameSf.blit(fontMessage.render("One more game?",True,(0,0,0)),(50,50))
    fontYesAndNo = pg.font.Font(None,25)
    txtYes = fontYesAndNo.render("Yes",True,(0,0,0))
    pg.draw.rect(regameSf,(255,0,0),rectYes)
    txtNo = fontYesAndNo.render("No",True,(0,0,0))
    pg.draw.rect(regameSf,(255,0,0),rectNo)
    regameSf.blit(txtYes,txtYes.get_rect(center=rectYes.center))
    regameSf.blit(txtNo,txtNo.get_rect(center=rectNo.center))
    return regameSf

