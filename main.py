import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import Shot

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    return screen, timer, updatable, drawable, asteroids, asteroidfield, player, shots

def main():
    screen, timer, updatable, drawable, asteroids, asteroidfield, player, shots = init_game()

    while True:
        dt = timer.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt, shots)

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