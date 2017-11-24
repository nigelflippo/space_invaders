import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to key presses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		

def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to key presses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Movement
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""Fire a bullet if limit not yet reached"""
	# Create a bullet and add it to group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def update_bullets(bullets):
	"""Update position of bullets and remove bullets"""
	# Update bullet position
	bullets.update()

	# Delete bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
	"""Create a full fleet of aliens"""
	# Create an alien and find the number of aliens in a row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	# Create the first row of aliens
	for alien_number in range(number_aliens_x):
		# Create an alien and place it in the row
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)

def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""Update images on the screen and flip to the new screen"""
	# Redraw screen each time
	screen.fill(ai_settings.bg_color)
	# Redraw bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# Draw sprites
	ship.blitme()
	aliens.draw(screen)

	# Display most recently drawn version of screen
	pygame.display.flip()