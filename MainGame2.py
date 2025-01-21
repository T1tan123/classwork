import pygame
from PlayerGame import Player, HEIGHT, WIDTH



pygame.init()

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


class RoadMarking:
    def __init__(self, nlines, line_width, screen):
        self.nlines = nlines
        self.line_width = line_width
        self.screen = screen
        self.r_list = []
        self._init_marking()

    def _init_marking(self):
        for lane in range(1, self.nlines):
            x = lane * self.line_width
            for i in range(-50, self.screen.get_height(), 100):
                self.r_list.append(pygame.Rect(x-2, i, 5, 40))
    def update(self, speed):
        for r in self.r_list:
            if r.top > self.screen.get_height():
                t = self.r_list.pop()
                self.r_list.insert(0,t)
            r.y += speed

        screen_height = self.screen.get_height()
        self.r_list = [rect for rect in self.r_list if rect.y < screen_height]

        for rect in self.r_list:
            if rect.y >= screen_height:
                self.r_list.append(pygame.Rect(rect.x, -50, rect.width, rect.height))






run = True
while run:
    screen.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    player.move(keys)

    all_sprites.draw(screen)
    roud.update(5)


    pygame.display.update()
    clock.tick(FPS)
pygame.quit()