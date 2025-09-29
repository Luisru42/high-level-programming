import pygame


class Map:
    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 500, 960, 40),
            pygame.Rect(300, 400, 200, 20),
            pygame.Rect(600, 300, 150, 20)
        ]

    def draw(self, surface):
        for plat in self.platforms:
            pygame.draw.rect(surface, (100, 100, 100), plat)
