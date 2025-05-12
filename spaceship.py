import pygame
from laser import Laser

class spaceship(pygame.sprite.Sprite):    #sprite used to manage and organise objeects
    def __init__(self, scr_width, scr_height):
        self.scr_width = scr_width
        self.scr_height = scr_height
        super().__init__()
        self.image = pygame.image.load("gallary/spaceship3.png")
        original_image = pygame.image.load("gallary/spaceship3.png")
        self.image = pygame.transform.scale(original_image, (75, 75))
        self.rect = self.image.get_rect(midbottom = (self.scr_width/2,self.scr_height))   #spaceship location
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 130
        self.laser_sound = pygame.mixer.Sound("sounds/sounds_laser.ogg")
        
        
        
    def get_user_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False    
            laser = Laser(self.rect.center, 5 ,self.scr_height)   
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()
            
    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()
        
    def constrain_movement(self):
        if self.rect.right > self.scr_width + 40:
            self.rect.right = self.scr_width + 40
        if self.rect.left < 10:
            self.rect.left = 10
                 
    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
                
                
    def reset(self):
        self.rect = self.image.get_rect(midbottom = (self.scr_width/2 , self.scr_height))
        self.lasers_group.empty()