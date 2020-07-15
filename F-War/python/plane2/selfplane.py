import pygame
import plane2.bullet
class myplane(pygame.sprite.Sprite):
    def __init__(self,bg_size, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load(r"../source/images/hero1.png").convert_alpha()
        self.image2=pygame.image.load(r"../source/images/hero2.png").convert_alpha()

        
        self.destroy_images = []
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n1.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n2.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n3.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n4.png"))

        self.rect=self.image1.get_rect()
        self.width=bg_size[0]
        self.height=bg_size[1]
        '''self.rect.left=(self.width-self.rect.width)/2 # position
        self.rect.top=self.height-self.rect.height-100'''
        self.rect.left = x
        self.rect.top = y
        self.speed=10 # +10, -10
        self.screen=screen

        # 在飞机对象中创建子弹集合，让两架飞机同时可以发射子弹
        self.bulletlist=[] # 子弹集合
        pass
    def moveup(self):
        if self.rect.top - 10 >= 0:
            self.rect.top-=10
        pass
    def movedown(self):
        if self.rect.top + 10 <= 800:
            self.rect.top+=10
        pass
    def moveleft(self):
        if self.rect.left - 10 >= 0:
            self.rect.left-=10
        pass
    def moveright(self):
        if self.rect.left + 10 <= 480:
            self.rect.left += 10
        pass
    # 创建子弹集合
    def fire(self):
        for i in range(10):
            b1=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2,self.rect.top,self.screen,True)
            b2=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2+30,self.rect.top,self.screen,True)
            b3=plane2.bullet.Bullet((self.rect.left+self.rect.right)/2-30,self.rect.top,self.screen,True)
            # 用append将创建的对象加载到创建的list中
            self.bulletlist.append(b1)
            self.bulletlist.append(b2)
            self.bulletlist.append(b3)

    def show(self):
        self.screen.blit(self.image1, (self.rect.left, self.rect.top))
        # 在飞机对象的显示方法中，将子弹list里面的对象依次显示出来
        for bt in self.bulletlist:
            bt.show()
            bt.move(True)
        pass
    def reset(self):
        pass
