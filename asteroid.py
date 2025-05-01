from circleshape import CircleShape
from constants import *
import pygame
from main import screen
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self):
        pygame.draw.circle(screen, "red",(x,y) , self.radius, 2)

    
    def update(self,dt):
       self.position += (self.velocity * dt)

 