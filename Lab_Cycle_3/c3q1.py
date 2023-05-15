import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tik Tac Toe')
clock = pygame.time.Clock()
game_active = True
player = 1
clicked = False
winner = 0
game_over =False
font = pygame.font.SysFont(None,90)

markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
image_cord = [[1, 1, 1], [3, 3, 3], [5, 5, 5]]


def draw_grid():
    screen.fill((0, 153, 153))
    pygame.draw.line(screen, 'Black', (200, 10), (200, 590), 5)
    pygame.draw.line(screen, 'Black', (400, 10), (400, 590), 5)
    pygame.draw.line(screen, 'Black', (10, 210), (590, 210), 5)
    pygame.draw.line(screen, 'Black', (10, 410), (590, 410), 5)


def draw_markers():
    o_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/O.png').convert_alpha()
    o_image = pygame.transform.rotozoom(o_image, 0, 0.4)
    x_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/X.png').convert_alpha()
    x_image = pygame.transform.rotozoom(x_image, 0, 0.4)
    x_width = x_image.get_width()
    x_height = x_image.get_height()
    o_width = o_image.get_width()
    o_height = o_image.get_height()

    for i in range(len(markers)):
        for j in range(len(markers[i])):
            marker = markers[i][j]

            if marker == 1:
                screen.blit(x_image, (image_cord[i][j] * 100 - x_width / 2, image_cord[j][i] * 100 - x_height / 2))

            if marker == -1:
                screen.blit(o_image, (image_cord[i][j] * 100 - o_width / 2, image_cord[j][i] * 100 - o_height / 2))

def check_winner():
    global winner
    global game_over
    y_pos = 0
    empty_cells = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over =  True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        if markers[0][0]+ markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] == 3:
            winner = 1
            game_over = True
        if markers[0][0]+ markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
            winner = 2
            game_over = True
        y_pos += 1
        
        empty_cells +=x.count(0)


    if empty_cells == 0 and winner == 0:
        winner = -1
        game_over = True


def display_winner():
    o_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/O.png').convert_alpha()
    o_image = pygame.transform.rotozoom(o_image, 0, 0.8)
    x_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/X.png').convert_alpha()
    x_image = pygame.transform.rotozoom(x_image, 0, 0.8)   
    txt= font.render("WON",True,'Black')
    if winner == 1:
        x_rect = x_image.get_rect(center = (300,200))
        screen.blit(x_image,x_rect)
        screen.blit(txt,(220,370))
    if winner == -1:
        x_image = pygame.transform.rotozoom(x_image, 0, 0.6) 
        o_image = pygame.transform.rotozoom(o_image, 0, 0.6)
        x_rect = x_image.get_rect(center = (150,220))
        o_rect = o_image.get_rect(center = (450,220))
        screen.blit(x_image,x_rect)
        screen.blit(o_image,o_rect)
        txt= font.render("DRAW",True,'Black')
        screen.blit(txt,(220,370))
    if winner == 2:
        o_rect = o_image.get_rect(center = (290,200))
        screen.blit(o_image,o_rect)
        screen.blit(txt,(220,370))


def clear_marker():
    global markers
    markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


mouse_index=(0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                cell_x =mouse_pos[0]
                cell_y = mouse_pos[1]
                if markers[cell_x//200][cell_y//200] == 0:
                    markers[cell_x//200][cell_y//200] = player
                    player *= -1
                    check_winner()

        if game_over == True:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 350 and 450 <= mouse_pos[1] <= 550:
                    game_over = False
                    player = 1
                    clear_marker()
                    winner = 0
        

  

    if game_over == False:
        draw_grid()
        draw_markers()
    if game_over == True:
        screen.fill((0, 153, 153))        
        display_winner()
        again_text = font.render("Restart?", True, (255, 255, 255))
        screen.blit(again_text, (200, 470))
        
          



    pygame.display.update()
    clock.tick(60)
