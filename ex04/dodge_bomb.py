from pickle import TRUE
import pygame as pg
import sys
from random import randint


x,y=randint(0+10,1600-10),randint(0+10,900-10)

a,b=randint(0+10,1600-10),randint(0+10,900-10)


def main():
    pg.init()
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    #壁紙の設定      
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_sfc = pg.transform.rotozoom(bg_sfc,0,1)
    bg_rct = bg_sfc.get_rect()

    

    bakuhatsu_sfc = pg.image.load("fig/bakuhatsu.png")
    bakuhatsu_sfc = pg.transform.rotozoom(bakuhatsu_sfc,0,0.5)
    bakuhatsu_rct = bakuhatsu_sfc.get_rect()
    bakuhatsu_rct.center = x,y

    unchi_sfc = pg.image.load("fig/unchi.png")
    unchi_sfc = pg.transform.rotozoom(unchi_sfc,0,0.1)
    unchi_rct = unchi_sfc.get_rect()
    unchi_rct.center = a,b    
    
    draw_sfc = pg.Surface((20,20))
    draw_sfc.set_colorkey((0,0,0))
    pg.draw.circle(draw_sfc,(255,0,0),(10,10),10)
    draw_rct = draw_sfc.get_rect()
    draw_rct.center = x, y

    
    num = 0
    tori_sfc = pg.image.load(f"fig/{num}.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 800,450
    vx=5
    vy=5

    while(True):
        #こうかとんの設定
        
        

        scrn_sfc.blit(bg_sfc,bg_rct)
        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(draw_sfc,draw_rct)
        
        #爆弾の移動
        draw_rct.move_ip(+vx,+vy)
        if draw_rct.left<0 or draw_rct.right>1600:
            vx*=-1.05
        if draw_rct.top<0 or draw_rct.bottom>900:
            vy*=-1.05
        
        

        for event in pg.event.get():
            key_lst = pg.key.get_pressed()
            if event.type == pg.QUIT: return
            if event.type == pg.KEYDOWN:
                for num in range(10):
                    if num+48 == event.key:
                        tori_sfc = pg.image.load(f"fig/{num}.png")
                        tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
            
               
        if key_lst[pg.K_UP]==True:
            tori_rct.centery -= 5
        if key_lst[pg.K_DOWN]==True:
            tori_rct.centery += 5
        if key_lst[pg.K_RIGHT]==True:
            tori_rct.centerx += 5
        if key_lst[pg.K_LEFT]==True:
            tori_rct.centerx -= 5
        if key_lst[pg.K_u]==True:
            scrn_sfc.blit(unchi_sfc,tori_rct)
        
        #こうかとん画像変更
        
        
        if tori_rct.left<0:
            tori_rct.move_ip(+5,0)
        if tori_rct.right>1600:
            tori_rct.move_ip(-5,0)
        if tori_rct.top<0:
            tori_rct.move_ip(0,+5)
        if tori_rct.bottom>900:
            tori_rct.move_ip(0,-5)

        if tori_rct.colliderect(draw_rct):
            scrn_sfc.blit(bakuhatsu_sfc,tori_rct)

        
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
        
        

if __name__ == "__main__":
    main()

    