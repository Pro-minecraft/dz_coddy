import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение размеров игрового окна
width, height = 1000, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Настройки змейки
size_snake = 10
speed_snake = 5

# Начальное положение и направление змеи
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (size_snake, 0)

# Начальное положение еды
food = (random.randrange(1, (width // size_snake)) * size_snake,
        random.randrange(1, (height // size_snake)) * size_snake)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Обработка событий клавиш для изменения направления змеи
            if event.key == pygame.K_UP and snake_direction != (0, size_snake):
                snake_direction = (0, -size_snake)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -size_snake):
                snake_direction = (0, size_snake)
            elif event.key == pygame.K_LEFT and snake_direction != (size_snake, 0):
                snake_direction = (-size_snake, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-size_snake, 0):
                snake_direction = (size_snake, 0)

    # Двигаем змею
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Проверяем, съела ли змея еду
    if snake[0] == food:
        snake.append(snake[-1])  # Увеличиваем змею
        food = (random.randrange(1, (width // size_snake)) * size_snake,
                random.randrange(1, (height // size_snake)) * size_snake)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Счет: {snake.score}", True, (0,0,0))
    window.blit(score_text, (10, 10))


    if (snake[0] in snake[1:] or
            snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height):
        pygame.quit()
        sys.exit()

    # Рисуем игровое окно
    window.fill(white)
    pygame.draw.rect(window, red, (*food, size_snake, size_snake))

    for segment in snake:
        pygame.draw.rect(window, green, (*segment, size_snake, size_snake))

    pygame.display.flip()

    # Управление скоростью змеи
    pygame.time.Clock().tick(speed_snake)
