import sys

import pygame

class Pirate():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('practice/images/luffy.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    bg_color = (0,0,230)
    luffy = Pirate(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        luffy.blitme()
        pygame.display.flip()

run_game()