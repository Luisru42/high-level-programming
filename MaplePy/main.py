import pygame
from engine.player import Player
from engine.enemy import Enemy
from engine.map import Map
from engine.ui import UI

pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()

player = Player(100, 400)
enemy = Enemy(700, 400)
game_map = Map()
ui = UI(player)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update(keys, game_map.platforms)
    enemy.update(player)

    screen.fill((30, 30, 60))
    game_map.draw(screen)
    enemy.draw(screen)
    player.draw(screen)
    ui.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    pygame.quit()
