import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,position,speed,scr_height):
        super().__init__()
        self.image = pygame.Surface((4,15))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(center = position)
        self.scr_height = scr_height
        
        self.speed = speed
        
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y > self.scr_height + 15 or self.rect.y < 0:
            self.kill()