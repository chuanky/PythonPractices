import pygame
import pygame.display
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    # 载入设置信息
    m_settings = Settings()
    screen = pygame.display.set_mode((m_settings.screen_width, m_settings.screen_height))
    pygame.display.set_caption(m_settings.caption)
    # 建立一个飞船对象
    ship = Ship(m_settings, screen)
    bullets = Group()
    # 开始游戏的主循环
    while m_settings.running:
        gf.check_event(ship, m_settings, bullets, m_settings, screen)
        ship.update()
        bullets.update()
        gf.update_screen(m_settings, screen, ship, bullets)


run_game()
