from random import random

import pygame

HEIGHT = 600
WIDTH = 400
class Entity2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,60))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.line_pos = WIDTH // 80
        self.rect.centerx = random.randint

x = WIDTH/5
for a in range(5):
    pygame.draw.rect(WIDTH-x)