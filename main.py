import random

import pygame

# Width and Height of snake and window
SNAKE_SQURE_DIAMENSION = 10
SNAKE_SPEED = 20
COLS = 60
ROW = 40

#Color settings
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (230, 94, 16)
COLOR_BLCK= (0,0,0)

#setting the width and height
WIDTH = COLS * SNAKE_SQURE_DIAMENSION
HEIGHT = ROW * SNAKE_SQURE_DIAMENSION

#initializing pygame
pygame.init()

#Displaying window
WIND = pygame.display.set_mode([WIDTH, HEIGHT])
#setting the caption and fonts
pygame.display.set_caption("SNAKE GAME")
font_style = pygame.font.SysFont("spendthrift", 30)

#for FPS
clock = pygame.time.Clock()

#x,y position for the snake movement
x1 = 30
y1 = 20

#draw a sing block function
def draw_block(snake_block, COLOR_BLUE):
    x_position = snake_block[0] * 10
    y_position = snake_block[1] * 10
    pygame.draw.rect(WIND, COLOR_BLUE, (x_position, y_position, SNAKE_SQURE_DIAMENSION, SNAKE_SQURE_DIAMENSION))

#draw the main snake
def long_snake(snake_list):
    for snake_block in snake_list:
        draw_block(snake_block, COLOR_BLUE)

#function for move the snake in the main window
def move_block(COLS, ROW, direction):
    if direction == "LEFT":
        COLS = COLS - 1
    if direction == "RIGHT":
        COLS = COLS + 1
    if direction == "UP":
        ROW = ROW - 1
    if direction == "DOWN":
        ROW = ROW + 1

    return [COLS, ROW]

#function for change the direction of the moving snake
def detect_direction(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction

#creating the target for the snake
def add_food():
    food_x = round(random.randrange(0, 59))
    food_y = round(random.randrange(0, 39))
    # Food_image_loading
    apple = pygame.image.load('apple.jpg')
    colr = WIND.blit(apple, [food_x,food_y])
    return [food_x,food_y,colr]

#function for quit the screen
def Quit_msg(msgs, COLOR_ORANGE):
    message = font_style.render(msgs, True, COLOR_ORANGE)
    WIND.blit(message, [WIDTH / 7.5, HEIGHT / 3])

#displying the current score
def score(scr):

    text = font_style.render("SCORE " + str(scr) , True ,COLOR_BLUE)
    WIND.blit(text ,[0,10])

#the main loop of the game
def game_loop():
    run = True
    game_close = False

    x1_change = 30
    y1_change = 20

    direction = "UP"
    snake_list = [[30, 23], [30, 22], [30, 21], [30, 20]]
    snake_length = 4

    food = add_food()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            direction = detect_direction(direction, event)

        if x1_change >= 60 or x1_change < 0 or y1_change >= 40 or y1_change < 0:
            run = False

        x1_change, y1_change = move_block(x1_change, y1_change, direction)

        #background_image_loading

        bg = pygame.image.load('background.jpg')
        WIND.blit(bg,[0,0])

        draw_block(food, COLOR_RED)
        snake_list.append([x1_change, y1_change])

        if (len(snake_list) >= snake_length):
            del snake_list[0]

        for pixel in snake_list[:-1]:
            if pixel == [x1_change,y1_change]:
                run = False


        long_snake(snake_list)

        score(snake_length - 4)
        pygame.display.update()

        if x1_change == food[0] and y1_change == food[1]:
            food = add_food()
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    while not game_close:
        # WIND.fill(COLOR_GREEN)
        Quit_msg("Please  P to Play again , or Q to  Quit", COLOR_ORANGE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.type == pygame.QUIT:
                    game_close = False
                    pygame.quit()
                elif event.key == pygame.K_p:
                    game_loop()

#calling the main function
game_loop()

#calling the quit finction to quit the incase loop quit doesn't work
pygame.quit()
