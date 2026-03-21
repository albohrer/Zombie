import pygame
from Player import Player
from Zombie import Zombie
from Bullet import Bullet


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Zombie Survival")

        self.clock = pygame.time.Clock()
        self.player = Player()
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.start_time = pygame.time.get_ticks()
        self.background = pygame.image.load("assets/background.png").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.last_shot_time = 0
        self.shoot_delay = 300
        pygame.mixer.set_num_channels(16)
        # cria zombies iniciais
        for i in range(5):
            self.zombies.add(Zombie())

        # som de fundo e tiro
        pygame.mixer.music.load("assets/soundreality-horror.mp3")
        pygame.mixer.music.play(-1)

        self.shoot_sound = pygame.mixer.Sound("assets/gunshoot.mp3")

    def menu(self):
        font_title = pygame.font.Font(None, 60)
        font_menu = pygame.font.Font(None, 40)

        def centralizar(texto, y):
            x = (800 - texto.get_width()) // 2
            self.screen.blit(texto, (x, y))

        while True:

            self.screen.fill((0, 0, 0))

            # textos do menu
            title = font_title.render("ZOMBIE SURVIVAL", True, (0, 0, 255))
            play = font_menu.render("ENTER - Start", True, (0, 255, 0))
            shoot = font_menu.render("SPACE - Shoot", True, (255, 255, 255))
            up = font_menu.render("UP ARROW - Move Up", True, (255, 255, 255))
            down = font_menu.render("DOWN ARROW - Move Down", True, (255, 255, 255))

            # desenha na tela
            centralizar(title, 120)
            centralizar(play, 220)
            centralizar(shoot, 320)
            centralizar(up, 370)
            centralizar(down, 420)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                # inicia o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def run(self):
        self.menu()
        self.start_time = pygame.time.get_ticks()
        running = True

        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                current_time = pygame.time.get_ticks()

                # controla o tempo entre bullets
                if current_time - self.last_shot_time > self.shoot_delay:

                    # limita quantidade de bullet na tela
                    if len(self.bullets) < 5:
                        bullet = Bullet(self.player.rect.right, self.player.rect.centery - 30)
                        self.bullets.add(bullet)
                        # som sempre sincronizado
                        pygame.mixer.find_channel(True).play(self.shoot_sound)

                        self.last_shot_time = current_time

            self.player.update(keys)
            self.zombies.update()
            self.bullets.update()

            # colisão bullet x zombie
            for bullet in self.bullets:
                hits = pygame.sprite.spritecollide(bullet, self.zombies, True)
                if hits:
                    bullet.kill()
                    self.zombies.add(Zombie())

            # colisão soldier x zombie
            for zombie in self.zombies:
                if pygame.time.get_ticks() - self.start_time > 3000:
                    for zombie in self.zombies:
                        if self.player.rect.colliderect(zombie.rect):
                            print("GAME OVER")
                            running = False

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image, self.player.rect)

            for zombie in self.zombies:
                self.screen.blit(zombie.image, zombie.rect)

            for bullet in self.bullets:
                self.screen.blit(bullet.image, bullet.rect)

            pygame.display.update()

        pygame.quit()
