import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 10))
        self.rect = self.image.get_rect(center=(x,y))

        self.speed = 8

    def update(self):
        self.rect.x += self.speed

        if self.rect.y < 0:
            self.kill()