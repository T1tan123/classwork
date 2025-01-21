import  pygame
from PlayerGame import Player
from pygame.draw_py import draw_line


class Objekt:
    def __init__(self, whline, num, screen):
        self.whline = whline
        self.num = num
        self.screen = screen
        self.ofset = 0
    def update(self, speed):
        self.ofset = speed

    def drow(self):
        x = self.screen.get_widh()
        y = self.screen.get_heigt()
        self.whline = x / self.num
        for g in range(self.num):
            pygame.draw.rect(self.screen, (255,255,255), x-self.whline, )





