import pygame
import sys
import time
import random

pygame.init()

# Définir les couleurs
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Définir la taille de l'écran
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Your Name')

# Définir la vitesse du serpent
snake_block = 10
snake_speed = 15

# Définir la police et la taille du texte
font_style = pygame.font.SysFont(None, 30)

# Fonction pour dessiner le serpent sur l'écran
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Fonction pour afficher le score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Fonction principale pour exécuter le jeu
def gameLoop():
    game_over = False
    game_close = False

    # Position initiale du serpent
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Changement initial de la position du serpent
    x1_change = 0
    y1_change = 0

    # Initialiser la longueur du serpent
    snake_List = []
    Length_of_snake = 1

    # Position initiale de la pomme
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Vérifier si le serpent atteint les bords de l'écran
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Mettre à jour la position du serpent
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)

        # Supprimer les éléments du serpent s'il est trop long
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Vérifier la collision avec soi-même
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Générer une nouvelle pomme si le serpent la mange
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Contrôler la vitesse du serpent
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
