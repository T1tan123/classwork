import random

import pygame


class Player:
    def __init__(self, color, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = pygame.Rect(x, y ,width, height)
        self.exp = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -=  self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

class Enemy(Player):
    def move(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.bottom = 0
            self.rect.x = random.randint(0 , 760)






pygame.init()

FPS = 120

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player1 = Player((255,0,0), 400, 500, 40 , 40, 5)



enemies = []
for i in range(10):
    enemy1 = Enemy((0,225,0),
                   random.randint(0, 760),
                   random.randint(40, 80)*(-1),
                   random.randint(20, 40),
                   random.randint(20, 40),
                   random.randint(3, 10)
                   )
    enemies.append(enemy1)



run = True

while run:
    screen.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    for enemy in enemies:
        if player1.rect.colliderect(enemy.rect):
            player1.color = (225,0,0)
            FPS = 1

        if enemy.rect.y >=600:
            player1.exp += 1







    keys = pygame.key.get_pressed()
    player1.move(keys)
    for e in enemies:
        e.move()
        e.draw(screen)
    #print(keys)

    player1.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()