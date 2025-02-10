import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Load and play background music
pygame.mixer.music.load("muzyka.wav")
pygame.mixer.music.set_volume(0.5)  # Set the volume to 50%


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
pygame.display.set_caption("Eligebete")

# Load start screen images and scale them
start_img = pygame.image.load("start.png")
start_img = pygame.transform.scale(start_img, (int(start_img.get_width() // 3), int(start_img.get_height() // 3)))

play_img = pygame.image.load("play.png")
play_img = pygame.transform.scale(play_img, (int(play_img.get_width() // 3), int(play_img.get_height() // 3)))

exit_img = pygame.image.load("exit.png")
exit_img = pygame.transform.scale(exit_img, (int(exit_img.get_width() // 3), int(exit_img.get_height() // 3)))

fire_card_img = pygame.transform.scale(pygame.image.load("kogien.png"), (120, 180))
water_card_img = pygame.transform.scale(pygame.image.load("kwoda.png"), (120, 180))
earth_card_img = pygame.transform.scale(pygame.image.load("kziemia.png"), (120, 180))
reveal_card_img = pygame.transform.scale(pygame.image.load("reveal.png"), (120, 180))
heal_card_img = pygame.transform.scale(pygame.image.load("heal.png"), (120, 180))
double_card_img = pygame.transform.scale(pygame.image.load("double.png"), (120, 180))
toady_images = [pygame.image.load(f"toady{i}.png") for i in range(2, 7)]
toady_images = [pygame.transform.scale(img, (250, 250)) for img in toady_images]
freddy_images = [pygame.image.load(f"freddy{i}.png") for i in range(2, 7)]
freddy_images = [pygame.transform.scale(img, (250, 250)) for img in freddy_images]
freddy_images_flipped = [pygame.transform.flip(img, True, False) for img in freddy_images]


def load_game_assets():
    global background, toady_images, freddy_images, freddy_images_flipped
    global toady_af_images, toady_aw_images, toady_ae_images, toady_death_images
    global freddy_af_images, freddy_aw_images, freddy_ae_images, freddy_death_images
    global fire_card_img, water_card_img, earth_card_img
    global reveal_card_img, heal_card_img, double_card_img
    global toady_fire_projectile_images, toady_water_projectile_images, toady_earth_projectile_images
    global freddy_fire_projectile_images, freddy_water_projectile_images, freddy_earth_projectile_images
# Load background image and scale to screen size
    background = pygame.image.load("tlo.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load character images and scale to desired size (significantly larger)
    toady_images = [pygame.image.load(f"toady{i}.png") for i in range(2, 7)]
    toady_images = [pygame.transform.scale(img, (250, 250)) for img in toady_images]

    freddy_images = [pygame.image.load(f"freddy{i}.png") for i in range(2, 7)]
    freddy_images = [pygame.transform.scale(img, (250, 250)) for img in freddy_images]
    freddy_images_flipped = [pygame.transform.flip(img, True, False) for img in freddy_images]

# Load toady attack fire images and scale to desired size (significantly larger)
    toady_af_images = [pygame.image.load(f"toadyaf{i}.png") for i in range(1, 7)]
    toady_af_images = [pygame.transform.scale(img, (250, 250)) for img in toady_af_images]

# Load toady attack water images and scale to desired size (significantly larger)
    toady_aw_images = [pygame.image.load(f"toadyaw{i}.png") for i in range(1, 7)]
    toady_aw_images = [pygame.transform.scale(img, (250, 250)) for img in toady_aw_images]

# Load toady attack earth images and scale to desired size (significantly larger)
    toady_ae_images = [pygame.image.load(f"toadyae{i}.png") for i in range(1, 7)]
    toady_ae_images = [pygame.transform.scale(img, (250, 250)) for img in toady_ae_images]

# Load toady death images and scale to desired size (significantly larger)
    toady_death_images = [pygame.image.load(f"toadydeath{i}.png") for i in range(1, 14)]
    toady_death_images = [pygame.transform.scale(img, (250, 250)) for img in toady_death_images]

# Load and flip freddy attack fire images (significantly larger)
    freddy_af_images = [pygame.image.load(f"freddy{i}af.png") for i in range(1, 7)]
    freddy_af_images = [pygame.transform.flip(pygame.transform.scale(img, (250, 250)), True, False) for img in freddy_af_images]

# Load and flip freddy attack water images (significantly larger)
    freddy_aw_images = [pygame.image.load(f"freddy{i}aw.png") for i in range(1, 7)]
    freddy_aw_images = [pygame.transform.flip(pygame.transform.scale(img, (250, 250)), True, False) for img in freddy_aw_images]

# Load and flip freddy attack earth images (significantly larger)
    freddy_ae_images = [pygame.image.load(f"freddy{i}ae.png") for i in range(1, 7)]
    freddy_ae_images = [pygame.transform.flip(pygame.transform.scale(img, (250, 250)), True, False) for img in freddy_ae_images]

# Load and flip freddy death images (significantly larger)
    freddy_death_images = [pygame.image.load(f"freddydeath{i}.png") for i in range(1, 14)]
    freddy_death_images = [pygame.transform.flip(pygame.transform.scale(img, (250, 250)), True, False) for img in freddy_death_images]

# Load card images and scale to card size
    fire_card_img = pygame.transform.scale(pygame.image.load("kogien.png"), (120, 180))
    water_card_img = pygame.transform.scale(pygame.image.load("kwoda.png"), (120, 180))
    earth_card_img = pygame.transform.scale(pygame.image.load("kziemia.png"), (120, 180))

# Add the new special card images
    reveal_card_img = pygame.transform.scale(pygame.image.load("reveal.png"), (120, 180))
    heal_card_img = pygame.transform.scale(pygame.image.load("heal.png"), (120, 180))
    double_card_img = pygame.transform.scale(pygame.image.load("double.png"), (120, 180))

# Load projectile animation images for toady and flip them horizontally
<<<<<<< HEAD
    toady_fire_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"o{i}.png"), True, False), (int(pygame.image.load(f"o{i}.png").get_width() * 2), int(pygame.image.load(f"o{i}.png").get_height() * 2))) for i in range(1, 6)]
    toady_water_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"w{i}.png"), True, False), (int(pygame.image.load(f"w{i}.png").get_width() * 2), int(pygame.image.load(f"w{i}.png").get_height() * 2))) for i in range(1, 6)]
    toady_earth_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"z{i}.png"), True, False), (int(pygame.image.load(f"z{i}.png").get_width() * 2), int(pygame.image.load(f"z{i}.png").get_height() * 2))) for i in range(1, 6)]

