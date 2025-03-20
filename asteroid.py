import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        CircleShape.__init__(self, x, y, radius)

        # If no velocity is specified, assign a random one
        if velocity is None:
            speed = random.uniform(50, 150)  # Random speed between 50-150
            angle = random.uniform(0, 360)  # Random direction
            self.velocity = pygame.math.Vector2(speed, 0).rotate(angle)
        else:
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position),self.radius , 2)

    def split(self):
        self.kill()  # Destroy this asteroid
    
    # If the asteroid is too small, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

    # Splitting logic continues only for larger asteroids
        angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(angle)
        angle2 = self.velocity.rotate(-angle)

        velocity1 = angle1 * 1.2
        velocity2 = angle2 * 1.2

        radius_new = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius_new, velocity1)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius_new, velocity2)

    def update(self, dt, shots=None):
        self.position = (self.position + (self.velocity * dt))