

import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 20
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control frame rate
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Fill screen and draw circle
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    pygame.display.update()

# Quit Pygame
pygame.quit()