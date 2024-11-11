import sys
import pygame
from gallery.main import main


if __name__ == "__main__":
    # This will be the main point from where the game will start
    # Initialize pygame
    pygame.init()
    main()
    pygame.quit()
    sys.exit()
