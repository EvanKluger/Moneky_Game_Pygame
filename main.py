import random
import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crazy For Bananas')


SCORE_FONT = pygame.font.SysFont('comicsans', 40)
GAMEOVER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60


BANANA_IMAGE = pygame.image.load(os.path.join('assets', 'BANANA.png'))
TRASH_IMAGE = pygame.image.load(os.path.join('assets', 'TRASH.png'))
MONKEY_IMAGE = pygame.image.load(os.path.join('assets', 'MONKEY.png'))
JUNGLE_IMAGE = pygame.image.load(os.path.join('assets', 'JUNGLE.png'))


score_x = 700
score_y = 25
gameover_x = 160
gameover_y = 140

BANANA = pygame.transform.scale(BANANA_IMAGE, (80, 40))
BANANA_2 = pygame.transform.scale(BANANA_IMAGE, (80, 40))
BANANA_3 = pygame.transform.scale(BANANA_IMAGE, (80, 40))
TRASH = pygame.transform.scale(TRASH_IMAGE, (80, 40))
TRASH_2 = pygame.transform.scale(TRASH_IMAGE, (80, 40))
TRASH_3 = pygame.transform.scale(TRASH_IMAGE, (80, 40))
MONKEY = pygame.transform.scale(MONKEY_IMAGE, (120, 60))
JUNGLE = pygame.transform.scale(JUNGLE_IMAGE, (900, 500))

def random_coordinate_x():
    x = random.randint(50, 850)
    return x
def random_coordinate_y():
    y = random.randint(5, 495)
    return y


def monkey_movement(keys_pressed, monkey_box, MONKEY_VEL):
    if keys_pressed[pygame.K_LEFT] and monkey_box.x > 0:
        monkey_box.x -= MONKEY_VEL
    if keys_pressed[pygame.K_RIGHT] and monkey_box.x < WIDTH - monkey_box.width:
        monkey_box.x += MONKEY_VEL

def banana_movement(banana_box, BANANA_VEL):
    if banana_box.y < 500:
        banana_box.y = banana_box.y + BANANA_VEL
    else:
        banana_box.x = random_coordinate_x()
        banana_box.y = 0 

def banana_movement_2(banana_box_2, BANANA_VEL):
    if banana_box_2.y < 500:
        banana_box_2.y = banana_box_2.y + BANANA_VEL + 2
    else:
        banana_box_2.x = random_coordinate_x()
        banana_box_2.y = 0 

def banana_movement_3(banana_box_3, BANANA_VEL):
    if banana_box_3.y < 500:
        banana_box_3.y = banana_box_3.y + BANANA_VEL + 3
    else:
        banana_box_3.x = random_coordinate_x()
        banana_box_3.y = 0 

def trash_movement(trash_box, TRASH_VEL):
    if trash_box.y < 500:
        trash_box.y = trash_box.y + TRASH_VEL
    else:
        trash_box.x = random_coordinate_x()
        trash_box.y = 0

def trash_movement_2(trash_box_2, TRASH_VEL):
    if trash_box_2.y < 500:
        trash_box_2.y = trash_box_2.y + TRASH_VEL + 1
    else:
        trash_box_2.x = random_coordinate_x()
        trash_box_2.y = 0

def trash_movement_3(trash_box_3, TRASH_VEL):
    if trash_box_3.y < 500:
        trash_box_3.y = trash_box_3.y + TRASH_VEL + 2
    else:
        trash_box_3.x = random_coordinate_x()
        trash_box_3.y = 0

def draw_window(monkey_box, banana_box, trash_box, score_value, score_x, score_y, trash_box_2, banana_box_2, trash_box_3, banana_box_3, lost):
    WIN.fill((204, 255, 255))
    WIN.blit(JUNGLE, (0, 0))
    WIN.blit(MONKEY, (monkey_box.x, monkey_box.y))
    
    WIN.blit(BANANA, (banana_box.x, banana_box.y))
    WIN.blit(TRASH, (trash_box.x, trash_box.y))
    
    if score_value > 10:
        add_banana_2(banana_box_2)
        add_trash_2(trash_box_2)
    
    if score_value > 20:
        add_banana_3(banana_box_3)
        add_trash_3(trash_box_3)
    
    score = SCORE_FONT.render('Score : ' + str(score_value), True, (0,0,0))
    WIN.blit(score, (score_x,score_y))
    
    if lost == True:
        gameover = GAMEOVER_FONT.render('GAMEOVER', True, (0,0,0))
        WIN.blit(gameover, (gameover_x,gameover_y)) 
    
    pygame.display.update()

def add_trash_2(trash_box_2):
    WIN.blit(TRASH_2, (trash_box_2.x, trash_box_2.y))

def add_banana_2(banana_box_2):
    WIN.blit(BANANA_2, (banana_box_2.x, banana_box_2.y))

def add_trash_3(trash_box_3):
    WIN.blit(TRASH_3, (trash_box_3.x, trash_box_3.y))

def add_banana_3(banana_box_3):
    WIN.blit(BANANA_3, (banana_box_3.x, banana_box_3.y))

def main():
    MONKEY_VEL = 4
    BANANA_VEL = 3
    TRASH_VEL = 3
    lost = False
    score_value = 0
    count_items = 0
    count_monkey = 0
    monkey_box = pygame.Rect(450, 440, 120, 60)
    banana_box = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    trash_box = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    banana_box_2 = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    trash_box_2 = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    banana_box_3 = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    trash_box_3 = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    clock = pygame.time.Clock()
    run = True
    

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        keys_pressed = pygame.key.get_pressed()
        monkey_movement(keys_pressed, monkey_box, MONKEY_VEL)
        banana_movement(banana_box, BANANA_VEL)
        trash_movement(trash_box, TRASH_VEL)
        
        
        if score_value > 10:
            trash_movement_2(trash_box_2, TRASH_VEL)
            banana_movement_2(banana_box_2, BANANA_VEL)
        
        if score_value > 20:
            trash_movement_3(trash_box_3, TRASH_VEL)
            banana_movement_3(banana_box_3, BANANA_VEL)
        
        draw_window(monkey_box, banana_box, trash_box, score_value, score_x, score_y, trash_box_2, banana_box_2, trash_box_3, banana_box_3, lost)
        
        if count_monkey == 10:
            MONKEY_VEL += 1
            count_monkey = 0

        if count_items == 5:
            BANANA_VEL += 1
            TRASH_VEL += 1
            count_items = 0
        
        if monkey_box.colliderect(banana_box):
            score_value += 1
            count_items += 1
            count_monkey += 1
            banana_box.x = random_coordinate_x()
            banana_box.y = 0
        
        if monkey_box.colliderect(banana_box_2):
            score_value += 1
            count_items += 1
            count_monkey += 1
            banana_box_2.x = random_coordinate_x()
            banana_box_2.y = 0

        if monkey_box.colliderect(banana_box_3):
            score_value += 1
            count_items += 1
            count_monkey += 1
            banana_box_3.x = random_coordinate_x()
            banana_box_3.y = 0

        if monkey_box.colliderect(trash_box) or monkey_box.colliderect(trash_box_2) or monkey_box.colliderect(trash_box_3):
            lost = True 
            run = False

    pygame.quit()



if __name__ == '__main__':
    main()