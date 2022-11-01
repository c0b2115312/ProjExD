from symbol import test_nocond
import pygame as pg
import sys
from random import randint

#背景の設定
class Screen:
    def __init__(self,title,wh,bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc=pg.display.set_mode(wh) #(1600, 900)
        self.rct=self.sfc.get_rect()
        self.bgi_sfc=pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct=self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)

#鳥の設定
class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,img,zoom,xy):
        sfc=pg.image.load(img) # "fig/6.png"
        self.sfc=pg.transform.rotozoom(sfc,0,zoom) # 2.0
        self.rct=self.sfc.get_rect()
        self.rct.center=xy # 900, 400

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_states=pg.key.get_pressed()
        for key,delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx+=delta[0]
                self.rct.centery+=delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx-=delta[0]
                    self.rct.centery-=delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

#爆弾の設定
class Bomb:
    def __init__(self,img,zoom,vxy,scr:Screen):
        self.sfc=pg.image.load(img) # 空のSurface
        self.sfc.set_colorkey((255,255,255)) # 四隅の黒い部分を透過させる
        self.sfc=pg.transform.rotozoom(self.sfc,0,zoom) # 2.0
        self.rct=self.sfc.get_rect()
        self.rct.centerx=randint(0, scr.rct.width)
        self.rct.centery=randint(0, scr.rct.height)
        self.vx, self.vy=vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko,tate=check_bound(self.rct,scr.rct)
        self.vx*=yoko
        self.vy*=tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

#天使の設定
class Angel:
    def __init__(self,img,zoom,scr:Screen):
        sfc=pg.image.load(img) 
        self.sfc=pg.transform.rotozoom(sfc,0,zoom) # 2.0
        self.rct=self.sfc.get_rect()
        self.rct.centerx=randint(0,scr.rct.width)
        self.rct.centery=randint(0,scr.rct.height)

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen):
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
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    num=0
    kkt = Bird(f"fig/{num}.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb("fig/akuma.jpg", 0.5, (+1, +1), scr)

    clock = pg.time.Clock() # 練習1

    a = False

    ang = ""

    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                for num in range(10):
                    if num+48 == event.key:
                        kkt = Bird(f"fig/{num}.png",2.0,kkt.rct.center)#こうかとんの設定
            if event.type == pg.KEYDOWN:
                key_states = pg.key.get_pressed()
                if key_states[pg.K_SPACE] == True:
                    a = True
                    ang = Angel("fig/tensi.png",0.1,scr)
        
        if a==True:
            ang.update(scr)
                    
        # 練習4
        kkt.update(scr)

        # 練習7
        bkd.update(scr)

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()