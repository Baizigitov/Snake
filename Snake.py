import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


font = pygame.font.SysFont("Verdana", 15)

radius = 20
snake_pos = [screen_width / 2, screen_height - radius]
snake_size = 40

snake_list = []

x = random.randrange(radius, screen_width - radius, radius*2)
y = random.randrange(radius, screen_height - radius, radius*2)

speed_x = snake_size
speed_y = 0
score = 0
game_over = False
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and speed_x == 0:
            speed_x = -snake_size
            speed_y = 0
        elif keys[pygame.K_RIGHT] and speed_x == 0:
            speed_x = snake_size
            speed_y = 0
        elif keys[pygame.K_UP] and speed_y == 0:
            speed_y = -snake_size
            speed_x = 0
        elif keys[pygame.K_DOWN] and speed_y == 0:
            speed_y = snake_size
            speed_x = 0
        if snake_pos[0] < radius or snake_pos[0] > screen_width or snake_pos[1] < radius or snake_pos[1] > screen_height:
            game_over = True
        if x == snake_pos[0] and y == snake_pos[1]:
            score += 1
            snake_list.append([x - snake_size, y - snake_size])
            while True:
                x = random.randrange(radius, screen_width-radius, radius*2)
                y = random.randrange(
                    radius, screen_height - radius, radius*2)
                if all(snake[0] != x or snake[1] != y for snake in snake_list):
                    break
        for snake in snake_list:
            if snake_pos[0] == snake[0] and snake_pos[1] == snake[1]:
                game_over = True
    snake_list.insert(0, [snake_pos[0], snake_pos[1]])
    if snake_pos[0] != x or snake_pos[1] != y:
        snake_list.pop()

    snake_pos[0] += speed_x
    snake_pos[1] += speed_y

    screen.fill(black)

    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.draw.circle(
        screen, green, (snake_pos[0], snake_pos[1]), radius)
    for snake in snake_list:
        pygame.draw.circle(
            screen, green, (snake[0], snake[1]), radius)
    score_text = font.render(f'Съедено яблок: {score}', True, white)
    screen.blit(score_text, (10, 10))

    if game_over:
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
