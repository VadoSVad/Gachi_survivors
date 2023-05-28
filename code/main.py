import pygame, sys
from settings import *
from level import Level
from player import Player


class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		pygame.display.set_caption('Gachi_Survivor')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound
		main_sound = pygame.mixer.Sound('../audio/main.mp3')
		main_sound.set_volume(0.2)
		main_sound.play(loops=-1)



	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)




if __name__ == '__main__':
	game = Game()
	game.run()