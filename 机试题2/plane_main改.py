import pygame
from plane_sprites改 import *

pygame.mixer.init()

pygame.mixer.music.load("/home/share/Beyond-不再犹豫.mp3")

pygame.mixer.music.play()


class MenWeiJia_PlaneGame(object):

	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREAT_ENEMY_EVENT,500)
		pygame.time.set_timer(HERO_FIRE_EVENT,200)

	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()

	def __create_sprites(self):
			bg1 = MenWeiJia_Background()
			bg2 = MenWeiJia_Background(True)
			#bg2.rect.y = bg2.rect.height
			self.back_group = pygame.sprite.Group(bg1,bg2)
			self.enemy_group = pygame.sprite.Group()
			self.hero = MenWeiJia_Hero()
			
			self.hero_group = pygame.sprite.Group(self.hero)
			
			
			
	def __event_handler(self):
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				MenWeiJia_PlaneGame.__game_over()

			elif event.type == CREAT_ENEMY_EVENT:
				enemy = MenWeiJia_Enemy()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.hero.up = True				
					
				elif event.key == pygame.K_DOWN:
					self.hero.down = True
				elif event.key == pygame.K_LEFT:
					self.hero.left = True
				elif event.key == pygame.K_RIGHT:
					self.hero.right = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.hero.up = False				
					
				elif event.key == pygame.K_DOWN:
					self.hero.down = False
				elif event.key == pygame.K_LEFT:
					self.hero.left = False
				elif event.key == pygame.K_RIGHT:
					self.hero.right = False
			

	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullets_group,self.enemy_group,True,True)
		self.enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

		if len(self.enemies) > 0:
			self.hero.kill()
			
			MenWeiJia_PlaneGame.__game_over()
		

	def __update_sprites(self):
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets_group]:
			group.update()
			group.draw(self.screen)

	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()

if __name__ == "__main__":
	game = MenWeiJia_PlaneGame()
	game.start_game()