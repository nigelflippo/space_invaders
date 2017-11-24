import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien"""

	def __init__(self, ai_settings, screen):
		"""Initialize alien and set starting position"""
		super(Alien, self).__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		# Load the alien and set its rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien towards the top of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's position
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the alien at its current position"""
		self.screen.blit(self.image, self.rect)