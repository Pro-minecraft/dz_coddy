import random

import pygame
from pygame.locals import (
    RLEACCEL,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Minecraft")
bg = pygame.image.load('1031.jpg')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_image = pygame.image.load("promc_.png").convert()
        self.surf = pygame.transform.scale(player_image, (80, 190))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT // 2
        self.score = 0

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy_skel(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_skel, self).__init__()
        enemy_image = pygame.image.load("1ske.jpg").convert()
        self.surf = pygame.transform.scale(enemy_image, (50, 190))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_HEIGHT - 400,
                SCREEN_WIDTH - 10,
            )
        )
        self.speed = 10


class Enemy_krip(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_krip, self).__init__()
        enemy_image = pygame.image.load("1645772145_1-kartinkin-net-p-kartinki-kripera-1.png").convert()
        self.surf = pygame.transform.scale(enemy_image, (50, 190))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_HEIGHT - 400,
                SCREEN_WIDTH - 10,
            )
        )
        self.speed = 10

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Enemy_zomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_zomb, self).__init__()
        enemy_image = pygame.image.load("3F3F%3F_JE3_BE2.png").convert()
        self.surf = pygame.transform.scale(enemy_image, (50, 190))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_HEIGHT - 400,
                SCREEN_WIDTH - 10,
            )
        )
        self.speed = 10


mobs = [Enemy_krip, Enemy_skel, Enemy_zomb]
mob = random.choice(mobs)
pygame.mixer.init()

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

pygame.mixer.music.load("Minecraft.mp3")
pygame.mixer.music.play(loops=-1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy_krip()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    screen.blit(bg, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        break
    screen.blit(player.surf, player.rect.topleft)
    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
