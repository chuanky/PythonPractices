import sys

import pygame

class Rockets():
    def __init__(self, speed_factor, screen):
        self.screen = screen
        self.speed_factor = speed_factor
        self.image = pygame.image.load('practice/images/rockets_1.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.position_x = float(self.rect.centerx)
        self.position_y = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position_x += self.speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.position_x -= self.speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.position_y += self.speed_factor
        
        if self.moving_up and self.rect.top > 0:
            self.position_y -= self.speed_factor
        
        self.rect.centerx = self.position_x
        self.rect.centery = self.position_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def check_events(rockets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rockets.moving_right = True
            elif event.key == pygame.K_LEFT:
                rockets.moving_left = True
            elif event.key == pygame.K_UP:
                rockets.moving_up = True
            elif event.key == pygame.K_DOWN:
                rockets.moving_down = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rockets.moving_right = False
            elif event.key == pygame.K_LEFT:
                rockets.moving_left = False
            elif event.key == pygame.K_UP:
                rockets.moving_up = False
            elif event.key == pygame.K_DOWN:
                rockets.moving_down = False

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    bg_color = (230,230,230)
    speed_factor = 1.5
    rockets = Rockets(speed_factor,screen)
    while True:
        check_events(rockets)
        screen.fill(bg_color)
        rockets.blitme()
        rockets.update()
        pygame.display.flip()

run_game()