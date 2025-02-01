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

# Load background image and scale to screen size
background = pygame.image.load("tlo.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load character images and scale to desired size
toady_images = [pygame.image.load(f"toady{i}.png") for i in range(2, 7)]
toady_images = [pygame.transform.scale(img, (120, 120)) for img in toady_images]

freddy_images = [pygame.image.load(f"freddy{i}.png") for i in range(2, 7)]
freddy_images = [pygame.transform.scale(img, (120, 120)) for img in freddy_images]
freddy_images_flipped = [pygame.transform.flip(img, True, False) for img in freddy_images]

# Load toady attack fire images and scale to desired size
toady_af_images = [pygame.image.load(f"toadyaf{i}.png") for i in range(1, 7)]
toady_af_images = [pygame.transform.scale(img, (120, 120)) for img in toady_af_images]

# Load toady attack water images and scale to desired size
toady_aw_images = [pygame.image.load(f"toadyaw{i}.png") for i in range(1, 7)]
toady_aw_images = [pygame.transform.scale(img, (120, 120)) for img in toady_aw_images]

# Load toady attack earth images and scale to desired size
toady_ae_images = [pygame.image.load(f"toadyae{i}.png") for i in range(1, 7)]
toady_ae_images = [pygame.transform.scale(img, (120, 120)) for img in toady_ae_images]

# Frame counter for animation
toady_frame = 0
freddy_frame = 0
toady_af_frame = 0
toady_aw_frame = 0
toady_ae_frame = 0

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
        pygame.draw.rect(screen, WHITE, (x, y, 120, 180))
        text = FONT.render(self.name, True, BLACK)
        screen.blit(text, (x + 5, y + 10))
        elem_text = FONT.render(self.element, True, BLACK)
        screen.blit(elem_text, (x + 5, y + 150))


# Special Card class
class SpecialCard:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def draw(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x, y, 120, 180))
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
        pygame.draw.circle(screen, color, (self.x, self.y), 15)


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

    # Initialize frame counters
    toady_frame = 0
    freddy_frame = 0
    toady_af_frame = 0
    toady_aw_frame = 0
    toady_ae_frame = 0

    # Flags to indicate if FIRE, WATER, or EARTH animation is active
    fire_animation_active = False
    water_animation_active = False
    earth_animation_active = False

    while running:
        screen.fill(BLACK)

        # Draw background
        screen.blit(background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check special card selection
                for i, card in enumerate(special_cards):
                    if 20 + i * 140 <= x <= 140 + i * 140 and SCREEN_HEIGHT - 220 <= y <= SCREEN_HEIGHT - 40:
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
                    if SCREEN_WIDTH // 2 - 280 + i * 140 <= x <= SCREEN_WIDTH // 2 - 160 + i * 140 and SCREEN_HEIGHT - 220 <= y <= SCREEN_HEIGHT - 40:
                        if not player_projectile:
                            player_projectile = Projectile(200, SCREEN_HEIGHT // 2, 10, card.element)
                            enemy_choice = random.choice(player_deck)
                            enemy_projectile = Projectile(SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2, -10,
                                                          enemy_choice.element)
                            if card.element == "Fire":
                                fire_animation_active = True
                                water_animation_active = False
                                earth_animation_active = False
                            elif card.element == "Water":
                                water_animation_active = True
                                fire_animation_active = False
                                earth_animation_active = False
                            elif card.element == "Earth":
                                earth_animation_active = True
                                fire_animation_active = False
                                water_animation_active = False

        # Draw health bars
        player_health_text = FONT.render(f"Player Health: {player_health}", True, WHITE)
        screen.blit(player_health_text, (20, 20))

        enemy_health_text = FONT.render(f"Enemy Health: {enemy_health}", True, WHITE)
        screen.blit(enemy_health_text, (SCREEN_WIDTH - 250, 20))

        # Draw revealed element
        if revealed_element:
            reveal_text = FONT.render(f"Enemy Element: {revealed_element}", True, YELLOW)
            screen.blit(reveal_text, (20, 60))

        # Draw player and enemy images
        if fire_animation_active:
            screen.blit(toady_af_images[toady_af_frame // 5], (100, SCREEN_HEIGHT // 2 - 60))
            toady_af_frame += 1
            if toady_af_frame // 5 >= len(toady_af_images):
                toady_af_frame = 0
                fire_animation_active = False
        elif water_animation_active:
            screen.blit(toady_aw_images[toady_aw_frame // 5], (100, SCREEN_HEIGHT // 2 - 60))
            toady_aw_frame += 1
            if toady_aw_frame // 5 >= len(toady_aw_images):
                toady_aw_frame = 0
                water_animation_active = False
        elif earth_animation_active:
            screen.blit(toady_ae_images[toady_ae_frame // 5], (100, SCREEN_HEIGHT // 2 - 60))
            toady_ae_frame += 1
            if toady_ae_frame // 5 >= len(toady_ae_images):
                toady_ae_frame = 0
                earth_animation_active = False
        else:
            screen.blit(toady_images[toady_frame // 5], (100, SCREEN_HEIGHT // 2 - 60))
            toady_frame = (toady_frame + 1) % (len(toady_images) * 5)

        screen.blit(freddy_images_flipped[freddy_frame // 5], (SCREEN_WIDTH - 180, SCREEN_HEIGHT // 2 - 60))
        freddy_frame = (freddy_frame + 1) % (len(freddy_images_flipped) * 5)

        # Draw special cards
        for i, card in enumerate(special_cards):
            card.draw(20 + i * 140, SCREEN_HEIGHT - 220)

        # Draw elemental cards
        for i, card in enumerate(player_deck):
            card.draw(SCREEN_WIDTH // 2 - 280 + i * 140, SCREEN_HEIGHT - 220)

        # Handle projectiles
        if player_projectile:
            player_projectile.move()
            player_projectile.draw()

        if enemy_projectile:
            enemy_projectile.move()
            enemy_projectile.draw()

        # Check collision
        if player_projectile and enemy_projectile and abs(player_projectile.x - enemy_projectile.x) < 30:
            if ELEMENT_STRENGTHS[player_projectile.element] == enemy_projectile.element:
                enemy_projectile = None
            elif ELEMENT_STRENGTHS[enemy_projectile.element] == player_projectile.element:
                player_projectile = None
            else:
                player_projectile = None
                enemy_projectile = None

        # Check if projectiles hit their target
        if player_projectile and player_projectile.x >= SCREEN_WIDTH - 180:
            damage = 20 if not double_damage else 40
            enemy_health -= damage
            player_projectile = None
            double_damage = False

        if enemy_projectile and enemy_projectile.x <= 180:
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