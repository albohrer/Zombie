import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        #Carrega imagem com transparência, austa o tamanho e define a posição
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 10))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 5 # velocidade do tiro

    def update(self):
        self.rect.x += self.speed #movimento do tiro

        #Remove o tiro ao sair da tela
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
