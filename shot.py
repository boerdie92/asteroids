import pygame
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        CircleShape.__init__(self, position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position),self.radius , 2)

    def update(self, dt, shots=None):
        self.position = (self.position + (self.velocity * dt))
