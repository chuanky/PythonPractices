import sys
import pygame
from pygame.sprite import Group,Sprite

class Rocket():
    def __init__(self, speed_factor, screen):
        self.screen = screen
        self.speed_factor = speed_factor
        self.image = pygame.image.load('practice/images/rockets_2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.position_y = float(self.rect.centery)
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.position_y += self.speed_factor
        
        if self.moving_up and self.rect.top > 0:
            self.position_y -= self.speed_factor
        
        self.rect.centery = self.position_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, screen, rocket):
        super().__init__()
        self.screen = screen
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centery = rocket.rect.centery
        self.rect.right = rocket.rect.right
        self.x = float(self.rect.x)
        self.color = self.bullet_color
    
    def update(self):
        self.x += self.bullet_speed_factor
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        

def check_events(screen, rocket, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
            elif event.key ==  pygame.K_SPACE:
                new_bullet = Bullet(screen, rocket)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    bg_color = (230,230,230)
    speed_factor = 1.5
    rocket = Rocket(speed_factor,screen)
    bullets = Group()

    while True:
        check_events(screen, rocket ,bullets)
        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        rocket.blitme()
        rocket.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        pygame.display.flip()

run_game()