import pygame
import random
from pygame import mixer
import math as m
pygame.init()
pygame.mixer.init()

#size of gaming window
size=(800,600)
game_window=pygame.display.set_mode(size)

#SETTING TITLE
pygame.display.set_caption("Soul Invader")

#SETTING ICON
icon=pygame.image.load('images/space_icon.png')
pygame.display.set_icon(icon)

#FPS
clock = pygame.time.Clock()

#FONT
font_score = pygame.font.SysFont("tlwgtypo", 30)

# COLORS
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue_grey = (204, 229, 255)
blue=( 93, 173, 226 )


#BACKGROUND IMAGE
back_ground_small=pygame.image.load('images/background.png')
back_ground = pygame.transform.scale(back_ground_small, (800, 600))

back_ground_small_low = pygame.image.load('images/background.png').convert()
back_ground_low = pygame.transform.scale(back_ground_small_low, (800, 600))
back_ground_low.set_alpha(100)


#TEXT INTRO
soulinvaderintro_small=pygame.image.load('images/soulinvadertitle.png')
soulinvaderintro = pygame.transform.scale(soulinvaderintro_small, (500, 220))

press_space_small=pygame.image.load('images/press_space.png')
press_space = pygame.transform.scale(press_space_small, (360, 220))

gameover_lg = pygame.image.load('images/gameover.png')
gameover = pygame.transform.scale(gameover_lg, (300, 220))

#BACKGROUND SOUND
mixer.music.load("sounds/background.wav")
mixer.music.play(-1)

#VARIABLES
running=True


#FUNCTION TO DISPLAY SCORE
def textscreen(heading,text,color, x, y):
    screen_text = font_score.render(f"{heading} : {str(text)}",True,color)
    game_window.blit(screen_text, [x, y])


# PLAYER FUNCTION
def player(player_img, x, y):
    game_window.blit(player_img, (x, y))


# game over
def game_over_text():
    game_window.fill(blue)
    game_window.blit(back_ground_low, (0, 0))
    game_window.blit(gameover, [260, 150])

    restarttext_lg = pygame.image.load('images/restarttext.png')
    restarttext = pygame.transform.scale(restarttext_lg, (470, 150))
    game_window.blit(restarttext, [160, 400])
    pygame.display.update()
    return


# ENEMY FUNCTION
def enemy(enemy_img, x, y):
    game_window.blit(enemy_img, (x, y))


# BULLET FUN
def bullet(bullet_img, x, y):
    global bulletstate
    bulletstate = 'fire'
    game_window.blit(bullet_img, (x + 16, y + 10))


# CHECK COLLISON B/W BULLET AND ENEMY
def checkcollison(enemyX,enemyY,bulletX,bulletY):
    distance=m.sqrt((m.pow((enemyX-bulletX),2))+(m.pow((enemyY-bulletY),2)))
    if distance<=26:
        return True
    else:
        return False


def menu():
    game_close = False
    enemy_img1 = pygame.image.load(f'images/alian1.png')
    enemy_img2 = pygame.image.load(f'images/alian2.png')
    enemyX1 = 370
    enemyY1 = 280
    enemyX2 = 500
    enemyY2 = 280

    enemyChangeX1 = 3
    enemyChangeY1 = 0
    enemyChangeX2 = 4
    enemyChangeY2 = 0

    while not game_close:
        game_window.fill(blue)
        game_window.blit(back_ground_low,(0,0))
        game_window.blit(soulinvaderintro, (180, 100))
        game_window.blit(press_space, (240, 330))

        enemyX1 += enemyChangeX1
        if enemyX1 <= 0:
            enemyChangeX1 = 5
            enemyY1 += enemyChangeY1
        elif enemyX1 >= 736:
            enemyChangeX1 = -5
            enemyY1 += enemyChangeY1

        enemyX2 += enemyChangeX2
        if enemyX2 <= 0:
            enemyChangeX2 = 5
            enemyY2 += enemyChangeY2
        elif enemyX2 >= 736:
            enemyChangeX2 = -5
            enemyY2 += enemyChangeY2

        enemy(enemy_img1, enemyX1, enemyY1)
        enemy(enemy_img2, enemyX2, enemyY2)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_close=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/button_press.mp3')
                    pygame.mixer.music.play()
                    gameplay()
        clock.tick(60)


