# Created by a human
# when:
# 11/23/2015
# 5:43 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame

def setActorRect(actor,w,h,x=0,y=0):
    actor.rect = pygame.Rect(x,y,w,h)

def actorBlankImage(actor,width,height):
    actor.image = pygame.Surface((width,height))

def fillBlankImage(actor, r,g,b):
    actor.image.fill((r,g,b))

def putOnScreen(actor,screen):

    screen.blit(actor.image, actor.rect)

class Actor(pygame.sprite.Sprite):
    def __init__(self, color=0):
        pygame.sprite.Sprite.__init__(self)
        setActorRect(self,16,16)
        actorBlankImage(self,16,16)
        if color == 0: # used as 'floor' color
            fillBlankImage(self,120,120,120)
        if color == 1: # darken unreachable areas
            fillBlankImage(self,30,35,32)
        if color == 2: # walls
            fillBlankImage(self,80,80,240)
        if color == 3: # doors
            fillBlankImage(self,50,50,50)
        if color == 4:
            fillBlankImage(self,80,240,80)
        if color == 5:
            fillBlankImage(self,240,80,80)

    def topLeft(self):
        return self.rect.topleft

    def setPosition(self,x,y):

        self.rect.topleft = (x,y)
