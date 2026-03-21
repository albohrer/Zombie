import pygame
import random


class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Carrega imagem com transparência, austa o tamanho, define a posição e velocidade
        self.image = pygame.image.load("assets/zombie.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed = random.randint(2, 3)
        self.spawn()

    def spawn(self):
        #Posiciona o zombie
        while True:
            self.rect.x = random.randint(820, 1000)
            self.rect.y = random.randint(80, 480)

            # evita nascer perto do soldier
            if abs(self.rect.x - 400) > 150:
                break

    def update(self):
        #Move o zombie para esquerda na direção do soldier se sair da tela reaparece em nova posição
        self.rect.x -= self.speed

        if self.rect.x < -100:
            self.spawn()
