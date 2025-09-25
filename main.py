from constants import *
import pygame
from player import *
import inspect
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    ##Groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ##Group Assignment
    Player.containers = (drawable,updatable)
    Asteroid.containers = (drawable,updatable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers=(updatable,shots,drawable)
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroidField = AsteroidField()
    should_exit = False
    while not(should_exit):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        # Calc Step
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

                    

        # Render step.
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
