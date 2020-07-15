import pygame

class myplane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load(r"../source/images/hero1.png").convert_alpha()
        self.image2=pygame.image.load(r"../source/images/hero2.png").convert_alpha()

        
        self.destroy_images = []
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n1.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n2.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n3.png"))
        self.destroy_images.append(pygame.image.load(r"../source/images/hero_blowup_n4.png"))

        self.rect=self.image1.get_rect()
        """self.width=self.image1.get_rect().width
        self.height=
        self.speed=
        self.active=
        self.invincible="""
        pass
    def moveup(self):
        pass
    def movedown(self):
        pass
    def moveleft(self):
        pass
    def moveright(self):
        pass
    def reset(self):
        pass
