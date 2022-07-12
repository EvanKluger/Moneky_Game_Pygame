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
MONKEY_VEL = 4
BANANA_VEL = 3
TRASH_VEL = 3

BANANA_IMAGE = pygame.image.load(os.path.join('assets', 'BANANA.png'))
TRASH_IMAGE = pygame.image.load(os.path.join('assets', 'TRASH.png'))
MONKEY_IMAGE = pygame.image.load(os.path.join('assets', 'MONKEY.png'))
JUNGLE_IMAGE = pygame.image.load(os.path.join('assets', 'JUNGLE.png'))


score_x = 700
score_y = 25
gameover_x = 450
gameover_y = 250

BANANA = pygame.transform.scale(BANANA_IMAGE, (80, 40))
TRASH = pygame.transform.scale(TRASH_IMAGE, (80, 40))
MONKEY = pygame.transform.scale(MONKEY_IMAGE, (120, 60))
JUNGLE = pygame.transform.scale(JUNGLE_IMAGE, (900, 500))

def random_coordinate_x():
    x = random.randint(5, 895)
    return x
def random_coordinate_y():
    y = random.randint(5, 495)
    return y


def monkey_movement(keys_pressed, monkey_box):
    if keys_pressed[pygame.K_LEFT] and monkey_box.x > 0:
        monkey_box.x -= MONKEY_VEL
    if keys_pressed[pygame.K_RIGHT] and monkey_box.x < WIDTH - monkey_box.width:
        monkey_box.x += MONKEY_VEL

def banana_movement(banana_box):
    if banana_box.y < 500:
        banana_box.y = banana_box.y + BANANA_VEL
    else:
        banana_box.x = random_coordinate_x()
        banana_box.y = 0 

def trash_movement(trash_box):
    if trash_box.y < 500:
        trash_box.y = trash_box.y + TRASH_VEL
    else:
        trash_box.x = random_coordinate_x()
        trash_box.y = 0

def draw_window(monkey_box, banana_box, trash_box, score_value, score_x, score_y):
    WIN.fill((204, 255, 255))
    WIN.blit(JUNGLE, (0, 0))
    WIN.blit(MONKEY, (monkey_box.x, monkey_box.y))
    
    WIN.blit(BANANA, (banana_box.x, banana_box.y))
    WIN.blit(TRASH, (trash_box.x, trash_box.y))
    
    score = SCORE_FONT.render('Score : ' + str(score_value), True, (0,0,0))
    WIN.blit(score, (score_x,score_y))

    pygame.display.update()


def main():
    
    score_value = 0
    count = 0
    monkey_box = pygame.Rect(450, 440, 120, 60)
    banana_box = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    trash_box = pygame.Rect(random_coordinate_x(), 0, 80, 40)
    clock = pygame.time.Clock()
    run = True
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        monkey_movement(keys_pressed, monkey_box)
        banana_movement(banana_box)
        trash_movement(trash_box)

        

        draw_window(monkey_box, banana_box, trash_box, score_value, score_x, score_y)
        

        if monkey_box.colliderect(banana_box):
            score_value += 1
            count += 1
            banana_box.x = random_coordinate_x()
            banana_box.y = 0

        if monkey_box.colliderect(trash_box):
            gameover = GAMEOVER_FONT.render('GAMEOVER', True, (0,0,0))
            WIN.blit(gameover, (gameover_x,gameover_y))
            
            run = False
        
        


    pygame.quit()



if __name__ == '__main__':
    main()