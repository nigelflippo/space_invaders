import pygame
from pygame.sprite import Sprite 

class Star(Sprite):
	"""A class to represent stars"""

	def __init__(self, ai_settings, screen):
		super().__init__()

		self.screen = screen
		self.ai_settings = ai_settings