# Created by a human
# when:
# 11/23/2015
# 5:33 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from engine import *
from mapGen import *
from actors import *

class Game(State):
    def __init__(self):
        State.__init__(self)
        self.world = LevelMap()
        mw = 63
        mh = 44
        f = 1000
        c = 100
        r = 100
        self.world.generateMap(mw,mh,f,c,r)
        self.screen = pygame.display.get_surface()
        self.background = pygame.Surface((1000, 1000))
        self.background.fill((255,220,0))
        self.mapList = []

        for y in range(mh):
            for x in range(mw):
                if self.world.mapArray[y][x] == 0:
                    a = Actor(color=0)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)
                if self.world.mapArray[y][x] == 1:
                    a = Actor(color=1)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)
                if self.world.mapArray[y][x] == 2:
                    a = Actor(color=2)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)
                if self.world.mapArray[y][x]== 3:
                    a = Actor(color=3)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)
                if self.world.mapArray[y][x] == 4:
                    a = Actor(color=4)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)
                if self.world.mapArray[y][x] == 5:
                    a = Actor(color=5)
                    a.setPosition(x*16,y*16)
                    self.mapList.append(a)


    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.quit()

    def check_collisions(self):
        pass

    def update_screen(self):
        self.screen.blit(self.background, self.background.get_rect())
        for m in self.mapList:
            self.screen.blit(m.image, m.rect)
        pygame.display.flip()