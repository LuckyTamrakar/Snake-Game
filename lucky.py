
import pygame
import random
import os

pygame.mixer.init()

pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
img = pygame.image.load("snake.jpg")
img = pygame.transform.scale(img , (900, 600)).convert_alpha()
imag = pygame.image.load("snake1.png")
imag = pygame.transform.scale(imag , (900, 600)).convert_alpha()

pygame.display.set_caption("Lucky Ko Saap")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(imag, (0, 0))
        text_screen("Lucky Ke Saapo Me Aapka Swagat Hae", red, 220, 530)
        text_screen("Chodo joh bhi hoo sbse bdo Balo Button Dabao Aur Saap ko Khana Khilao", red, 5, 570)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)



def gameloop():
    
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if "highscore.txt" :
        with open("hiscore.txt", "w") as f:
            hiscore = f.write("0")
    else:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 3
    snake_size = 15
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(img, (0, 0))
            
            text_screen("Mardao Tumne Hamae Saap ko Enter Dabake kro aab Zinda", red, 90, 230)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(img, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: "+str(hiscore), red, 5, 570)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameKhatam.mp3')
                pygame.mixer.music.play()
                gameWindow.blit(img, (0, 0))

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gamekhatam.mp3')
                pygame.mixer.music.play()
                
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

