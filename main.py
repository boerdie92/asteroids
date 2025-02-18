import pygame
from constants import *
from player import Player

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    return screen, timer, updatable, drawable

def main():
    screen, timer, updatable, drawable = init_game()
    
    while True:
        dt = timer.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill((0,0,0))

        for drawa in drawable:
            drawa.draw(screen)
        
        pygame.display.flip()



if __name__ == "__main__":
    main()