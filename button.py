import pygame.font
from scoreboard import Scoreboard as sb

class Button():
	def __init__(self, ai_settings , screen ,stats, msg,msg1):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
#		self.sb = Scoreboard(ai_settings, screen, stats,play_button)
		# 设置按钮的尺寸和其他属性
		self.width, self.height = 240, 60
		self.button_color = (66, 44, 33)
		self.text_color = (255, 200, 255)
		self.font = pygame.font.SysFont(None, 32)
		self.font1 = pygame.font.SysFont(None, 52)
		# 创建按钮的rect对象，并使其居中
		self.rect = pygame.Rect(0, 0, self.screen_rect.right / 5, self.screen_rect.bottom / 10)
		self.rect1 = pygame.Rect(0, 0, self.screen_rect.right / 5, self.screen_rect.bottom / 10)
		self.rect2 = pygame.Rect(0, 0, self.screen_rect.right / 2.4, self.screen_rect.bottom / 1.2)
		#self.rect.center = self.screen_rect.center
		self.rect.bottom = self.screen_rect.bottom / 2
		self.rect.right = self.screen_rect.right / 2 +120
		self.rect1.bottom = self.rect.bottom + self.screen_rect.bottom / 10 + 1
		self.rect1.right = self.rect.right
		self.rect2.center = self.screen_rect.center
		

		# 按钮的标签只需创建一次
		self.prep_msg(msg)
		self.prep_msg1(msg1)
		self.prep_reset()
		self.prep_return()
	def prep_msg(self,msg):
		"""将msg渲染为图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg, True, self.text_color,
		self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		#self.msg_image_rect.bottom = self.rect.bottom
		#self.msg_image_rect.right = self.rect.right
		self.msg_image_rect.center = self.rect.center

	def prep_msg1(self,msg1):
		self.msg_image1 = self.font.render(msg1, True, self.text_color,
		self.button_color)
		self.msg_image_rect1 = self.msg_image1.get_rect()
		self.msg_image_rect1.center = self.rect1.center
	def draw_button(self):
		# 绘制一个用颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color, self.rect)
		self.screen.fill(self.button_color, self.rect1)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		self.screen.blit(self.msg_image1, self.msg_image_rect1)
	def prep_reset(self):
		#绘制一个按钮
		self.reset = self.font1.render('reset', True, (240, 244, 230),
		self.text_color)
		self.reset_rect = self.reset.get_rect()
		self.reset_rect.left = self.rect2.left + 10
		self.reset_rect.bottom = self.rect2.bottom - 10
	def prep_return(self):
		self.returns = self.font1.render('return', True, (240, 244, 230),
		self.text_color)
		self.returns_rect = self.returns.get_rect()
		self.returns_rect.right = self.rect2.right - 10
		self.returns_rect.bottom = self.rect2.bottom - 10
	def prep_history_score(self):
		self.screen.fill((240, 244, 230), self.rect2)
		self.screen.blit(self.reset,self.reset_rect)
		self.screen.blit(self.returns,self.returns_rect)

