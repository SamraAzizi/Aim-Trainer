
import math
import random
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2


def main():
    run = True


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    
    pygame.quit()


if __name__ == "__main__":
    main()