# Load projectile animation images for freddy (no flip needed)
    freddy_fire_projectile_images = [pygame.transform.scale(pygame.image.load(f"o{i}.png"), (int(pygame.image.load(f"o{i}.png").get_width() * 2), int(pygame.image.load(f"o{i}.png").get_height() * 2))) for i in range(1, 6)]
    freddy_water_projectile_images = [pygame.transform.scale(pygame.image.load(f"w{i}.png"), (int(pygame.image.load(f"w{i}.png").get_width() * 2), int(pygame.image.load(f"w{i}.png").get_height() * 2))) for i in range(1, 6)]
    freddy_earth_projectile_images = [pygame.transform.scale(pygame.image.load(f"z{i}.png"), (int(pygame.image.load(f"z{i}.png").get_width() * 2), int(pygame.image.load(f"z{i}.png").get_height() * 2))) for i in range(1, 6)]
=======
    toady_fire_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"o{i}.png"), True, False), (int(pygame.image.load(f"o{i}.png").get_width() * 2), int(pygame.image.load(f"o{i}.png").get_height() * 3))) for i in range(1, 7)]
    toady_water_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"w{i}.png"), True, False), (int(pygame.image.load(f"w{i}.png").get_width() * 2), int(pygame.image.load(f"w{i}.png").get_height() * 3))) for i in range(1, 7)]
    toady_earth_projectile_images = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"z{i}.png"), True, False), (int(pygame.image.load(f"z{i}.png").get_width() * 2), int(pygame.image.load(f"z{i}.png").get_height() * 3))) for i in range(1, 7)]

