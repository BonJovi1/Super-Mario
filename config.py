import os
class Config:
	'''Miscellaneous Stuff '''
	def __init__(self):
		self.rem = 150
		self.coins =0 
		self.kills = 0 

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			pass
	 
		try:
			import unicodedata
			unicodedata.numeric(s)
			return True
		except (TypeError, ValueError):
			pass

		return False

	def coins_right(self, grid, obj_mario):
		if (grid[obj_mario.ycoo + 2][obj_mario.xcoo + 3] == "$"):
			self.coins += 1
			os.system('afplay ./music/coin.wav&')

	def coins_left(self, grid, obj_mario):
		if (grid[obj_mario.ycoo + 2][obj_mario.xcoo - 1] == "$"):
			self.coins += 1
			os.system('afplay ./music/coin.wav&')

	def check_brick_collision(self, obj_scenery, obj_board, obj_mario):
		
		if obj_scenery.brick_score == 0:
			os.system('afplay ./music/bump.wav&')
		
		elif(self.is_number(obj_board.matrix[obj_mario.ycoo-2][obj_mario.xcoo+1]) == True):
			if( obj_board.matrix [obj_mario.ycoo-2] [obj_mario.xcoo+1] > 0):
				
				obj_board.matrix[obj_mario.ycoo-2][obj_mario.xcoo+1] -= 1
				
				os.system('afplay ./music/brick.wav&')
				self.coins += 1


