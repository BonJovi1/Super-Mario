Coded By : Abhinav Gupta
Roll No : 20171059

The file has following sections :

1) Information about the game
2) Rules of the Game
3) Description of Classes created
4) Instructions of running the game
5) Requirements
6) SPECIAL FEATURES ADDED

1.   About the Game

	 Browse this link for info : https://en.wikipedia.org/wiki/Super_Mario_Bros.

2.   Rules of the game

	1) 
	2) You get bonus points and coins on the way, you can also kill enemies by jumping on them
	3) You get 4 lives and a timer to predict ur final score.
	4) In the end ,the boss level starts, the boss shoots bullets once you come in his line of sight.
	5) Boss is SMART and CHASES the mario character and shoots bullets in that direction.
	6) Boss can be killed by jumping on his head represented by 'T', if you touch anywhere else, You lose a life. 

3.   Description of Classes

	1) Draw_Scenery : This class creates the whole level at once segments of which are displayed during gameplay.

	2) GameBoard : The Gameboard Class inherits the Draw_Scenery class. This displays the segment of the whole scenery and 
	player,missiles,enemies etc. on it.

	3) Mario : Mario Class inherits the Draw_Scenery class , It helps in movement of Mario and also manages its score and lives throughout the game .

	4) Enemy : The Enemy Class inherits the Draw_Scenery class. The class creates and manages various enemies onboard.

	5) Boss : The Boss Class inherits the Draw_Scenery class. This creates the SMART boss enemy which FOLLOWS THE MARIO and SHOOTS IN HIS DIRECTION once he SEES the player.

4.   Instructions to play 

	Run the following command in the directory :

	1)python3 main.py

	2) Use the following controls:
		a) w,a,d to jump, move left, move right respectively.
		b) press q to quit the game

5.  Requirements

	1) Python3 
		a) Numpy Library Version '1.15.0' (install it using pip3 install numpy)

6.  Special Features 

	1) The boss enemy is smart and follows the character around wherever he goes and shoots in that direction.
	2) Sounds added for various events.
	3) Springs around the boss to facilitate jumping above him.