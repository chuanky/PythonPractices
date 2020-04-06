import pygame

class Ship():
    def __init__(self,m_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.settings = m_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(m_settings.playerImgPath)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        '''TODO: 因为左右移动速度不一样'''
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)