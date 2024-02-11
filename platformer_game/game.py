import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Гавно")

walkRight = [pygame.image.load('R1.png'),
             pygame.image.load('R2.png'),
             pygame.image.load('R3.png'),
             pygame.image.load('R4.png'),
             pygame.image.load('R5.png'),
             pygame.image.load('R6.png'),
             pygame.image.load('R7.png'),
             pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'),
            pygame.image.load('L2.png'),
            pygame.image.load('L3.png'),
            pygame.image.load('L4.png'),
            pygame.image.load('L5.png'),
            pygame.image.load('L6.png'),
            pygame.image.load('L7.png'),
            pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1

    elif right:
        window.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        window.blit(char, (x, y))

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
