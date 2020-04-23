import pygame,sys
'''引用'''

class Settings():
    '''定义设置'''
    def __init__(self):
        self.width = 600
        self.height = 400
        self.bg_color = (0, 0, 0)
        self.fps = 300

class Balls():
    '''定义小球'''
    def __init__(self, name, ai_settings, screen, address, x, y):
        self.name = name
        self.screen = screen
        self.image = pygame.image.load(address)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [1,1]
        self.settings = ai_settings
        
    def check_side(self):
        self.rect = self.rect.move(self.speed[0],self.speed[1])
        if self.rect.left < 0 or self.rect.right > self.settings.width:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.settings.height:
            self.speed[1] = - self.speed[1]
        return self.speed
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

def check_events(balls):
    global number
    choosen_ball = balls[int(number%len(balls))]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                choosen_ball.speed[0] = choosen_ball.speed[0] if choosen_ball.speed[0] == 0 else (abs(choosen_ball.speed[0] - 1)) * int(choosen_ball.speed[0]/abs(choosen_ball.speed[0]))
            elif event.key == pygame.K_RIGHT:
                choosen_ball.speed[0] = choosen_ball.speed[0] + 1 if choosen_ball.speed[0] > 0 else choosen_ball.speed[0] - 1
            elif event.key == pygame.K_UP:
                choosen_ball.speed[1] = choosen_ball.speed[1] + 1 if choosen_ball.speed[1] > 0 else choosen_ball.speed[1]-1
            elif event.key == pygame.K_DOWN:
                choosen_ball.speed[1] = choosen_ball.speed[1] if choosen_ball.speed[1] == 0 else (abs(choosen_ball.speed[1] - 1)) * int(choosen_ball.speed[1]/abs(choosen_ball.speed[1]))
            elif event.key == pygame.K_TAB:
                number += 1
                print(choosen_ball.name)
                print(int(number/len(balls)))
                print(number)

def update_screen(ai_settings, balls):
    # 填充背景
    screen.fill(ai_settings.bg_color)
    # 画小球
    for ball in balls:
        ball.check_side()
        ball.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

# 初始化
pygame.init()
'''初始化部分'''
# 设置屏幕和抬头
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
pygame.display.set_caption('狗头壁球')
fclock = pygame.time.Clock()
# 创造球
ball1 = Balls('2jiang',ai_settings, screen, r'haoke\\pygamelesson\\images\\twojiang.png', 50, 50)
ball2 = Balls('hengha',ai_settings, screen, r'haoke\\pygamelesson\\images\\hengha.png', 550, 350)
balls = [ball1,ball2]
number = 0

while True:
# 开始循环
    check_events(balls)
    update_screen(ai_settings, balls)
    fclock.tick(ai_settings.fps)



