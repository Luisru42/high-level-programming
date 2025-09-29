import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hp = 100
        self.direction = -1
        self.speed = 2

    def update(self, player):
        if self.hp <= 0:
            return
        if abs(self.rect.x - player.rect.x) < 200:
            self.rect.x += self.speed * self.direction
        else:
            self.direction *= -1

        if self.rect.colliderect(player.rect):
            player.hp = max(player.hp - 1, 0)

        sword_hitbox = player.get_sword_hitbox()
        if sword_hitbox and sword_hitbox.colliderect(self.rect):
            self.hp = max(self.hp - 5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
