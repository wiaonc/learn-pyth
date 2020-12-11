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
		#现在的按钮还很丑 待优化
		self.history_image = pygame.image.load('images/history.webp')
		self.history_size = pygame.transform.scale(self.history_image,(int(self.screen_rect.right / 5), int(self.screen_rect.bottom / 10)))
		
		self.play_image = pygame.image.load('images/play.webp')
		self.play_size = pygame.transform.scale(self.play_image,(int(self.screen_rect.right / 5), int(self.screen_rect.bottom / 10)))
		
		self.historybg_image = pygame.image.load('images/historybg.webp')
		self.historybg_size = pygame.transform.scale(self.historybg_image,(int(self.screen_rect.right / 2.4), int(self.screen_rect.bottom / 1.2)))

		self.history_rect = self.history_size.get_rect()
		self.play_rect = self.play_size.get_rect()
		self.historybg_rect = self.historybg_size.get_rect()
		
		self.play_rect.bottom = self.screen_rect.bottom / 2
		self.play_rect.right = self.screen_rect.right / 2 +120
		self.history_rect.bottom = self.play_rect.bottom + self.screen_rect.bottom / 10 + 1
		self.history_rect.right = self.play_rect.right
		self.historybg_rect.center = self.screen_rect.center
		

		# 按钮的标签只需创建一次
		self.prep_msg(msg)
		self.prep_msg1(msg1)
		self.prep_reset()
		self.prep_return()
	def prep_msg(self,msg):
		"""将msg渲染为图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg, True, self.button_color,None)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.play_rect.center

	def prep_msg1(self,msg1):
		self.msg_image1 = self.font.render(msg1, True, self.button_color,None)
		self.msg_image_rect1 = self.msg_image1.get_rect()
		self.msg_image_rect1.center = self.history_rect.center
	def draw_button(self):
		# 绘制一个用图片填充的按钮
		self.screen.blit(self.play_size, self.play_rect)
		self.screen.blit(self.history_size, self.history_rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		self.screen.blit(self.msg_image1, self.msg_image_rect1)
	def prep_reset(self):
		#绘制一个按钮
		self.reset = self.font1.render('reset', True, (240, 244, 230),
		self.text_color)
		self.reset_rect = self.reset.get_rect()
		self.reset_rect.left = self.historybg_rect.left + 10
		self.reset_rect.bottom = self.historybg_rect.bottom - 10
	def prep_return(self):
		self.returns = self.font1.render('return', True, (240, 244, 230),
		self.text_color)
		self.returns_rect = self.returns.get_rect()
		self.returns_rect.right = self.historybg_rect.right - 10
		self.returns_rect.bottom = self.historybg_rect.bottom - 10
	def prep_history_score(self):
		self.screen.blit( self.historybg_size, self.historybg_rect)
		self.screen.blit(self.reset,self.reset_rect)
		self.screen.blit(self.returns,self.returns_rect)

