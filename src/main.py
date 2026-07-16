import pygame as pg 
from sys import exit 
import random 

pg.init()

screen = pg.display.set_mode([800, 400])
title = pg.display.set_caption('bounce the ball')
clock = pg.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
Xpos1 = 400
Xpos2 = 450
Xpos3 = 350
Ypos1 = 200
Ypos2 = 200
Ypos3 = 200
background = pg.image.load('player.png')
background = pg.transform.scale(background, (800, 400))
player = pg.image.load('background.png')
player = pg.transform.scale(player, (50, 50))
playerX = 375
playerY = 350
font = pg.font.Font(None, 36)
score = 0

def update_score():
    global surface1 
    surface1 = font.render(f'Score: {score}', True, white)

update_score()

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()

        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                playerX -= 20  
                print("Left arrow key pressed")

            elif i.key == pg.K_RIGHT:
                playerX += 20
                print("Right arrow key pressed")

    screen.blit(background, (0, 0))
    screen.blit(player, (playerX, playerY))

    Ypos1 += 1
    Ypos2 += 1
    Ypos3 += 1

    circle1 = pg.draw.circle(screen, white, (Xpos1, Ypos1), 20, 0) 
    circle2 = pg.draw.circle(screen, white, (Xpos2, Ypos2), 20, 0)
    circle3 = pg.draw.circle(screen, white, (Xpos3, Ypos3), 20, 0)

    if Ypos1 >= 430 or Ypos2 >= 430 or Ypos3 >= 430:
        print("collision")
        print("game over")
        print(score)
        pg.quit()
        exit()

    if (Ypos1 + 20 >= playerY and Ypos1 - 20 <= playerY + 50) and (Xpos1 + 20 >= playerX and Xpos1 - 20 <= playerX + 50):  
        Ypos1 = random.randint(190, 200)
        Xpos1 = random.randint(200, 450)
        print("Circle 1 collision with player")
        score += 1 
        update_score()  

    if (Ypos2 + 20 >= playerY and Ypos2 - 20 <= playerY + 50) and (Xpos2 + 20 >= playerX and Xpos2 - 20 <= playerX + 50):  
        Ypos2 = random.randint(190, 200)
        Xpos2 = random.randint(200, 400)
        print("Circle 2 collision with player")
        score += 1
        update_score()  

    if (Ypos3 + 20 >= playerY and Ypos3 - 20 <= playerY + 50) and (Xpos3 + 20 >= playerX and Xpos3 - 20 <= playerX + 50):  
        Ypos3 = random.randint(190, 200)
        Xpos3 = random.randint(200, 400)
        print("Circle 3 collision with player")
        score += 1 
        update_score()  
                                
    screen.blit(surface1, (10, 10))
    
    pg.display.update()
    clock.tick(60)
