import pygame as pg
import sys
from random import randint


class Screen:
    def __init__(self,title,wh,bgimg):
        pg.display.set_caption(title) 
        self.sfc=pg.display.set_mode(wh) #(1600, 900)
        self.rct=self.sfc.get_rect()
        self.bgi_sfc=pg.image.load(bgimg)
        self.bgi_rct=self.bgi_sfc.get_rect()
        
        self.bgy = 0
        self.scroll_speed = 3
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc,(0,self.bgy))
        self.sfc.blit(self.bgi_sfc,(0,self.bgy - self.bgi_rct.height))

    def update(self):
        self.bgy = (self.bgy + self.scroll_speed) % self.bgi_rct.height

class Man:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,img,zoom,xy):
        self.sfc=pg.image.load(img)
        self.sfc=pg.transform.rotozoom(self.sfc,0,zoom)
        self.rct=self.sfc.get_rect()
        self.rct.center=xy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_states=pg.key.get_pressed()
        for key,delta in Man.key_delta.items():
            if key_states[key]:
                self.rct.centerx+=delta[0]
                self.rct.centery+=delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx-=delta[0]
                    self.rct.centery-=delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

class Ufos:
    def __init__(self,img,zoom,vxy,scr:Screen):
        self.sfc=pg.image.load(img) # 空のSurface
        self.sfc=pg.transform.rotozoom(self.sfc,0,zoom) # 2.0
        self.rct=self.sfc.get_rect()
        self.rct.centerx=50
        self.rct.centery=50
        self.vx, self.vy=vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko,tate=check_bound(self.rct,scr.rct)
        self.vx*=yoko
        self.vy*=tate
        if yoko == -1:
            self.rct.centery += 100

        self.blit(scr)


class Shot():
    def __init__(self,img,zoom,xy):
        self.sfc=pg.image.load(img)
        self.sfc=pg.transform.rotozoom(self.sfc,0,zoom)
        self.rct=self.sfc.get_rect()
        self.rct.center=xy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_states=pg.key.get_pressed()
        for key,delta in Man.key_delta.items():
            if key_states[key]:
                self.rct.centerx+=delta[0]
                self.rct.centery+=delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx-=delta[0]
                    self.rct.centery-=delta[1]
        self.rct.move_ip(0,-10)

        self.blit(scr)

def check_bound(obj_rct,scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def main():
    scr = Screen("シューティングゲーム", (800, 1000), "fig/unnamed.png")

    man = Man(f"fig/jet.png", 0.3, (400, 900))

    ufo = Ufos("fig/UFO.png", 0.1, (+1, 0), scr)

    a = False

    clock = pg.time.Clock()

    while True:
        scr.blit()
        scr.update()

        man.update(scr)

        ufo.update(scr)

        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                key_states = pg.key.get_pressed()
                if key_states[pg.K_SPACE] == True:
                    a = True
                    shot = Shot("fig/tama.png",0.2,man.rct.center)


        if a == True:
            shot.update(scr) 
            if shot.rct.colliderect(ufo.rct):
                ufo = Ufos("fig/UFO.png", 0.1, (+1, 0), scr)

        if man.rct.colliderect(ufo.rct):
            return

        

        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()