import pygame
import random


class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/zombie.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        self.speed = random.randint(2, 4)

        self.spawn()

    def spawn(self):

        while True:
            self.rect.x = random.randint(820, 1000)  # fora da tela à direita
            self.rect.y = random.randint(80, 480)

            # evita nascer perto do centro (player)
            if abs(self.rect.x - 400) > 150:
                break

    def update(self):

        self.rect.x -= self.speed

        if self.rect.x < -100:
            self.spawn()
