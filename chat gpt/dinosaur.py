import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dinosaur Jumping Game')

# Load images
dino_image = pygame.image.load('dino.png').convert_alpha()
cactus_image = pygame.image.load('cactus.png').convert_alpha()

# Set up variables
dino_x = 100
dino_y = SCREEN_HEIGHT - 100
dino_speed = 0
dino_jump_height = 150
dino_jump_speed = 10
is_jumping = False
cactus_x = SCREEN_WIDTH
cactus_y = SCREEN_HEIGHT - 100
cactus_speed = 5
score = 0
font = pygame.font.SysFont(None, 30)

# Define functions
def display_score(score):
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def display_game_over():
    game_over_text = font.render('Game Over! Press SPACE to play again.', True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2))

def is_collision(dino_x, dino_y, cactus_x, cactus_y):
    if dino_x + dino_image.get_width() >= cactus_x and \
        dino_x <= cactus_x + cactus_image.get_width() and \
        dino_y + dino_image.get_height() >= cactus_y:
        return True
    else:
        return False

# Main game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                dino_speed = -dino_jump_speed

    # Move the cactus
    cactus_x -= cactus_speed
    if cactus_x < -cactus_image.get_width():
        cactus_x = SCREEN_WIDTH
        cactus_y = SCREEN_HEIGHT - 100 + random.randint(-50, 50)
        score += 1
        if score % 10 == 0:
            cactus_speed += 1

    # Move the dino
    if is_jumping:
        dino_y += dino_speed
        dino_speed += 1
        if dino_y > SCREEN_HEIGHT - 100:
            dino_y = SCREEN_HEIGHT - 100
            is_jumping = False
            dino_speed = 0

    # Check for collision
    if is_collision(dino_x, dino_y, cactus_x, cactus_y):
        running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(cactus_image, (cactus_x, cactus_y))
    display_score(score)
    if not running:
        display_game_over()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
