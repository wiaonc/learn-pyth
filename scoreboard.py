import pygame.font
from pygame.sprite import Group
from ship import Ship
import json
import os
import time

class Scoreboard():
	"""显示得分信息的类"""
	def __init__(self, ai_settings, screen, stats,play_button):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		self.play_button = play_button
		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 32)
		self.dts ={}
		# 准备包含最高得分和当前得分的图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		self.load_file()
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		rounded_score = round(self.stats.score, -1)
		score_str =  'score:'+str("{:,}".format(rounded_score))
		self.score_image = self.font.render(score_str, True,
		self.text_color, None)
		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	def show_score(self):
		"""在屏幕上显示飞船和得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# 绘制飞船
		self.ships.draw(self.screen)
	def prep_high_score(self):
		"""将最高得分转换为渲染的图像"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = 'history high score:'+str("{:,}".format(high_score))
		self.high_score_image = self.font.render(high_score_str, True, 
		self.text_color, None)
		#将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
	def prep_level(self):
		"""将等级转换为渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level), True, 
		self.text_color, None)
		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	def prep_ranking(self):
		#ranking = int(round(self.stats.high_score, -1))
		#high_score = 'history high score:'+str("{:,}".format(high_score))
		self.rankingx = pygame.image.load('1212.png')#获取图片
		self.ranking = pygame.transform.scale(self.rankingx,(500,120))#更改图片像素，
		self.ranking_rect = self.ranking.get_rect()
		self.ranking_rect.right = self.play_button.rect2.right
		self.ranking_rect.bottom = self.play_button.rect2.bottom
		
		self.high_score_ranking = self.font.render('1', True, 
		self.text_color, None)
		#将最高得分放在屏幕顶部中央
		self.score_ranking_rect = self.high_score_ranking.get_rect()
		
		self.score_ranking_rect.center = self.ranking_rect.center
		
		self.screen.blit(self.ranking, self.ranking_rect)
		
		self.screen.blit(self.high_score_ranking, self.score_ranking_rect)

	def dump_file(self):
#		if not os.path.exists('data'):#检查 该目录没有data文件
#			os.mkdir("data")#创建data文件
		'''这里换成异常检查文件是否存在似乎更好'''
		times = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
		history = [{'times':times,'scores':self.stats.high_score}]
		hsty = {'times':times,'scores':self.stats.high_score}
		self.data = []
		for d in self.datas:
			#下面这段在for循环中修改字典耗费了我好多时间才写出来。
			#原因就是还不太了解字典的属性，以及对逻辑不熟悉
			#dx={k:v for k,v in d.items() if int(k)==self.stats.high_score}#这段还不知道怎么使用，但是如果用起来肯定是更简洁的

			#self.ds={x:y for x,y in d.items()}
			#循环遍历字典
			for key,value in d.items():
				self.d ={}
				if int(key) == int(self.stats.high_score):
					#如果遍历的键和本局分数相同则值再添加一个值（这里的值是列表状态，所以不会影响字典大小）
					value.append(hsty)
					#再通过修改键值的方式传递给self。dts（应该是只要不添加新键值就没问题）
					d[key] = value
					self.dts = d
					break
				elif int(key) != int(self.stats.high_score):
					#如果键不同就传递原来的键值给self。dts，并且新的属性赋值一个新字典
					self.dts = d
					self.d=history
			if not d.keys():
				#如果字典是空的就赋值（这项目的是为了防止刚创建文本的时候字典没有数据会导致错误）
				d[self.stats.high_score] = history
				self.dts = d
			elif self.d:
				#如果self。d有值就添加到self。dts字典里（字典d没有新纪录的键就会导致self。d有个新字典值）
				self.dts[self.stats.high_score] =self.d
			break
		self.data.append(self.dts)
		with open ('data\historyscore.json','w') as score:
			json.dump(self.data,score)
	def load_file(self):
		try:
			self.datas=[]
			with open ('data\historyscore.json','r') as score:
				self.datas = json.load(score)
			print('load')
			print(self.datas)
		except FileNotFoundError:
			if not os.path.exists('data'):#检查 该目录没有data文件
				os.mkdir("data")
			#写入json文件，由于第一次写入json数据没有文件提供储存，所以下面要重新执行读取验证文件
			self.dump_file()
			#重新读取文件，以便创建好基础json数据
			self.load_file()
		else:
			pass
	def history_score(self):
		pass
		#self.load_file()
		#self.s = []
		#for sc in self.datas:
			
			#for s in max(int(sc['scores'])):
		#	print(sc)
		
