from colorama import init, Fore
init()
import os

class Main_person:
	def __init__(self,ycoo,xcoo,dire):
		self.xcoo = xcoo
		self.ycoo = ycoo
		self.direction = dire

class Enemy(Main_person):
	
	def __init__(self, ycoo, xcoo, dire):
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.__shape = [ ["@", "@"], ["@", "@"] ]
		self.allowed_collision = [ " " ]
		self.hit_with_mario = [ "^" ]
		self.killed = 0

	def starting_position(self, grid):
		for i in range(self.ycoo,self.ycoo+2):
			for j in range(self.xcoo,self.xcoo+2):
				grid[i][j] = self.__shape[i-self.ycoo][j-self.xcoo]


	def disappear_enemy(self, grid):
		for i in range(self.ycoo, self.ycoo+2, 1):
			for j in range(self.xcoo, self.xcoo+2, 1):
				grid[i][j] = " "

	def reappear_enemy(self, grid):
		for i in range(self.ycoo, self.ycoo + 2, 1):
			for j in range(self.xcoo, self.xcoo + 2, 1):
				grid[i][j] = self.__shape[i - self.ycoo][j - self.xcoo]


	def move(self,obj_board,obj_mario):
		
		# check collision
		if(self.direction == 1): # towards the right

			if(obj_board.matrix[self.ycoo + 1][self.xcoo + 2] in self.allowed_collision):
				self.disappear_enemy(obj_board.matrix)
				self.xcoo += 1 
				self.reappear_enemy(obj_board.matrix)

			elif( obj_board.matrix[self.ycoo + 1][self.xcoo + 2] in self.hit_with_mario or 
				  obj_board.matrix[self.ycoo + 1][self.xcoo - 1] in self.hit_with_mario ):
				obj_mario.life -= 1
				os.system('afplay ./music/mario_dies.wav&')
				obj_board.spawn_mario(obj_mario)
				# obj_mario.did_he_die = 0
			
			else:
				self.direction = -1 # reverse the direction!
				self.disappear_enemy(obj_board.matrix)
				self.xcoo -= 1

				self.reappear_enemy(obj_board.matrix)
		
		else: #towards the left
			if(obj_board.matrix[self.ycoo + 1][self.xcoo - 1] in self.allowed_collision):
				self.disappear_enemy(obj_board.matrix)
				self.xcoo -= 1 
				self.reappear_enemy(obj_board.matrix)

			elif(obj_board.matrix[self.ycoo + 1][self.xcoo - 1] in self.hit_with_mario or 
				obj_board.matrix[self.ycoo + 1][self.xcoo + 2] in self.hit_with_mario):
				
				obj_mario.life -= 1
				os.system('afplay ./music/mario_dies.wav&')
				obj_board.spawn_mario(obj_mario)

			
			else:
				self.direction = 1 #reverse direction
				self.disappear_enemy(obj_board.matrix)
				self.xcoo += 1
				self.reappear_enemy(obj_board.matrix)
		
		return 0


class BossEnemy(Main_person):
	def __init__(self, ycoo, xcoo, dire):
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.boss_type = 1
		self.boss_kill = False
		self.boss_life = 5
		self.boss = []
		self.boss_abduct = []

	def put_boss(self,grid):
		c=self.ycoo
		d=self.xcoo
		with open("./background/boss.txt") as obj:
			for line in obj:
				self.boss.append(line.strip('\n'))
		e=d
		for i in range(17):
			for j in range(37):
				grid[c][d] = self.boss[i][j]
				d+=1
			d=e
			c+=1 

	def remove_boss(self,grid):

		for i in range(self.ycoo, self.ycoo+17):
			for j in range(self.xcoo, self.xcoo + 37):
				grid[i][j] = " "

	def put_boss_abduct(self,grid):
		if(self.xcoo == 455):
			self.direction = -1

		elif(self.xcoo == 430):
			self.direction = 1
		self.xcoo += self.direction

		c=self.ycoo
		d=self.xcoo
		with open("./background/boss_abduct.txt") as obj:
			for line in obj:
				self.boss_abduct.append(line.strip('\n'))
		e=d
		for i in range(22):
			for j in range(37):
				grid[c][d] = self.boss_abduct[i][j]
				d+=1
			d=e
			c+=1

	def remove_boss_abduct(self,grid):

		for i in range(self.ycoo, self.ycoo+22):
			for j in range(self.xcoo, self.xcoo + 37):
				grid[i][j] = " "

	def check_boss_kill(self, obj_board, obj_mario):
		if(obj_board.matrix[obj_mario.ycoo-6][obj_mario.xcoo+1] == "*"):
			return True
		else:
			return False







			

		

