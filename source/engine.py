# Created by a human
# when:
# 11/23/2015
# 5:32 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import sys

import pygame


class Engine(object):
    # a generic state mach
    def __init__(self):
        self.currentState = State()
        self.states = []

    def run(self):
        self.states = [self.currentState]
        while self.states:
            self.currentState = self.states.pop()
            if self.currentState.paused:
                self.currentState.unpause()

            nextState, paused = self.currentState.mainloop()
            if self.currentState.killPrevious and self.states:
                self.states.pop()
            if paused:  # paused states are kept
                self.states.append(self.currentState)
            if nextState:
                self.states.append(nextState)

# generic parent class for a state
class State(object):
    def __init__(self):
        self.done = False
        self.nextState = None
        self.clock = pygame.time.Clock()
        self.paused = False
        self.killPrevious = False
        self.screen = pygame.display.get_surface()

    def reinit(self):
        pass

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False
        self.done = False
        self.nextState = None

    def main_start(self):
        pass

    def mainloop(self):
        self.main_start()
        while not self.done:
            self.check_events()
            self.check_collisions()
            self.update_screen()
            self.tick()
            pygame.event.pump()
        return self.nextState, self.paused

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.quit()

    def check_collisions(self):
        pass

    def update_screen(self):
        pass

    def tick(self):
        self.clock.tick(60)

    def quit(self):
        self.done = True
        self.screen.fill((0,0,0))
        return self.nextState, self.paused

    @staticmethod
    def closeGame():
        sys.exit(0)