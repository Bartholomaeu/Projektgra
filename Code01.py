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
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check special card selection
                for i, card in enumerate(special_cards):
                    if 20 + i * 120 <= x <= 120 + i * 120 and SCREEN_HEIGHT - 200 <= y <= SCREEN_HEIGHT - 50:
                        if card.name == "Reveal" and not special_used["Reveal"]:
                            revealed_element = random.choice(["Fire", "Water", "Earth"])
                            special_used["Reveal"] = True
                        elif card.name == "Heal" and not special_used["Heal"]:
                            player_health = min(player_health + 10, 100)
                            special_used["Heal"] = True
                        elif card.name == "Double" and not special_used["Double"]:
                            double_damage = True
                            special_used["Double"] = True

                # Check elemental card selection
                for i, card in enumerate(player_deck):
                    if SCREEN_WIDTH // 2 - 240 + i * 120 <= x <= SCREEN_WIDTH // 2 - 140 + i * 120 and SCREEN_HEIGHT - 200 <= y <= SCREEN_HEIGHT - 50:
                        if not player_projectile:
                            player_projectile = Projectile(200, SCREEN_HEIGHT // 2, 10, card.element)
                            enemy_choice = random.choice(player_deck)
                            enemy_projectile = Projectile(SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2, -10,
                                                          enemy_choice.element)

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

        # Draw special cards
        for i, card in enumerate(special_cards):
            card.draw(20 + i * 120, SCREEN_HEIGHT - 200)

        # Draw elemental cards
        for i, card in enumerate(player_deck):
            card.draw(SCREEN_WIDTH // 2 - 240 + i * 120, SCREEN_HEIGHT - 200)

        # Handle projectiles
        if player_projectile:
            player_projectile.move()
            player_projectile.draw()

        if enemy_projectile:
            enemy_projectile.move()
            enemy_projectile.draw()

        # Check collision
        if player_projectile and enemy_projectile and abs(player_projectile.x - enemy_projectile.x) < 20:
            if ELEMENT_STRENGTHS[player_projectile.element] == enemy_projectile.element:
                enemy_projectile = None
            elif ELEMENT_STRENGTHS[enemy_projectile.element] == player_projectile.element:
                player_projectile = None
            else:
                player_projectile = None
                enemy_projectile = None

        # Check if projectiles hit their target
        if player_projectile and player_projectile.x >= SCREEN_WIDTH - 150:
            damage = 20 if not double_damage else 40
            enemy_health -= damage
            player_projectile = None
            double_damage = False

        if enemy_projectile and enemy_projectile.x <= 150:
            player_health -= 20
            enemy_projectile = None

        # Check for win/lose
        if player_health <= 0:
            lose_text = FONT.render("You Lose!", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if enemy_health <= 0:
            win_text = FONT.render("You Win!", True, GREEN)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()