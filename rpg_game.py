import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic RPG")

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Load player image (you can replace this with a real sprite!)
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill((0, 128, 255))  # Blue square

# Player position
player_x = 100
player_y = 100
player_speed = 4

# Load tile image (placeholder floor tile)
floor_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
floor_tile.fill((40, 40, 40))  # Dark gray tile

# Draw a room (grid of tiles)
def draw_map():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(floor_tile, (x, y))
def handle_movement(keys):
    global player_x, player_y
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
# Main loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    handle_movement(keys)

    # Draw
    draw_map()
    screen.blit(player_image, (player_x, player_y))
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
