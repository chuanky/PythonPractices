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

def main():
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('draw block')
    screen = pygame.display.set_mode((500, 500), 0, 32)
    clicking = False

    world = World()
    block_width = 100
    block_height = 100

    while True:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        follow_block = Block(screen, mx, my, block_width, block_height)
        follow_block.biltme()

        for b in world.blocks:
            b.biltme()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                focus_block = world.get_block_at(mx, my)
                if focus_block:
                    world.blocks.pop(focus_block)
                else:
                    block = Block(screen, mx, my, block_width, block_height)
                    world.blocks[block] = ''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)


main()

