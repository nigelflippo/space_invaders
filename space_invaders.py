import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	"""initialize pygame, settings, and screen"""	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Invaders")
	#make a ship
	ship = Ship(screen)

	# bg_color = ai_settings.bg_color
	#start the main game loop
	while True:
		#redraw screen each time
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		for event in pygame.event.get():
			if event == pygame.QUIT:
				sys.exit()
		#display most recently drawn version of screen
		pygame.display.flip()
run_game()

