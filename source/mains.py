# Created by a human
# when:
# 11/23/2015
# 5:31 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from gameState import *
from engine import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (120,20)

def main():
    windowWidth = 1000
    windowHeight = 704
    display = (windowWidth, windowHeight)
    pygame.init()
    pygame.display.set_mode(display)
    pygame.display.set_caption("look out, people!")
    e = Engine()
    e.currentState = Game()
    e.run()
