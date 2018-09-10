import os
class Board:
	'''This class creates the grid for the game, and displays it'''
	
	def __init__(self, rows, columns): # initialize values
		self.rows = rows
		self.columns = columns
		self.matrix = []

	def create_board(self): # creates the entire grid

		for i in range (self.rows): #rows                              
			self.new = []                 
			for j in range (self.columns): #columns  
				self.new.append(" ")      
			self.matrix.append(self.new)

	def theyllprintit(self, a): # A reference to the Three Days of the Condor :P
		if(a==0): #the grid doesn't move in the beginning
			for i in range(self.rows):
				for j in range(a,a+110): # 110 columns at a time
					print(self.matrix[i][j],end='')
				print()
		
		elif(a == 444): # the grid stops moving from columns 444 to 499
			for i in range(self.rows):
				for j in range(444-55, 444+55): # 110 columns at a time
					print(self.matrix[i][j],end='')
				print()

		else:  # Now it starts moving!
			for i in range(self.rows):
				for j in range(a-55, a+55): # 110 columns at a time
					print(self.matrix[i][j],end='')
				print()

	def spawn_mario(self, obj_mario): # Spawns Mario after he dies

		obj_mario.disappear_mario(self)
						
		obj_mario.ycoo -= 14
		obj_mario.xcoo -= 5

		obj_mario.reappear_mario(self)

	def jump_higher(self, obj_mario):

		obj_mario.disappear_mario(self)
		obj_mario.ycoo -= 16
		obj_mario.reappear_mario(self)

		
