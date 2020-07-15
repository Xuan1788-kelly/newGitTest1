import pygame
import plane2.bullet
class jplane(pygame.sprite.Sprite):
    def __init__(self,planetype, bg_size, x, y, screen):
        # 敌机创建的主要行为： 出现，移动，攻击
        pygame.sprite.Sprite.__init__(self)
        self.planetype=planetype
        if planetype==1:
            self.image=pygame.image.load(r"../source/images/enemy1.png").convert_alpha()
        elif planetype==2:
            self.image=pygame.image.load(r"../source/images/enemy2.png").convert_alpha()
        elif planetype==3:
            self.image=pygame.image.load(r"../source/images/enemy3.png").convert_alpha()

        

        
        self.destroy_images = []
        self.destroy_images.append(pygame.image.load(r"../source/images/enemy1_down1.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/enemy1_down2.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/enemy1_down3.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/enemy1_down4.png"))

        self.rect=self.image.get_rect()
        self.width=bg_size[0]
        self.height=bg_size[1]
        '''self.rect.left=(self.width-self.rect.width)/2 # position
        self.rect.top=self.height-self.rect.height-100'''
        self.rect.left = x
        self.rect.top = y
        self.rect.bottom = y + self.rect.height
        self.speed=1
        self.screen=screen

        # 在飞机对象中创建子弹集合，让两架飞机同时可以发射子弹
        self.bulletlist=[] # 子弹集合
        pass
    def move(self):
        self.rect.top +=self.speed
        pass

    # 创建子弹集合
    def fire(self):
        if self.planetype==1:
            # 小型敌机
            for i in range(10):
                b1=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2,self.rect.top,self.screen,False)
                # 用append将创建的对象加载到创建的list中
                self.bulletlist.append(b1)
        elif self.planetype==2:
            # 中型敌机
            for i in range(10):
                b1=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2,self.rect.bottom,self.screen,False)
                b2=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2+20,self.rect.bottom,self.screen,False)
                b3=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2-20,self.rect.bottom,self.screen,False)
            
                # 用append将创建的对象加载到创建的list中
                self.bulletlist.append(b1)
                self.bulletlist.append(b2)
                self.bulletlist.append(b3)
        elif self.planetype==3:
            # 大型敌机
            for i in range(10):
                b1=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2,self.rect.bottom,self.screen,False)
                b2=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2+20,self.rect.bottom,self.screen,False)
                b3=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2-20,self.rect.bottom,self.screen,False)
                b4=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2+40,self.rect.bottom,self.screen,False)
                b5=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2-40,self.rect.bottom,self.screen,False)
                # 用append将创建的对象加载到创建的list中
                self.bulletlist.append(b1)
                self.bulletlist.append(b2)
                self.bulletlist.append(b3)
                self.bulletlist.append(b4)
                self.bulletlist.append(b5)
        pass

    def show(self):
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        # 在飞机对象的显示方法中，将子弹list里面的对象依次显示出来
        for bt in self.bulletlist:
            bt.show()
            bt.move(False)
        pass
    def reset(self):
        pass
