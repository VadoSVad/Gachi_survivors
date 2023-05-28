import pygame
from settings import *
from random import randint

class MagicPlayer:
	def __init__(self,animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'heal': pygame.mixer.Sound('../audio/heal.wav')
		}

	def heal(self,player,strength,cost,groups):
		if player.energy >= cost:
			self.sounds['heal'].play()
			player.health += strength
			player.energy -= cost
			if player.health >= player.stats['health']:
				player.health = player.stats['health']
			self.animation_player.create_particles('aura',player.rect.center,groups)
			self.animation_player.create_particles('heal',player.rect.center,groups)

