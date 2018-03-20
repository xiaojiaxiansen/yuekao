import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREAT_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class MenWeiJia_GameSprite(pygame.sprite.Sprite):
	
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y -= self.speed

class MenWeiJia_Background(MenWeiJia_GameSprite):

	def __init__(self,is_alt = False):
		super().__init__("./images/background.png")
		self.rect.y = 0
		if is_alt:
			self.rect.top = self.rect.bottom
	def update(self):
		super().update()
		
class MenWeiJia_Enemy(MenWeiJia_GameSprite):

	def __init__(self):
		super().__init__("./images/enemy1.png")
		self.speed = random.randint(1, 3)
		self.rect.top = 700
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)

	def update(self):
		super().update()
		if self.rect.y < 0:
			print("敌机飞出屏障")
			self.kill()

	def __del__(self):
		print("敌机挂掉了%s"%self.rect)

class MenWeiJia_Hero(MenWeiJia_GameSprite):

	def __init__(self):
		super().__init__("./images/me1.png",0)

		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.top = SCREEN_RECT.top - 120

		self.bullets_group = pygame.sprite.Group()

		self.up = False
		self.down = False
		self.left = False
		self.right = False

	def update(self):
		

		if self.up == True:
			self.rect.y -= 5
		elif self.down == True:
			self.rect.y += 5
		elif self.left == True:
			self.rect.x -= 5
		elif self.right == True:
			self.rect.x += 5

		self.rect.x += self.speed
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		elif self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom	
		
	def fire(self):
		print("发射子弹")

		for i in (1,2,3):
			bullet = MenWeiJia_Bullet()
			bullet.rect.top = self.rect.bottom + 20*i
			bullet.rect.centerx = self.rect.centerx
			self.bullets_group.add(bullet)


class MenWeiJia_Bullet(MenWeiJia_GameSprite):

	def __init__(self):
		super().__init__("./images/bullet1.png",5)
		#super().__init__("./images/bullet2.png",-5)

	def update(self):
		#super().update()
		self.rect.y += self.speed
		if self.rect.bottom > 700:
			self.kill()