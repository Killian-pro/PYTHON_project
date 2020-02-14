#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cluzel.killian
#
# Created:     16/03/2016
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

import JEU_a_nous_suite

pygame.init()  #on lance pygame
os.environ['SDL_VIDEO_WINDOW_POS']="300,400"

fenetre=pygame.display.set_mode((1000,750))
pygame.display.set_caption("TIME OUT ")

fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))


fond1 = pygame.image.load("brosse1.jpg").convert_alpha()
fond1=pygame.transform.scale(fond1,(200,200))
fenetre.blit(fond1, (233,150))

fond2 = pygame.image.load("oeuf1.jpg").convert_alpha()
fond2=pygame.transform.scale(fond2,(200,200))
fenetre.blit(fond2, (466,150))


fond3 = pygame.image.load("metro1.jpg").convert_alpha()
fond3=pygame.transform.scale(fond3,(200,200))
fenetre.blit(fond3, (699,150))

fond4 = pygame.image.load("medi1.jpg").convert_alpha()
fond4=pygame.transform.scale(fond4,(200,200))
fenetre.blit(fond4, (233,400))



fond5 = pygame.image.load("pates1.jpg").convert_alpha()
fond5=pygame.transform.scale(fond5,(200,200))
fenetre.blit(fond5, (466,400))


fond6 = pygame.image.load("des.jpg").convert_alpha()
fond6=pygame.transform.scale(fond6,(200,200))
fenetre.blit(fond6, (699,400))

color_index = 0
COLORS=(fond1, fond2, fond3, fond4, fond5, fond6)


pygame.display.flip()
continuer=1
while (continuer==1):
        ev=pygame.event.poll()
        if ev.type==QUIT:
                continuer=0
        elif ev.type==MOUSEBUTTONUP:
                if ev.button==1:
                        if ev.pos[0]>=233 and ev.pos[0]<=433 and ev.pos[1]>=150 and ev.pos[1]<=350:
                                JEU_a_nous_suite.lancer_jeu(120)

                if ev.button==1:
                        if ev.pos[0]>=466 and ev.pos[0]<=666 and ev.pos[1]>=150 and ev.pos[1]<=350:
                                JEU_a_nous_suite.lancer_jeu(180)

                if ev.button==1:
                        if ev.pos[0]>=699 and ev.pos[0]<=899 and ev.pos[1]>=150 and ev.pos[1]<=350:
                                JEU_a_nous_suite.lancer_jeu(300)

                if ev.button==1:
                        if ev.pos[0]>=233 and ev.pos[0]<=433 and ev.pos[1]>=400 and ev.pos[1]<=600:
                                JEU_a_nous_suite.lancer_jeu(420)

                if ev.button==1:
                        if ev.pos[0]>=466 and ev.pos[0]<=666 and ev.pos[1]>=400 and ev.pos[1]<=600:
                                JEU_a_nous_suite.lancer_jeu(540)

                if ev.button==1:
                        if ev.pos[0]>=699 and ev.pos[0]<=899 and ev.pos[1]>=400 and ev.pos[1]<=600:
                                JEU_a_nous_suite.lancer_jeu(random.randint(5,540))
pygame.quit()
exit()
