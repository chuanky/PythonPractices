import sys

from pygame.locals import *
import pygame
import pygame.draw

class Block():
    def __init__(self, screen, x, y, width=10, height=10):
        self.screen = screen
        self.rect = Rect(x - width / 2, y - height / 2, width, height)

    def biltme(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.rect)


class World():
    def __init__(self):
        self.blocks = {}

    def get_block_at(self, x, y):
        for block in self.blocks:
            in_x = x >= block.rect.left and x <= block.rect.right
            in_y = y >= block.rect.top and y <= block.rect.bottom
            if in_x and in_y:
                return block

    def get_blocks_at(self, x, y):
        result = []
        for block in self.blocks:
            in_x = x >= block.rect.left and x <= block.rect.right
            in_y = y >= block.rect.top and y <= block.rect.bottom
            if in_x and in_y:
                result.append(block)

        return result

class MouseController():
    def __init__(self, mouse):
        self.mouse = mouse
        self.origin = mouse.get_pos()
        self.is_moving = False

def main():
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('draw block')
    screen = pygame.display.set_mode((500, 500), 0, 32)

    m_mouse = MouseController(pygame.mouse)

    draw_mode = True
    clicking = False
    dragging = False

    world = World()
    block_width = 50
    block_height = 50

    curr_mouse_pos = (0, 0)

    while True:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        if draw_mode:
            follow_block = Block(screen, mx, my, block_width, block_height)
            follow_block.biltme()

        for b in world.blocks:
            b.biltme()

        if clicking:
            if curr_mouse_pos == pygame.mouse.get_pos():
                dragging = False
            else:
                dragging = True
                curr_mouse_pos = pygame.mouse.get_pos()

        if clicking and dragging:
            block = Block(screen, mx, my, block_width, block_height)
            world.blocks[block] = ''

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # 翻转draw_mode的值
                    draw_mode = not draw_mode

                if event.key == K_RETURN:
                    print(len(world.blocks))

            if event.type == MOUSEBUTTONDOWN:
                if draw_mode == False:
                    # focus_block = world.get_block_at(mx, my)
                    focus_blocks = world.get_blocks_at(mx, my)
                    # if focus_block:
                    #     world.blocks.pop(focus_block)
                    if len(focus_blocks) > 0:
                        for fb in focus_blocks:
                            world.blocks.pop(fb)
                
                if draw_mode == True:
                    clicking = True
                    curr_mouse_pos = pygame.mouse.get_pos()


            if event.type == MOUSEBUTTONUP:
                if draw_mode == True:
                    clicking = False

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)


main()

