import pygame as pg

class World():
    
    def __init__(self, image):
        self.image = image
    
    def draw(self, surface):
        surface.blit(self.image, (0, 0))