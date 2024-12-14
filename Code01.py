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
GRAY = (50, 50, 50)

# Fonts
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 28)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projekt-D")

# Card class
class Card:
    def __init__(self, name, damage, mana_cost, element):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.element = element

    def draw(self, x, y):
        pygame.draw.rect(screen, WHITE, (x, y, 140, 180))  # Slightly larger cards
        text = SMALL_FONT.render(self.name, True, BLACK)
        screen.blit(text, (x + 10, y + 10))
        dmg_text = SMALL_FONT.render(f"DMG: {self.damage}", True, BLACK)
        screen.blit(dmg_text, (x + 10, y + 50))
        mana_text = SMALL_FONT.render(f"Mana: {self.mana_cost}", True, BLACK)
        screen.blit(mana_text, (x + 10, y + 90))
        elem_text = SMALL_FONT.render(self.element, True, BLACK)
        screen.blit(elem_text, (x + 10, y + 130))

# Player and Enemy classes
class Player:
    def __init__(self):
        self.health = 100
        self.mana = 50
        self.deck = [
            Card("Fireball", 20, 10, "Fire"),
            Card("Water Blast", 15, 8, "Water"),
            Card("Earth Slam", 25, 12, "Earth"),
            Card("Wind Slash", 10, 5, "Wind")
        ]

class Enemy:
    def __init__(self, health):
        self.health = health

# Projectile class
class Projectile:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = 10

    def move(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), 10)

# Draw health and mana bars
def draw_bars(x, y, current, maximum, color, label, center_x):
    bar_width = 200
    bar_height = 20
    filled_width = int((current / maximum) * bar_width)
    pygame.draw.rect(screen, GRAY, (x, y, bar_width, bar_height))
    pygame.draw.rect(screen, color, (x, y, filled_width, bar_height))
    text = FONT.render(f"{label}: {current}/{maximum}", True, WHITE)
    text_rect = text.get_rect(center=(center_x, y - 15))
    screen.blit(text, text_rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    player = Player()
    enemy = Enemy(health=100)

    selected_card = None
    projectiles = []

    while running:
        screen.fill(BLACK)

        # Draw UI background
        interface_height = 250  # Increased height for the UI
        pygame.draw.rect(screen, GRAY, (0, SCREEN_HEIGHT - interface_height, SCREEN_WIDTH, interface_height))
        pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT - interface_height), (SCREEN_WIDTH, SCREEN_HEIGHT - interface_height), 2)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if a card is clicked
                for i, card in enumerate(player.deck):
                    card_x = SCREEN_WIDTH // 2 - 280 + i * 160  # Adjusted card positions
                    card_y = SCREEN_HEIGHT - interface_height + 20
                    if card_x <= x <= card_x + 140 and card_y <= y <= card_y + 180:
                        if player.mana >= card.mana_cost:
                            selected_card = card
                            player.mana -= card.mana_cost
                            projectiles.append(Projectile(200, SCREEN_HEIGHT // 3, card.damage))

        # Draw player's health and mana bars in the bottom UI
        draw_bars(50, SCREEN_HEIGHT - interface_height + 20, player.health, 100, RED, "Health", 150)
        draw_bars(300, SCREEN_HEIGHT - interface_height + 20, player.mana, 50, BLUE, "Mana", 400)

        # Draw enemy's health bar in the bottom UI
        draw_bars(SCREEN_WIDTH - 250, SCREEN_HEIGHT - interface_height + 20, enemy.health, 100, RED, "Enemy Health", SCREEN_WIDTH - 150)

        # Draw player as a square in the top half, adjusted position
        pygame.draw.rect(screen, BLUE, (300, SCREEN_HEIGHT // 3 - 50, 100, 100))

        # Draw enemy as a triangle in the top half, adjusted position
        pygame.draw.polygon(screen, RED, [
            (SCREEN_WIDTH - 300, SCREEN_HEIGHT // 3 - 50),
            (SCREEN_WIDTH - 250, SCREEN_HEIGHT // 3 + 50),
            (SCREEN_WIDTH - 350, SCREEN_HEIGHT // 3 + 50)
        ])

        # Draw cards in the bottom half
        for i, card in enumerate(player.deck):
            card.draw(SCREEN_WIDTH // 2 - 280 + i * 160, SCREEN_HEIGHT - interface_height + 20)

        # Handle projectiles
        for projectile in projectiles[:]:
            projectile.move()
            projectile.draw()
            if projectile.x >= SCREEN_WIDTH - 200:
                enemy.health -= projectile.damage
                projectiles.remove(projectile)

        # Check for victory or defeat
        if enemy.health <= 0:
            win_text = FONT.render("You Win!", True, GREEN)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if player.health <= 0:
            lose_text = FONT.render("You Lose!", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        # Update the screen
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