def gameplay():
    # Player
    player_img = pygame.image.load('images/spaceship.png')

    # ENEMY
    enemy_img = []
    enemyX = []
    enemyY = []
    enemyChangeX = []
    enemyChangeY = []
    no_of_enemies = 6

    # BULLET
    bullet_img = pygame.image.load('images/bullet.png')

    # VARIABLES
    score_value = 0
    game_over=False
    exit_game = False

    # player
    playerX = 370
    playerY = 480
    playerChange = 0

    # BULLET
    bulletX = 0
    bulletY = 480
    bulletChangeX = 0
    bulletChangeY = 40
    bulletstate = 'ready'
    with open("highest.txt", "r") as f:
        high = f.read()

    game_window.fill(white)
    game_window.blit(back_ground, (0, 0))

    for i in range(1, no_of_enemies + 1):
        enemy_img.append(pygame.image.load(f'images/alian{i}.png'))
        enemyX.append(random.randint(0, 750))
        enemyY.append(random.randint(50, 150))
        enemyChangeX.append(4)
        enemyChangeY.append(40)



    while not exit_game:
        if game_over==True:
            if score_value>int(high):
                print("dsjsd")
                with open("highest.txt", "w") as f:
                    f.write(str(score_value))

            game_over_text()
            pygame.display.update()
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 gameover==True
                 exit_game = True
              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_RETURN:
                      pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/button_press.mp3')
                      pygame.mixer.music.play()
                      menu()
        else:

            game_window.fill((0, 0, 0))

            game_window.blit(back_ground,(0,0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    menu()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        playerChange = 19
                    if event.key==pygame.K_LEFT:
                        playerChange = -19
                    if event.key==pygame.K_SPACE:
                       if bulletstate=='ready':
                            bulletX=playerX
                            laserSound = mixer.Sound("sounds/laser.wav")
                            laserSound.play()
                            bulletstate="fire"
                            bullet(bullet_img,bulletX,bulletY)
                    if event.key==pygame.K_RETURN:
                        menu()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerChange = 0


            #PLAYER MOVEMENT
            playerX+=playerChange
            if playerX<0:
                playerX=0
            if playerX>736:
                playerX=736

            player(player_img,playerX,playerY)

            #ENEMY MOVEMENT
            for i in range(1, no_of_enemies ):

                # Game Over
                if enemyY[i] > 440:
                    for j in range(1,no_of_enemies):
                        enemyY[j] = 2000
                    pygame.mixer_music.load("sounds/gameover.mp3")
                    pygame.mixer_music.play()
                    game_over=True





                enemyX[i]+=enemyChangeX[i]
                if enemyX[i]<=0:
                    enemyChangeX[i]=5
                    enemyY[i]+=enemyChangeY[i]
                elif enemyX[i]>=736:
                    enemyChangeX[i]=-5
                    enemyY[i]+=enemyChangeY[i]



                #CHECK COLLISON
                collison=checkcollison(enemyX[i],enemyY[i],bulletX,bulletY)
                if collison:
                    explosionSound = mixer.Sound("sounds/explosion.wav")
                    explosionSound.play()
                    bulletY=480
                    bulletstate='ready'
                    score_value+=1
                    enemyX[i] = random.randint(0, 750)
                    enemyY[i] = random.randint(50, 150)
                enemy(enemy_img[i],enemyX[i], enemyY[i])

            # BULLET MOVEMENT
            if bulletY <= 0:
                bulletY = 480
                bulletstate = 'ready'

            if bulletstate is 'fire':
                bullet(bullet_img,bulletX, bulletY)
                bulletY -= bulletChangeY
            textscreen("Score",score_value,red,10,10)
            textscreen("Highest Score",high, red, 470, 10)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

menu()