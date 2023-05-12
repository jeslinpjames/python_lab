import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption('Tik Tac Toe')
clock = pygame.time.Clock()
game_active = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if game_active:
        screen.fill((0,153,153))
    pygame.display.update()
    clock.tick(60)