import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, type,x,y):
        super().__init__()
        self.type = type
        path = f"gallary/ufo{type}.png"
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect(topleft = (x,y))
        
    
    def update(self,direction):
        self.rect.x += direction
        
        

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.image = pygame.image. load("gallary/boss2.png")
        self.image = pygame.transform.scale(self.image, (100, 60))

        x = random. choice([0, self.screen_width - self.image.get_width()])
        if x == 0:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft = (x, 40))
        
    def update(self):
        self.rect.x += self.speed
        
        if self.rect.right > self.screen_width + 40:
            self.kill()
            
        elif self.rect.left < 10 :
            self.kill()