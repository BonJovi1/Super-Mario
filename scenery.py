import random
import os
from colorama import init, Fore
init()

class Scenery:
	'''This class defines and puts all the clouds, bricks etc onto the grid'''
	
	def __init__(self):
		# self.cloud = [ ["(", "-", ")"], ["(", "_", ")"] ]
		
		self.__tunnel = [ ("-", "-", "-", "-", "-"), ("-", "-", "-", "-", "-"), 
						("-", "-", "-", "-", "-"), ("-", "-", "-", "-", "-"), 
						("-", "-", "-", "-", "-") ] 

		# self.cloud2 = [ [" ", "(", "-", "-", ")", " "], ["(", "-", "~", "-", "~", ")"], 
		# 				[" ", "(", "-", "-", ")", " "] ]

		self.__cloud = []
		self.__tunnel = []
		self.__brick = []
		self.__mountain = []
		self.spring = Fore.RED + "j" + '\x1b[0m'
		self.__sky = Fore.CYAN + "X" + '\x1b[0m'
		self.brick_score = 5
		self.__ground1 = Fore.MAGENTA + "T" + '\x1b[0m'
		

	def create_ground(self, grid):
		for i in range(500):
			grid[29][i]= self.__ground1
			grid[28][i]= "-"

	def create_sky(self,grid):
		for i in range(500):
			grid[0][i]=self.__sky

	def create_clouds(self,grid,c,d):
		with open("./background/cloud3.txt") as obj:
			for line in obj:
				self.__cloud.append(line.strip('\n'))

		while(d<271): # scenery1: we show clouds till column no. 270
			e=d
			f=c
			for i in range(4):
				for j in range(16):
					grid[c][d] = self.__cloud[i][j]
					d+=1
				d=e
				c+=1
			c=f +random.randint(0,2)
			d += 37 + random.randint(10,50) 

	def create_tunnels(self,grid,c,d):
		with open("./background/tunnel.txt") as obj:
			for line in obj:
				self.__tunnel.append(line.strip('\n'))

		while(d<360):
			e=d
			f=c
			for i in range(5):
				for j in range(13):
					grid[c][d] = self.__tunnel[i][j]
					d+=1
				d=e
				c+=1
			c=f
			d+=70 

	def create_bricks(self,grid,c,d):
		with open("./background/brick.txt") as obj:
			for line in obj:
				self.__brick.append(line.strip('\n'))

		while(d<360):
			e=d
			f=c
			for i in range(len(self.__brick)):
				for j in range(len(self.__brick[1])):
					if(i==2 and j==5):
						grid[c][d] = self.brick_score
					else:
						grid[c][d] = self.__brick[i][j]
					d+=1
				d=e
				c+=1
			c=f
			d+=70 

	def create_mountain(self,grid,c,d):
		with open("./background/mountain.txt") as obj:
			for line in obj:
				self.__mountain.append(line.strip('\n'))
		e=d
		for i in range(10):
			for j in range(68):
				grid[c][d] = self.__mountain[i][j]
				d+=1
			d=e
			c+=1

	def create_holes(self, obj_board):
		for i in range (40,45):
			obj_board.matrix[28][i] = " "
		for i in range (290,295):
			obj_board.matrix[28][i] = " "
		for i in range (323,328):
			obj_board.matrix[28][i] = " "
		for i in range (360,365):
			obj_board.matrix[28][i] = " "



	def create_springs(self, obj_board):
		
		obj_board.matrix[27][55] = self.spring 
		obj_board.matrix[27][195] = self.spring 

	def create_coins_platforms(self, obj_board):
		for i in range(115,130):
			obj_board.matrix[23][i] = "-"
		for i in range(115,130):
			obj_board.matrix[27][i] = "$"
		
		for i in range (320,334):
			obj_board.matrix[23][i] = "-"
		for i in range(320,334):
			obj_board.matrix[27][i] = "$"


	def put_barrier(self,grid):
		for i in range(30):
			grid[i][492] = '|'

	def remove_barrier(self,grid):
		for i in range(2,28):
			grid[i][492] = " "




				

		

