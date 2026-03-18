import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/Soldier.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midleft = (10, 300)
        self.speed = 4


    def update(self, keys):

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600