import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 80))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False
        self.hp = 100
        self.exp = 0
        self.attacking = False
        self.attack_cooldown = 0

    def update(self, keys, platforms):
        dx = 0
        if keys[pygame.K_a]:
            dx = -5
        if keys[pygame.K_d]:
            dx = 5
        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False
        if keys[pygame.K_SPACE] and self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 30
        else:
            self.attacking = False

        self.vel_y += 1
        self.rect.y += self.vel_y
        self.rect.x += dx

        # Collision
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.attacking:
            pygame.draw.rect(
                surface,
                (255, 0, 0),
                (self.rect.right, self.rect.centery - 5, 20, 10)
            )

    def get_sword_hitbox(self):
        if self.attacking:
            return pygame.Rect(self.rect.right, self.rect.centery - 5, 20, 10)
        return None
