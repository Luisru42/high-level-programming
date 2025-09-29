import pygame


class UI:
    def __init__(self, player):
        self.player = player

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (50, 30, 100, 10))
        pygame.draw.rect(surface, (0, 255, 0), (50, 30, self.player.hp, 10))
        pygame.draw.rect(surface, (0, 0, 255), (50, 50, self.player.exp, 10))
