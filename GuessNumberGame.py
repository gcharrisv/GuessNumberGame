import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guess the Number with Hangman")

# Set up font
font = pygame.font.Font(None, 36)

# Game variables
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10
input_text = ''
message = "Guess a number between 1 and 100"

# Function to draw hangman
def draw_hangman(attempts):
    # Simple drawing for each stage (up to 10)
    hangman_coords = [
        (400, 500, 10, 100), # base
        (405, 100, 10, 400), # stand
        (405, 100, 100, 10), # top
        (500, 100, 10, 50),  # rope
        # More parts for the hangman...
    ]

    for i in range(attempts):
        if i < len(hangman_coords):
            pygame.draw.rect(screen, (0, 0, 0), hangman_coords[i])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and attempts < max_attempts:
                try:
                    guess = int(input_text)
                    attempts += 1

                    if guess < number_to_guess:
                        message = "Too low. Try again."
                    elif guess > number_to_guess:
                        message = "Too high. Try again."
                    else:
                        message = f"Congratulations! You guessed the number in {attempts} attempts."
                        running = False

                    if attempts >= max_attempts:
                        message = "Game Over. You've reached the maximum attempts."

                except ValueError:
                    message = "Please enter a valid number."
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Fill screen
    screen.fill((255, 255, 255))

    # Draw hangman
    draw_hangman(attempts)

    # Render text
    text_surface = font.render(message, True, (0, 0, 0))
    input_surface = font.render(input_text, True, (0, 0, 0))

    # Blit text to screen
    screen.blit(text_surface, (10, 10))
    screen.blit(input_surface, (10, 50))

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()

