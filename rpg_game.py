import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
UI_HEIGHT = 100  # Height of the bottom UI section

# Colors
BACKGROUND_COLOR = (40, 40, 40)
UI_COLOR = (20, 20, 20)  # Darker gray for the bottom section
HEALTH_BAR_COLOR = (255, 0, 0)  # Red for health bar

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic RPG")

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

player_thumbnail = pygame.image.load("games/images/basic_mage.png")
# Resize the image to fit the 64x64 size (optional, if you need a specific size)
player_thumbnail = pygame.transform.scale(player_thumbnail, (64, 64))

player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill((0, 128, 255))  # Blue square for player thumbnail

# player_image = pygame.image.load("games/images/basic_mage.png")
# # Resize the image to fit the 64x64 size (optional, if you need a specific size)
# player_image = pygame.transform.scale(player_image, (64, 64))



# Player position in dungeon
player_x = 100
player_y = 100
player_speed = 4

# Player stats
health = 100
max_health = 100
inventory = ["Potion", "Sword", "Shield"]

# Font for text
font = pygame.font.SysFont("Arial", 20)


# Draw the dungeon (just tiles for now)
def draw_map():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT - UI_HEIGHT, TILE_SIZE):  # Don't draw in the UI area
            floor_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
            floor_tile.fill((40, 40, 40))  # Dark gray tile
            screen.blit(floor_tile, (x, y))


# Draw the bottom UI section (player info, health, inventory)
def draw_ui():
    pygame.draw.rect(screen, UI_COLOR, pygame.Rect(0, SCREEN_HEIGHT - UI_HEIGHT, SCREEN_WIDTH, UI_HEIGHT))

    # Draw player thumbnail
    screen.blit(player_thumbnail, (10, SCREEN_HEIGHT - UI_HEIGHT + 10))

    # Draw health bar
    health_bar_width = 200
    health_bar_height = 20
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(100, SCREEN_HEIGHT - UI_HEIGHT + 10, health_bar_width, health_bar_height))
    pygame.draw.rect(screen, HEALTH_BAR_COLOR,
                     pygame.Rect(100, SCREEN_HEIGHT - UI_HEIGHT + 10, (health / max_health) * health_bar_width,
                                 health_bar_height))

    # Draw health text
    health_text = font.render(f"Health: {health}/{max_health}", True, (255, 255, 255))
    screen.blit(health_text, (100, SCREEN_HEIGHT - UI_HEIGHT + 40))

    # Draw inventory
    inventory_text = font.render("Inventory:", True, (255, 255, 255))
    screen.blit(inventory_text, (350, SCREEN_HEIGHT - UI_HEIGHT + 10))

    # List items in the inventory
    inventory_y_offset = 40
    for i, item in enumerate(inventory):
        item_text = font.render(f"- {item}", True, (255, 255, 255))
        screen.blit(item_text, (350, SCREEN_HEIGHT - UI_HEIGHT + inventory_y_offset))
        inventory_y_offset += 30


# Handle player movement
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

    # Input handling
    keys = pygame.key.get_pressed()
    handle_movement(keys)

    # Draw the game world and UI
    draw_map()
    screen.blit(player_image, (player_x, player_y))  # Draw player in the dungeon
    draw_ui()  # Draw the bottom UI

    pygame.display.flip()  # Update the screen

# Quit
pygame.quit()
sys.exit()
