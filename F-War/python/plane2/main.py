import pygame
import pygame.midi
import pygame.locals
import plane2.selfplane
import plane2.enemyplane
import time



class Mainclass():
    def __init__(self, title):
        pygame.init()
        pygame.mixer.init()
        self.bg_size = width,height=480, 800

        self.screen=pygame.display.set_mode(self.bg_size)
        pygame.display.set_caption(title)
        self.bk=pygame.image.load(r"..\source\images\background.png").convert()

        self.myp1=plane2.selfplane.myplane(self.bg_size, 0, 0, self.screen)
        self.myp2=plane2.selfplane.myplane(self.bg_size, 150, 0, self.screen)
        self.enemy=plane2.enemyplane.jplane(3,self.bg_size,0,0,self.screen)

        pygame.mixer.music.load(r"..\source\music\background.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        pass
    
    def go(self):
        while True:
            self.screen.blit(self.bk, (0, 0))
            self.myp1.show()
            self.myp2.show()
            self.enemy.show()

            for event in pygame.event.get():
                if event.type==pygame.locals.QUIT:
                    print("exit")
                    exit()
                elif event.type==pygame.locals.KEYDOWN:
                    self.enemy.move()
                    if event.key==pygame.locals.K_w:
                        self.myp1.moveup()
                        self.myp2.moveup()
                        print("w")
                        
                    elif event.key==pygame.locals.K_s:
                        self.myp1.movedown()
                        self.myp2.movedown()
                        print("s")
                    elif event.key==pygame.locals.K_a:
                        self.myp1.moveleft()
                        self.myp2.moveleft()
                        print("a")
                    elif event.key==pygame.locals.K_d:
                        self.myp1.moveright()
                        self.myp2.moveright()
                        print("d")
                    elif event.key==pygame.locals.K_SPACE:
                        # 子弹的出现以及移动都是依托于飞机
                        # 所以我们在创建飞机对象的时候创建子弹
                        self.myp1.fire()
                        self.myp2.fire()
                        self.enemy.fire()
                        print("space")
            pygame.display.update() # to show the window picture, must update the whole window

main=Mainclass("Double Plane War")
main.go()
