import pygame
from bullet import Bullet

def check_keydown_events(event, ship, bullets, ai_settings, screen):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        bullets.add(Bullet(ai_settings, screen, ship))

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ship, m_settings, bullets, ai_settings, screen):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_settings.running = False
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, ai_settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(m_settings, screen, ship, bullets):
    '''让最近绘制的屏幕可见'''
    screen.fill(m_settings.bg_color)
    ship.blitme()
    for b in bullets:
        b.draw_bullet()
    pygame.display.flip()

