import pygame
import pygame.locals

# screen design
screen=pygame.display.set_mode((480, 800), 0, 32)
# load background
bk=pygame.image.load(r"C:/Users/kzhu/Documents/Learn Code/My WEBSITE/git_first_try/newGitTest1/F-War/images/background.png")
# load plane
plane=pygame.image.load(r"C:/Users/kzhu/Documents/Learn Code/My WEBSITE/git_first_try/newGitTest1/F-War/images/hero1.png")



x = 0
y = 0

# if we only program for a certain progress, we can not achieve massive operations.
# To achieve massive operations,we need to employ "class" and program for objectives.



# Demand Analysis:
# 1) enemies: random trajectories;
# 2) heros: 
while True:
    screen.blit(bk, (0,0)) # relative position of the game window
    screen.blit(plane, (x,y)) # load plane in the background
    # before update, deal with events
    for event in pygame.event.get(): # fetch each event
        if event.type==pygame.locals.QUIT: # formal mode of exit event
            print("exit")
            exit()
        elif event.type==pygame.locals.KEYDOWN: # deal with the event from the keyboard
            if event.key==pygame.locals.K_w: # when we push the "k" we can see k in the result window.
                if y-10 > 0 :
                    y -= 10
            elif event.key==pygame.locals.K_s:
                if y+10 < 800:
                    y += 10
            elif event.key==pygame.locals.K_a:
                if x-10>0:
                    x -= 10
            elif event.key==pygame.locals.K_d:
                if x+10 < 480:
                    x += 10
    pygame.display.update()
