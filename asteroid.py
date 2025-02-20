import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position),self.radius , 2)

    def update(self, dt, shots=None):
        self.position = (self.position + (self.velocity * dt))