import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at ship's position"""
		# Child class will make call to parent class using super
		super().__init__()

		self.screen = screen

		# Create a bullet rect and set position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the bullet's position as a decimal
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""Move the bullet"""
		# Update decimal position
		self.y -= self.speed_factor
		# Update rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
