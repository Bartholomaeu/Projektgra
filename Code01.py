import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Fonts
FONT = pygame.font.Font(None, 36)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elemental Card Duel")

# Load background image
background = pygame.image.load("tlo.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Element strengths
ELEMENT_STRENGTHS = {
    "Fire": "Earth",
    "Water": "Fire",
    "Earth": "Water"
}

# Card class
class Card:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def draw(self, x, y):
        pygame.draw.rect(screen, WHITE, (x, y, 100, 150))
        text = FONT.render(self.name, True, BLACK)
        screen.blit(text, (x + 5, y + 10))
        elem_text = FONT.render(self.element, True, BLACK)
        screen.blit(elem_text, (x + 5, y + 90))

# Special Card class
class SpecialCard:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def draw(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x, y, 100, 150))
        text = FONT.render(self.name, True, BLACK)
        screen.blit(text, (x + 5, y + 10))

# Projectile class
class Projectile:
    def __init__(self, x, y, speed, element):
        self.x = x
        self.y = y
        self.speed = speed
        self.element = element

    def move(self):
        self.x += self.speed

    def draw(self):
        color = RED if self.element == "Fire" else BLUE if self.element == "Water" else GREEN
        pygame.draw.circle(screen, color, (self.x, self.y), 10)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    # Player and enemy data
    player_health = 100
    enemy_health = 100
    double_damage = False
    special_used = {
        "Reveal": False,
        "Heal": False,
        "Double": False
    }

    player_deck = [
        Card("Flame", "Fire"),
        Card("Aqua", "Water"),
        Card("Terra", "Earth")
    ]

    special_cards = [
        SpecialCard("Reveal", "Reveal Enemy Element"),
        SpecialCard("Heal", "Heal 10 HP"),
        SpecialCard("Double", "Double Damage")
    ]

    player_projectile = None
    enemy_projectile = None
    revealed_element = None

    while running:
        screen.blit(background, (0, 0))  # Display background image

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw health bars
        player_health_text = FONT.render(f"Player Health: {player_health}", True, WHITE)
        screen.blit(player_health_text, (20, 20))

        enemy_health_text = FONT.render(f"Enemy Health: {enemy_health}", True, WHITE)
        screen.blit(enemy_health_text, (SCREEN_WIDTH - 250, 20))

        # Draw revealed element
        if revealed_element:
            reveal_text = FONT.render(f"Enemy Element: {revealed_element}", True, YELLOW)
            screen.blit(reveal_text, (20, 60))

        # Draw player and enemy
        pygame.draw.rect(screen, BLUE, (100, SCREEN_HEIGHT // 2 - 50, 100, 100))
        pygame.draw.polygon(screen, RED, [
            (SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2 - 50),
            (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 + 50),
            (SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2 + 50)
        ])

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

