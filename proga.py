import pygame

pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Minecraft 1.16.5!!!")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (79, 66, 120), (200, 200, 100, 100))
    pygame.display.flip()
