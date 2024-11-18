import pygame
import random

# window and grid size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 512
GRID_SIZE = 32
GRID_COLS = 20
GRID_ROWS = 16


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        # initial mole position in the top left corner
        mole_x, mole_y = 0, 0

        # game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_x, mole_y, GRID_SIZE, GRID_SIZE)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_x = random.randrange(0, GRID_COLS) * GRID_SIZE
                        mole_y = random.randrange(0, GRID_ROWS) * GRID_SIZE

            screen.fill("light green")

            for x in range(0, WINDOW_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, WINDOW_HEIGHT))
            for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, "black", (0, y), (WINDOW_WIDTH, y))

            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
