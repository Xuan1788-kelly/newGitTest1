import pygame
import pygame.midi
import pygame.locals
import plane3.myplane
import time


pygame.init() # initialization
pygame.mixer.init() # initialization for playing music
bg_size = width,heigth=480, 800 # show the main window

screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("Good Luck on this War!")
bk=pygame.image.load(r"C:/Users/kzhu/Documents/Learn Code/My WEBSITE/git_first_try/newGitTest1/F-War/images/background.png")

# load background music
pygame.mixer.music.load(r"../source/music/background.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

myp = plane1.myplane.myplane(bg_size) # class
myp.alive()
myp.update()
plane=pygame.image.load(r"C:/Users/kzhu/Documents/Learn Code/My WEBSITE/git_first_try/newGitTest1/F-War/images/hero1.png")


while True:
    screen.blit(bk, (0,0))

    for myimage in myp.destroy_images:
        screen.blit(myimage, (10, 10))
        time.sleep(0.1)
    screen.blit(myp.image1, (10,10))
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            print("exit")
            exit()
        elif event.type==pygame.locals.KEYDOWN:
            if event.key==pygame.locals.K_k:
                print("blow up")
                for myimage in myp.destroy_images:
                    screen.blit(myimage, (10, 10))
                    time.sleep(0.1)
    pygame.display.update()
