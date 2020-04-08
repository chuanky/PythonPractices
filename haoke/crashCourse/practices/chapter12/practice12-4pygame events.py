import sys

import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    bg_color = (230,230,230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        screen.fill(bg_color)
        pygame.display.flip()

run_game()