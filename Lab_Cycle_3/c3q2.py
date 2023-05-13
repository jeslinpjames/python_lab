import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tik Tac Toe')
clock = pygame.time.Clock()
game_active = True
player = 1
clicked = False

markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
image_cord = [[1, 1, 1], [3, 3, 3], [5, 5, 5]]


def draw_grid():
    screen.fill((0, 153, 153))
    pygame.draw.line(screen, 'Black', (200, 20), (200, 610), 5)
    pygame.draw.line(screen, 'Black', (400, 20), (400, 610), 5)
    pygame.draw.line(screen, 'Black', (10, 210), (590, 210), 5)
    pygame.draw.line(screen, 'Black', (10, 410), (590, 410), 5)


def draw_markers():
    """Draws the X and O markers on the screen.

    Args:
        markers: A list of lists of integers, where each integer represents the marker at a given position.
        image_cord: A list of lists of integers, where each integer represents the coordinates of an image at a given position.
    """

    # Load the X and O images.
    o_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/O.png').convert_alpha()
    o_image = pygame.transform.rotozoom(o_image, 0, 0.4)
    x_image = pygame.image.load('D:/git/PYTHON_LAB/Lab_Cycle_3/X.png').convert_alpha()
    x_image = pygame.transform.rotozoom(x_image, 0, 0.4)
    # Get the width and height of the images.
    x_width = x_image.get_width()
    x_height = x_image.get_height()
    o_width = o_image.get_width()
    o_height = o_image.get_height()

    # Loop over the markers.
    for i in range(len(markers)):
        for j in range(len(markers[i])):
            # Get the marker at the current position.
            marker = markers[i][j]

            # If the marker is X, draw the X image.
            if marker == 1:
                # Draw the X image at the specified coordinates.
                screen.blit(x_image, (image_cord[i][j] * 100 - x_width / 2, image_cord[j][i] * 100 - x_height / 2))

            # If the marker is O, draw the O image.
            if marker == -1:
                # Draw the O image at the specified coordinates.
                screen.blit(o_image, (image_cord[i][j] * 100 - o_width / 2, image_cord[j][i] * 100 - o_height / 2))










mouse_index=(0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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


  


    draw_grid()
    draw_markers()
    # print(markers)
        
          



    pygame.display.update()
    clock.tick(60)
