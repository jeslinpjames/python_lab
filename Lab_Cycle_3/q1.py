import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption('Tik Tac Toe')
clock = pygame.time.Clock()
game_active = True


o_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/O.png').convert_alpha()
o_image = pygame.transform.rotozoom(o_image,0,0.4)
x_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/X.png').convert_alpha()
x_image = pygame.transform.rotozoom(x_image,0,0.4)
o_rect = o_image.get_rect(center = (100,100))
x_rect = x_image.get_rect(center =(300,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if game_active:
        screen.fill((0,153,153))
        pygame.draw.line(screen,'Black',(200,20),(200,610),5)
        pygame.draw.line(screen,'Black',(400,20),(400,610),5)
        pygame.draw.line(screen,'Black',(10,210),(590,210),5)
        pygame.draw.line(screen,'Black',(10,410),(590,410),5)
        
        screen.blit(o_image,o_rect)
        x_rect = x_image.get_rect(center =(300,100))
        screen.blit(x_image,x_rect)
        x_rect = x_image.get_rect(center =(500,100))
        screen.blit(x_image,x_rect)
        o_rect = o_image.get_rect(center = (100,300))
        screen.blit(o_image,o_rect)
        x_rect = x_image.get_rect(center =(300,300))
        screen.blit(x_image,x_rect)
        o_rect = o_image.get_rect(center = (500,300))
        screen.blit(o_image,o_rect)
        x_rect = x_image.get_rect(center =(100,500))
        screen.blit(x_image,x_rect)
        o_rect = o_image.get_rect(center = (300,500))
        screen.blit(o_image,o_rect)
        x_rect = x_image.get_rect(center =(500,500))
        screen.blit(x_image,x_rect)



        # screen.blit(x_image,x_rect)


    pygame.display.update()
    clock.tick(60)