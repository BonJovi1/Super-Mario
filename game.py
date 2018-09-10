import signal
import os
import time
from colorama import init, Fore
init()

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from mario import Mario 
from scenery import Scenery
from enemy import Enemy, BossEnemy
from config import Config

obj_board = Board(30,500)
obj_board.create_board()

obj_mario = Mario(25,0,1)
obj_mario.starting_position(obj_board.matrix)

# Making the Background :D
obj_scenery = Scenery()

obj_scenery.create_ground(obj_board.matrix)
obj_scenery.create_sky(obj_board.matrix)
obj_scenery.create_clouds(obj_board.matrix, 2, 11)
obj_scenery.create_tunnels(obj_board.matrix, 23, 19)
obj_scenery.create_bricks(obj_board.matrix, 19, 57)
obj_scenery.create_mountain(obj_board.matrix, 3, 294)
obj_scenery.put_barrier(obj_board.matrix)
obj_scenery.create_springs(obj_board)
obj_scenery.create_holes(obj_board)
obj_scenery.create_coins_platforms(obj_board)

enemy1 = Enemy(26,70,1)
enemy2 = Enemy(26,210,1)
enemy3 = Enemy(26,280,1)
enemy4 = Enemy(26,350,1)
enemy5 = Enemy(26,400,1)

enemies = []
enemies.append(enemy1) 
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)

for en in enemies:
	en.starting_position(obj_board.matrix)
 
obj_bossenemy = BossEnemy(3,450,1)
obj_config = Config()

def movemario():
	''' moves Mario'''
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	char = user_input()

	if char == 'd':
		obj_config.coins_right(obj_board.matrix, obj_mario)
		can_he=obj_mario.check_not_collision_right(obj_board.matrix)

		if(obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] == 'B'):
			obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = " "

		
		if can_he == 1:
			obj_mario.disappear_mario(obj_board)
			obj_mario.xcoo+=1
			obj_mario.direction = 1
			obj_mario.reappear_mario(obj_board)

		elif can_he == 2:
			obj_mario.life -= 1
			os.system('afplay ./music/mario_dies.wav&')
			obj_board.spawn_mario(obj_mario)
			obj_mario.did_he_die = 0


		else:
			os.system('afplay ./music/bump.wav&')

	if char == 'a':
		
		obj_config.coins_left(obj_board.matrix, obj_mario)
		can_he=obj_mario.check_not_collision_left(obj_board.matrix)

		if(obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] == 'B'):
			obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = " "
		
		if can_he == 1:
			obj_mario.disappear_mario(obj_board)
			obj_mario.xcoo -= 1
			obj_mario.direction = -1
			obj_mario.reappear_mario(obj_board)

		elif can_he == 2:
			obj_mario.life -= 1
			os.system('afplay ./music/mario_dies.wav&')
			obj_board.spawn_mario(obj_mario)
			obj_mario.did_he_die = 0

		else:
			os.system('afplay ./music/bump.wav&')
				
	if char == 'q':
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		quit()
	
	if char == 'w':
		if(obj_board.matrix[obj_mario.ycoo + 3][obj_mario.xcoo] == "-"): #standing on surface

			prev_ycoo=obj_mario.ycoo
			
			while(obj_mario.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+2] == " " and
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+1] == " " and
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo] == " "): 

				obj_mario.disappear_mario(obj_board)
				obj_mario.ycoo -= 1

				obj_mario.reappear_mario(obj_board)

			os.system('afplay ./music/jump.wav&')
			obj_config.check_brick_collision(obj_scenery, obj_board, obj_mario)

	if char == 's':
		obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = 'B'
		os.system('afplay ./music/bullet.wav&')

		bosskill = obj_bossenemy.check_boss_kill(obj_board, obj_mario)
		# if(bosskill is False):
		# 	obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo] = " "
		# else:
		if bosskill is True:
			if(obj_bossenemy.boss_life == 1):
				obj_bossenemy.boss_kill = True
				obj_scenery.remove_barrier(obj_board.matrix)
			else:
				obj_bossenemy.boss_life -= 1

x=time.time()
y=x #copy
z=x #copy


os.system('afplay ./music/theme.mp3&')

while True: # The Game Loop
	os.system('clear')

	obj_config.rem = 150 - (round(time.time()) - round(x))
	print("TIME REMAINING:", obj_config.rem, end = '\t \t')
	print("LIVES:", obj_mario.life, end = '\t \t')
	print("COINS:", obj_config.coins, end = '\t \t')
	print ("Lives of Boss Enemy:", obj_bossenemy.boss_life)
	print("KILLS: ", obj_config.kills)

	if(time.time() - y >= 0.15): #move basic enemies every 0.5 sec
		y=time.time()
		for en in list(enemies):
			if(en.killed==0):
				en.move(obj_board,obj_mario)
			else:
				enemies.remove(en)

	if(time.time() - z >= 2 and obj_mario.abducted == False and obj_bossenemy.boss_kill is False): 
		''' This checks if 3 seconds have passed, so as to switch the boss enemy to abduction mode'''
		z=time.time()
		if(obj_bossenemy.boss_type == 0):
			obj_bossenemy.boss_type = 1
			obj_bossenemy.remove_boss_abduct(obj_board.matrix)
			obj_bossenemy.put_boss(obj_board.matrix)
		else:
			obj_bossenemy.boss_type=0
			obj_bossenemy.remove_boss(obj_board.matrix)
			obj_bossenemy.put_boss_abduct(obj_board.matrix)
	
	if(obj_bossenemy.boss_kill is True):
		obj_bossenemy.remove_boss_abduct(obj_board.matrix)
		obj_bossenemy.remove_boss(obj_board.matrix)

	
	
	if(obj_mario.ycoo == 26): # Fell into a hole!
		obj_mario.life -= 1
		os.system('afplay ./music/mario_dies.wav&')
		obj_board.spawn_mario(obj_mario)

	if(obj_config.rem==0 or obj_mario.life == 0):
		print("GAME OVER")
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		quit()


	if(obj_mario.xcoo<55):
		obj_board.theyllprintit(0)
	elif(obj_mario.xcoo>=55 and obj_mario.xcoo<444):
		obj_board.theyllprintit(obj_mario.xcoo)
	else:
		obj_board.theyllprintit(444)
	
	movemario()
	
	if(obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo]== obj_scenery.spring or 
		obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+1]== obj_scenery.spring or 
		obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+2]==obj_scenery.spring ):
		
		os.system('afplay ./music/jump.wav&')
		obj_board.jump_higher(obj_mario)

	if(obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo] == "|" and 
		obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+2] == "|"):

		obj_mario.abducted = True

	if(obj_mario.abducted is True):
		
		obj_mario.disappear_mario(obj_board)
		obj_mario.ycoo = obj_mario.ycoo - 1
		obj_mario.reappear_mario(obj_board)

		if(obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+1] == "*"):
			print("GAME OVER")
			os.system("killall afplay")
			os.system('afplay ./music/game_over.wav&')
			quit()

	if(obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo]==" " # simulate gravity
		and obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+1]==" "
		and obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+2]==" " 
		and obj_mario.abducted is False):
			
		obj_mario.disappear_mario(obj_board)
		obj_mario.ycoo+=1
		obj_mario.reappear_mario(obj_board)

	for en in list(enemies):
		obj_mario.check_enemy_collision(obj_board, en, obj_config)

	if(obj_mario.xcoo==497):
		print("WELL DONE!")
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		break;









												  




 

