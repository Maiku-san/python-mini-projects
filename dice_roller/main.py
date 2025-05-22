import pygame
import sys
from button import Button
from dice_roller import DiceRoller

# Init Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (70, 70, 70)
BUTTON_HOVER_COLOR = (100, 100, 100)
BUTTON_SELECTED_COLOR = (0, 150, 0)

# Screen and font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Dice manager
roller = DiceRoller()
buttons = []

# Dice type buttons
start_x, start_y, gap = 50, 150, 10
button_width, button_height = 70, 40

for i, die_name in enumerate(roller.dice_types):
    x = start_x + (i % 4) * (button_width + gap)
    y = start_y + (i // 4) * (button_height + gap)
    def make_callback(dn=die_name):
        return lambda: roller.select_die(dn)
    buttons.append(Button(die_name, x, y, button_width, button_height, make_callback()))

# Count buttons
buttons.append(Button("+", 420, 150, 40, 40, roller.increase_count))
buttons.append(Button("-", 470, 150, 40, 40, roller.decrease_count))

# Roll button
buttons.append(Button("Roll", 420, 250, 90, 40, roller.roll))

# Exit button
def exit_program():
    pygame.quit()
    sys.exit()

buttons.append(Button("Exit", WIDTH - 100, HEIGHT - 60, 80, 40, exit_program))

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    # Title
    title = font.render("Dice Roller", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Dice count
    count_label = small_font.render(f"Number of dice: {roller.num_dice}", True, WHITE)
    screen.blit(count_label, (420, 200))

    # Buttons
    for button in buttons:
        is_selected = (
            roller.selected_die is not None and 
            button.text == roller.selected_die.name
        )
        button.draw(
            screen,
            small_font,
            BUTTON_COLOR,
            BUTTON_HOVER_COLOR,
            WHITE,
            selected=is_selected,
            selected_color=BUTTON_SELECTED_COLOR
        )

    # Roll results
    if roller.roll_results:
        if isinstance(roller.roll_results[0], int):
            result_text = f"Results: {', '.join(map(str, roller.roll_results))}"
        else:
            result_text = roller.roll_results[0]
        result_surface = small_font.render(result_text, True, WHITE)
        screen.blit(result_surface, (50, 320))

    pygame.display.flip()

pygame.quit()
sys.exit()