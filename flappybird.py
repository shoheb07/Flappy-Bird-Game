import pygame
import random

pygame.init()

# Window
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,200,0)
YELLOW = (255,255,0)

# Bird
bird_x = 100
bird_y = HEIGHT//2
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Pipes
pipe_width = 70
pipe_gap = 180
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None,36)

# Pipe spawn timer
spawn_timer = 0


def draw_bird():
    pygame.draw.circle(screen,YELLOW,(bird_x,bird_y),15)


def spawn_pipe():
    height = random.randint(100,400)
    top_pipe = pygame.Rect(WIDTH,0,pipe_width,height)
    bottom_pipe = pygame.Rect(WIDTH,height+pipe_gap,pipe_width,HEIGHT)
    pipes.append((top_pipe,bottom_pipe))


running = True

while running:

    clock.tick(60)
    screen.fill((135,206,235))  # sky blue

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    # Spawn pipes
    spawn_timer += 1
    if spawn_timer > 90:
        spawn_pipe()
        spawn_timer = 0

    # Move pipes
    for pipe in pipes:
        pipe[0].x -= 3
        pipe[1].x -= 3

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen,GREEN,pipe[0])
        pygame.draw.rect(screen,GREEN,pipe[1])

    # Collision
    bird_rect = pygame.Rect(bird_x-15,bird_y-15,30,30)

    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            running = False

    # Score
    for pipe in pipes:
        if pipe[0].x == bird_x:
            score += 1

    # Draw bird
    draw_bird()

    # Score text
    score_text = font.render(f"Score: {score}",True,BLACK)
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()
