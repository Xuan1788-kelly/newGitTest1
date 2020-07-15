import pygame
class Bullet(pygame.sprite.Sprite):
    # 子弹的设计要尽可能的通用，可以设置参数判断是否为我方飞机，从而根据不同的情况设计子弹
    def __init__(self, x, y, screen, ismy):
        pygame.sprite.Sprite.__init__(self)
        if ismy:
            self.image1 = pygame.image.load(r"../source/images/bullet1.png").convert_alpha()
        else:
            self.image1 = pygame.image.load(r"../source/images/bullet2.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.left = x
        self.rect.top = y

        self.speed=1
        self.screen = screen # 屏幕 -> 创建的对象可以将自己显示出来

    def move(self, ismy):
        if ismy:
            self.rect.top -= self.speed # 子弹的移动不需要考虑轨迹上线
        else:
            self.rect.top += self.speed
        pass

    # 需要show函数显示子弹
    def show(self):
        # 子弹可以显示自己的图片，以及自己的位置
        self.screen.blit(self.image1, (self.rect.left, self.rect.top))
