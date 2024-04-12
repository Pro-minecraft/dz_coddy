import random

import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
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
        self.score = 0

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            bullets.append(bullet.get_rect(topleft=()))
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.x += 4
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        enemy_image = pygame.image.load("1645963596_2-kartinkin-net-p-kartinki-zombi-iz-mainkrafta-2.jpg").convert_alpha()
        self.surf = pygame.transform.scale(enemy_image,(90,190))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH - 50, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = y
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
pygame.mixer.init()
pygame.mixer.music.load("Minecraft.mp3")
pygame.mixer.music.play(loops=-1)
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bullet = pygame.image.load('bullets_PNG35620.jpg').convert_alpha()
bullets = []

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

running = True

font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    screen.blit(bg, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollide(player, enemies, True):
        player.kill()
        break

    screen.blit(player.surf, player.rect.topleft)
    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
