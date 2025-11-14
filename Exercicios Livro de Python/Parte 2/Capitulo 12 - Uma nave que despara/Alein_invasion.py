import sys
import pygame
from settings import settings
from ship import ship

class alieninvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship(self)
        

    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.settings.bg_c)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    ai = alieninvasion()
    ai.rungame()