# Load projectile animation images for freddy (no flip needed)
    freddy_fire_projectile_images = [pygame.transform.scale(pygame.image.load(f"o{i}.png"), (int(pygame.image.load(f"o{i}.png").get_width() * 2), int(pygame.image.load(f"o{i}.png").get_height() * 3))) for i in range(1, 7)]
    freddy_water_projectile_images = [pygame.transform.scale(pygame.image.load(f"w{i}.png"), (int(pygame.image.load(f"w{i}.png").get_width() * 2), int(pygame.image.load(f"w{i}.png").get_height() * 3))) for i in range(1, 7)]
    freddy_earth_projectile_images = [pygame.transform.scale(pygame.image.load(f"z{i}.png"), (int(pygame.image.load(f"z{i}.png").get_width() * 2), int(pygame.image.load(f"z{i}.png").get_height() * 3))) for i in range(1, 7)]
>>>>>>> 374d77fc5a0480d56f3bd09175d5705bcf9664e3

# Frame counter for animation
toady_frame = 0
freddy_frame = 0
toady_af_frame = 0
toady_aw_frame = 0
toady_ae_frame = 0
freddy_af_frame = 0
freddy_aw_frame = 0
freddy_ae_frame = 0
toady_death_frame = 0
freddy_death_frame = 0

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
        self.image = None
        if element == "Fire":
            self.image = fire_card_img
        elif element == "Water":
            self.image = water_card_img
        elif element == "Earth":
            self.image = earth_card_img

    def draw(self, x, y):
        if self.image:
            screen.blit(self.image, (x, y))

# Special Card class
class SpecialCard:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.image = None
        if name == "Reveal":
            self.image = reveal_card_img
        elif name == "Heal":
            self.image = heal_card_img
        elif name == "Double":
            self.image = double_card_img

    def draw(self, x, y):
        if self.image:
            screen.blit(self.image, (x, y))

