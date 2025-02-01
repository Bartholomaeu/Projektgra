import pygame
import random
import time

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

# Load images
background = pygame.image.load("tlo.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

idle_img = pygame.image.load("mcidle.png")
attack_fire_img = pygame.image.load("mcattackfire.png")
attack_water_img = pygame.image.load("mcattackwater.png")
attack_earth_img = pygame.image.load("mcattackearth.png")
death_img = pygame.image.load("mcdeath.png")

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

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    player_health = 100
    enemy_health = 100
    player_sprite = idle_img  # Początkowa animacja postaci
    sprite_timer = 0  # Czas trwania animacji obrażeń

    while running:
        screen.blit(background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Testowe zmniejszenie HP dla demonstracji
        if random.randint(1, 100) > 98:
            damage_type = random.choice(["Fire", "Water", "Earth"])
            if damage_type == "Fire":
                player_sprite = attack_fire_img
            elif damage_type == "Water":
                player_sprite = attack_water_img
            elif damage_type == "Earth":
                player_sprite = attack_earth_img

            sprite_timer = time.time()
            player_health -= 10

        # Sprawdzenie czasu animacji obrażeń
        if sprite_timer and time.time() - sprite_timer > 0.5:
            player_sprite = idle_img  # Powrót do podstawowej animacji

        # Sprawdzenie śmierci postaci
        if player_health <= 0:
            player_sprite = death_img

        # Rysowanie postaci
        screen.blit(player_sprite, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))

        # Draw health bars
        player_health_text = FONT.render(f"Player Health: {player_health}", True, WHITE)
        screen.blit(player_health_text, (20, 20))

        enemy_health_text = FONT.render(f"Enemy Health: {enemy_health}", True, WHITE)
        screen.blit(enemy_health_text, (SCREEN_WIDTH - 250, 20))

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
