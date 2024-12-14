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
pygame.display.set_caption("Fantasy Card Game")

# Card class
class Card:
    def __init__(self, name, damage, element):
        self.name = name
        self.damage = damage
        self.element = element

    def draw(self, x, y):
        pygame.draw.rect(screen, WHITE, (x, y, 100, 150))
        text = FONT.render(self.name, True, BLACK)
        screen.blit(text, (x + 5, y + 10))
        dmg_text = FONT.render(f"DMG: {self.damage}", True, BLACK)
        screen.blit(dmg_text, (x + 5, y + 50))
        elem_text = FONT.render(self.element, True, BLACK)
        screen.blit(elem_text, (x + 5, y + 90))

# Player and Enemy classes
class Player:
    def __init__(self):
        self.health = 100
        self.mana = 50
        self.deck = [
            Card("Fireball", 20, "Fire"),
            Card("Water Blast", 15, "Water"),
            Card("Earth Slam", 25, "Earth"),
            Card("Wind Slash", 10, "Wind")
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

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if a card is clicked
                for i, card in enumerate(player.deck):
                    if SCREEN_WIDTH // 2 - 240 + i * 120 <= x <= SCREEN_WIDTH // 2 - 140 + i * 120 and SCREEN_HEIGHT - 200 <= y <= SCREEN_HEIGHT - 50:
                        if player.mana >= 10:
                            selected_card = card
                            player.mana -= 10
                            projectiles.append(Projectile(200, SCREEN_HEIGHT // 2, card.damage))

        # Draw player's health and mana
        health_text = FONT.render(f"Health: {player.health}", True, WHITE)
        screen.blit(health_text, (20, 20))

        mana_text = FONT.render(f"Mana: {player.mana}", True, WHITE)
        screen.blit(mana_text, (20, 70))

        # Draw enemy's health
        enemy_health_text = FONT.render(f"Enemy Health: {enemy.health}", True, RED)
        screen.blit(enemy_health_text, (SCREEN_WIDTH - 250, 20))

        # Draw player as a square
        pygame.draw.rect(screen, BLUE, (100, SCREEN_HEIGHT // 2 - 50, 100, 100))

        # Draw enemy as a triangle
        pygame.draw.polygon(screen, RED, [
            (SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2 - 50),
            (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 + 50),
            (SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2 + 50)
        ])

        # Draw cards
        for i, card in enumerate(player.deck):
            card.draw(SCREEN_WIDTH // 2 - 240 + i * 120, SCREEN_HEIGHT - 200)

        # Handle projectiles
        for projectile in projectiles[:]:
            projectile.move()
            projectile.draw()
            if projectile.x >= SCREEN_WIDTH - 150:
                enemy.health -= projectile.damage
                projectiles.remove(projectile)

        # Check for victory or defeat
        if enemy.health <= 0:
            win_text = FONT.render("You Win!", True, GREEN)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if player.health <= 0:
            lose_text = FONT.render("You Lose!", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        # Update the screen
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