# Projectile class
class Projectile:
    def __init__(self, x, y, speed, element, character):
        self.x = x
        self.y = y
        self.speed = speed
        self.element = element
        self.character = character
        self.frame = 0
        if self.character == "toady":
            if self.element == "Fire":
                self.images = toady_fire_projectile_images
            elif self.element == "Water":
                self.images = toady_water_projectile_images
            elif self.element == "Earth":
                self.images = toady_earth_projectile_images
        elif self.character == "freddy":
            if self.element == "Fire":
                self.images = freddy_fire_projectile_images
            elif self.element == "Water":
                self.images = freddy_water_projectile_images
            elif self.element == "Earth":
                self.images = freddy_earth_projectile_images

    def move(self):
        self.x += self.speed

    def draw(self):
        # Draw the current frame of the animation
        screen.blit(self.images[self.frame // 5], (self.x, self.y))
        self.frame = (self.frame + 1) % (len(self.images) * 5)


# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    game_started = False

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
    freddy_af_frame = 0
    freddy_aw_frame = 0
    freddy_ae_frame = 0
    toady_death_frame = 0
    freddy_death_frame = 0

    # Flags to indicate if FIRE, WATER, or EARTH animation is active
    fire_animation_active = False
    water_animation_active = False
    earth_animation_active = False

    # Flags to indicate if Freddy's FIRE, WATER, or EARTH animation is active
    freddy_fire_animation_active = False
    freddy_water_animation_active = False
    freddy_earth_animation_active = False

    # Flags to indicate if death animation is active
    toady_death_animation_active = False
    freddy_death_animation_active = False

    # Flags to indicate if game is over
    game_over = False
    winner = None

    while running:
        screen.fill(BLACK)

        if not game_started:
            # Draw start screen
            screen.blit(start_img, (
            SCREEN_WIDTH // 2 - start_img.get_width() // 2, SCREEN_HEIGHT // 2 - start_img.get_height() // 2 - 150))
            screen.blit(play_img, (
            SCREEN_WIDTH // 2 - play_img.get_width() // 2 - 200, SCREEN_HEIGHT // 2 - play_img.get_height() // 2))
            screen.blit(exit_img, (
            SCREEN_WIDTH // 2 - exit_img.get_width() // 2 + 200, SCREEN_HEIGHT // 2 - exit_img.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if SCREEN_WIDTH // 2 - play_img.get_width() // 2 - 200 <= x <= SCREEN_WIDTH // 2 - play_img.get_width() // 2 - 200 + play_img.get_width() and SCREEN_HEIGHT // 2 - play_img.get_height() // 2 <= y <= SCREEN_HEIGHT // 2 - play_img.get_height() // 2 + play_img.get_height():
                        game_started = True
                        pygame.mixer.music.play(-1)  # Play the music in a loop
                        load_game_assets()
                    if SCREEN_WIDTH // 2 - exit_img.get_width() // 2 + 200 <= x <= SCREEN_WIDTH // 2 - exit_img.get_width() // 2 + 200 + exit_img.get_width() and SCREEN_HEIGHT // 2 - exit_img.get_height() // 2 <= y <= SCREEN_HEIGHT // 2 - exit_img.get_height() // 2 + exit_img.get_height():
                        running = False
        else:
            # Draw background
            screen.blit(background, (0, 0))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    # Jeśli element został ujawniony, każde kolejne kliknięcie go ukrywa
                    if revealed_element:
                        revealed_element = None
                    else:
                        # Sprawdzamy, czy kliknięto kartę "Reveal"
                        for i, card in enumerate(special_cards):
                            if (SCREEN_WIDTH // 2 - 210) + i * 140 <= x <= (
                                    SCREEN_WIDTH // 2 - 90) + i * 140 and 20 <= y <= 200:
                                if card.name == "Reveal" and not special_used["Reveal"]:
                                    revealed_element = random.choice(["Fire", "Water", "Earth"])
                                    special_used["Reveal"] = True

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                # Check special card selection
                for i, card in enumerate(special_cards):
                    if (SCREEN_WIDTH // 2 - 210) + i * 140 <= x <= (SCREEN_WIDTH // 2 - 90) + i * 140 and 20 <= y <= 200:
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
                    if (SCREEN_WIDTH // 2 - 210) + i * 140 <= x <= (SCREEN_WIDTH // 2 - 90) + i * 140 and SCREEN_HEIGHT - 220 <= y <= SCREEN_HEIGHT - 40:
                        if not player_projectile:
                            player_projectile = Projectile(225, SCREEN_HEIGHT - 225, 10, card.element, "toady")
                            enemy_choice = random.choice(player_deck)
                            enemy_projectile = Projectile(SCREEN_WIDTH - 325, SCREEN_HEIGHT - 225, -10, enemy_choice.element, "freddy")
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

                            # Randomly select Freddy's animation based on the element
                            freddy_element = enemy_choice.element
                            if freddy_element == "Fire":
                                freddy_fire_animation_active = True
                                freddy_water_animation_active = False
                                freddy_earth_animation_active = False
                            elif freddy_element == "Water":
                                freddy_water_animation_active = True
                                freddy_fire_animation_active = False
                                freddy_earth_animation_active = False
                            elif freddy_element == "Earth":
                                freddy_earth_animation_active = True
                                freddy_fire_animation_active = False
                                freddy_water_animation_active = False

        if game_started:
            # Draw health bars
            player_health_text = FONT.render(f"Player Health: {player_health}", True, WHITE)
            screen.blit(player_health_text, (50, 20))

            enemy_health_text = FONT.render(f"Enemy Health: {enemy_health}", True, WHITE)
            screen.blit(enemy_health_text, (SCREEN_WIDTH - 250, 20))

        # Draw revealed element
        if revealed_element:
            reveal_text = FONT.render(f"Enemy Element: {revealed_element}", True, YELLOW)
            screen.blit(reveal_text, (SCREEN_WIDTH // 2 - 60, 250))

        if game_started:
            # Draw player and enemy images
            player_y_pos = SCREEN_HEIGHT - 300  # Y position for the player
            enemy_y_pos = SCREEN_HEIGHT - 300  # Y position for the enemy

            player_x_pos = 100  # X position for the player
            enemy_x_pos = SCREEN_WIDTH - 350  # X position for the enemy

            if player_health <= 0:
                toady_death_animation_active = True
                game_over = True
                winner = "freddy"
            if enemy_health <= 0:
                freddy_death_animation_active = True
                game_over = True
                winner = "toady"

            if toady_death_animation_active:
                screen.blit(toady_death_images[toady_death_frame // 5], (player_x_pos, player_y_pos))
                toady_death_frame += 1
                if toady_death_frame // 5 >= len(toady_death_images):
                    toady_death_frame = 0
                    toady_death_animation_active = False
                    if winner == "freddy":
                        lose_text = FONT.render("You Lose!", True, RED)
                        screen.blit(lose_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running = False
            elif fire_animation_active:
                screen.blit(toady_af_images[toady_af_frame // 5], (player_x_pos, player_y_pos))
                toady_af_frame += 1
                if toady_af_frame // 5 >= len(toady_af_images):
                    toady_af_frame = 0
                    fire_animation_active = False
            elif water_animation_active:
                screen.blit(toady_aw_images[toady_aw_frame // 5], (player_x_pos, player_y_pos))
                toady_aw_frame += 1
                if toady_aw_frame // 5 >= len(toady_aw_images):
                    toady_aw_frame = 0
                    water_animation_active = False
            elif earth_animation_active:
                screen.blit(toady_ae_images[toady_ae_frame // 5], (player_x_pos, player_y_pos))
                toady_ae_frame += 1
                if toady_ae_frame // 5 >= len(toady_ae_images):
                    toady_ae_frame = 0
                    earth_animation_active = False
            else:
                screen.blit(toady_images[toady_frame // 5], (player_x_pos, player_y_pos))
                toady_frame = (toady_frame + 1) % (len(toady_images) * 5)

            if freddy_death_animation_active:
                screen.blit(freddy_death_images[freddy_death_frame // 5], (enemy_x_pos, enemy_y_pos))
                freddy_death_frame += 1
                if freddy_death_frame // 5 >= len(freddy_death_images):
                    freddy_death_frame = 0
                    freddy_death_animation_active = False
                    if winner == "toady":
                        win_text = FONT.render("You Win!", True, GREEN)
                        screen.blit(win_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running = False
            elif freddy_fire_animation_active:
                screen.blit(freddy_af_images[freddy_af_frame // 5], (enemy_x_pos, enemy_y_pos))
                freddy_af_frame += 1
                if freddy_af_frame // 5 >= len(freddy_af_images):
                    freddy_af_frame = 0
                    freddy_fire_animation_active = False
            elif freddy_water_animation_active:
                screen.blit(freddy_aw_images[freddy_aw_frame // 5], (enemy_x_pos, enemy_y_pos))
                freddy_aw_frame += 1
                if freddy_aw_frame // 5 >= len(freddy_aw_images):
                    freddy_aw_frame = 0
                    freddy_water_animation_active = False
            elif freddy_earth_animation_active:
                screen.blit(freddy_ae_images[freddy_ae_frame // 5], (enemy_x_pos, enemy_y_pos))
                freddy_ae_frame += 1
                if freddy_ae_frame // 5 >= len(freddy_ae_images):
                    freddy_ae_frame = 0
                    freddy_earth_animation_active = False
            else:
                screen.blit(freddy_images_flipped[freddy_frame // 5], (enemy_x_pos, enemy_y_pos))
                freddy_frame = (freddy_frame + 1) % (len(freddy_images_flipped) * 5)

        if game_started:
            # Draw special cards
            for i, card in enumerate(special_cards):
                if not special_used[card.name]:
                    card.draw((SCREEN_WIDTH // 2 - 210) + i * 140, 20)

            # Draw elemental cards
            for i, card in enumerate(player_deck):
                card.draw((SCREEN_WIDTH // 2 - 210) + i * 140, SCREEN_HEIGHT - 220)

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

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
