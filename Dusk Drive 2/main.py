import pygame
from pygame.locals import *
import sys
import random
from pygame import mixer

FPS=100
screen_width=494
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
game_sprites={}
game_sounds={}

def welcome_screen():

    msg_x=(screen_width-game_sprites['msg'].get_width())/2
    msg_y=(screen_height-game_sprites['msg'].get_height())/3
    car_x = (screen_width - game_sprites['car'].get_width())/2
    car_y = (screen_height - game_sprites['car'].get_height()-20)
    while(True):
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_RETURN:
                return
            else:
                screen.blit(game_sprites['background'],(0,0))
                screen.blit(game_sprites['strips'][0],(240,0))
                screen.blit(game_sprites['strips'][1],(111.5,0))
                screen.blit(game_sprites['strips'][1],(373,0))
                screen.blit(game_sprites['msg'], (msg_x, msg_y))
                screen.blit(game_sprites['car'], (car_x, car_y))
                pygame.display.update()

def random_obs():
    temp=random.randrange(0,4)
    obs_x = ((123.5 - game_sprites['obs'].get_width()) / 2) + (123.5 * temp)
    obs_y = -300
    obs={'x':obs_x,'y':obs_y, 'r':temp}
    return obs

def main_game():
    playbg()
    temp_ran=random.randrange(0,4)
    car_x = ((123.5- game_sprites['car'].get_width()) / 2) + (123.5*temp_ran)
    car_y = (screen_height - game_sprites['car'].get_height() - 20)
    obs1=random_obs()
    obs2=random_obs()
    # obs3=random_obs()

    obs=[
        {'x':obs1['x'],'y':obs1['y'],'r':obs1['r']},
        {'x':obs2['x'],'y':obs2['y']-(0.75*screen_height),'r':obs2['r']},
    ]

    obs_vel=10
    score=0
    strip_x=[111.5,240,373]
    strip_y=-50

    while (True):

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_RIGHT):
                if car_x < 350:
                    car_x += 123.5
                    temp_ran+=1
                    game_sounds['wing'].play()
            if event.type == KEYDOWN and (event.key == K_LEFT):
                if car_x > 100:
                    car_x -= 123.5
                    temp_ran -= 1
                    game_sounds['wing'].play()

        crashTest = isCollide(temp_ran,obs)
        if crashTest == True:
            playcrash()
            return

        for item in obs:
            item['y']+=obs_vel

        if 570<=obs[0]['y']<600:
            newobs=random_obs()
            obs.append(newobs)

        if (obs[0]['y']+game_sprites['obs'].get_height())>730:
            score+=1
            obs.pop(0)

        strip_y+=10
        if strip_y>=0:
            strip_y=-50

        screen.blit(game_sprites['background'],(0,0))
        screen.blit(game_sprites['strips'][0], (strip_x[0], strip_y))
        screen.blit(game_sprites['strips'][0], (strip_x[1], strip_y))
        screen.blit(game_sprites['strips'][0], (strip_x[2], strip_y))
        screen.blit(game_sprites['car'],(car_x,car_y))
        for item in obs:
            screen.blit(game_sprites['obs'],(item['x'],item['y']))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def playbg():
    mixer.music.load("sounds/bgmusic.mp3")
    mixer.music.play()
def playcrash():
    mixer.music.load("sounds/hit.mp3")
    mixer.music.play()

def isCollide(temp_ran,obs):
    for item in obs:
        if(item['r']==temp_ran and (item['y']+game_sprites['obs'].get_height())>=418 and item['y']<=680):
            return True
    return False

if __name__=="__main__":
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Dusk Drive")
    game_sprites['background']=pygame.image.load("sprites/background.png").convert_alpha()
    game_sprites['msg'] = pygame.image.load("sprites/msg.png").convert_alpha()
    game_sprites['car'] = pygame.image.load("sprites/car.png").convert_alpha()
    game_sprites['strips'] = (
        pygame.image.load("sprites/ystrip2.png").convert_alpha(),
        pygame.image.load("sprites/wstrip2.png").convert_alpha()
    )
    game_sprites['obs'] = (pygame.image.load("sprites/obs1.png").convert_alpha())
    game_sprites['numbers']=[
        pygame.image.load("sprites/0.png").convert_alpha,
        pygame.image.load("sprites/1.png").convert_alpha,
        pygame.image.load("sprites/2.png").convert_alpha,
        pygame.image.load("sprites/3.png").convert_alpha,
        pygame.image.load("sprites/4.png").convert_alpha,
        pygame.image.load("sprites/5.png").convert_alpha,
        pygame.image.load("sprites/6.png").convert_alpha,
        pygame.image.load("sprites/7.png").convert_alpha,
        pygame.image.load("sprites/8.png").convert_alpha,
        pygame.image.load("sprites/9.png").convert_alpha
    ]
    game_sounds['die']=pygame.mixer.Sound('sounds/die.wav')
    game_sounds['wing']=pygame.mixer.Sound('sounds/wing.wav')
    while(True):
        welcome_screen()
        main_game()
