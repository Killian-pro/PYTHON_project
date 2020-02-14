#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cluzel.killian
#
# Created:     23/03/2016
# Copyright:   (c) cluzel.killian 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import time
import pygame
import os
from sys import*
import traceback
from pygame.locals import * #on importe les constantes


def lancer_jeu(temps):
    surfacew = 950
    surfaceH = 360
    licorneW = 20
    licorneH = 20

    x=5
    y=5

    x_mur = surfacew-100
    y_mur = 0
    espace = licorneH
    mur_vitesse = 0.05

    os.environ['SDL_VIDEO_WINDOW_POS']="300,400"

    fenetre = pygame.display.set_mode((950,360))
    pygame.display.set_caption("Saute la licorne")
    from pygame.locals import * #on importe les constantes

    fond =pygame.image.load("paysage.jpg").convert()
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    lico= pygame.image.load("licorne.png").convert_alpha()
    lico=pygame.transform.scale(lico,(200,130))

    mur =pygame.image.load("mur.jpg")
    mur=pygame.transform.scale(mur,(100,100))

    font = pygame.font.Font(None, 36)
    #font=pygame.font.SysFont("broadway",24,bold=True,italic=False)
    #Text_timeend=font.render('TIMEEND',1,(0,0,0))

    temps_init=time.time()

    temps_vitesse_change = time.time()

    continuer=1
    fenetre.blit(lico,(x,y))
    pygame.display.flip()
    y_move = 10

    y_mur = random.randint(0,260)

    pygame.key.set_repeat(30, 30)

    while (continuer==1):
        ev=pygame.event.poll()
        if ev.type==QUIT:
            continuer=0
        elif ev.type==KEYDOWN:
            k=ev.key
            if k==K_DOWN:
                y=y+y_move
                if y>230:
                    y=230
            elif k==K_UP:
                y= y-y_move
                if y<0:
                    y = 0

        x_mur -= mur_vitesse


        if x_mur < -100:
            x_mur = surfacew-100
            y_mur = random.randint(0,260)

        if time.time()-temps_init>temps:
                #fais ce que tu veux avant de quitter
                #fenetre.blit(Text_timeend,(100,300))
                pygame.time.delay(2000)
                continuer=0



        if time.time()-temps_vitesse_change>10:
                mur_vitesse += 0.12
                temps_vitesse_change = time.time()



        fenetre.blit(fond, (0,0))
        fenetre.blit(mur, (x_mur, y_mur))
        fenetre.blit(lico,(x,y))


        if (x_mur<=200) and (x_mur >=-100) and (y>(y_mur-130)) and (y<(y_mur+100)):
            mur_vitesse = mur_vitesse - 1
            print "collision"




        #if pygame.font:
        #    font = pygame.font.Font(None, 36)
        text = font.render(str(temps-(time.time()-temps_init)), 1, (10, 10, 10))
        textpos = (900,0)
        fenetre.blit(text, textpos)

        pygame.display.flip()

    pygame.quit()
    exit()


