import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *

# Test setup for CircleShape collision
#circle1 = CircleShape(0, 0, 10)  # A circle at (0, 0) with radius 10
#circle2 = CircleShape(15, 0, 10)  # Another circle at (15, 0), also with radius 10

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    return screen, timer, updatable, drawable, asteroids, asteroidfield, player

def main():
    screen, timer, updatable, drawable, asteroids, asteroidfield, player = init_game()

    # Test if the two circles collide
    #if circle1.collision(circle2):
    #    print("Collision detected!")
    #else:
    #    print("No collision!")

    while True:
        dt = timer.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill((0,0,0))

        for drawa in drawable:
            drawa.draw(screen)
        
        pygame.display.flip()



if __name__ == "__main__":
    main()