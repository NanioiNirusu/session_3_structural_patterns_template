# Import the pygame library
import pygame

# Import the WindowGame class from the views.windows.WindowGame module
from views.windows.WindowGame import WindowGame

# Initialize all imported pygame modules
pygame.init()

# Create an instance of the WindowGame class, which likely represents 
# the main game window or menu
window_menu = WindowGame()

# Call the show() method on the window_menu object
# This likely displays the game window or menu on the screen
window_menu.show()
