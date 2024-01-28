from processing import *

#Defining variables
width = 800
height = 600
player_x = 350
player_y = 300
player_width = 35
player_height = 50
monster_x = 400
monster_y = 300
move_monster_x = 7
move_monster_y = 4
monster_width = 50
monster_height = 50
bullet_x = player_x
bullet_y = 300
bullet_width = 21
bullet_height = 30
move_bullet_x = 0
move_bullet_y = 15
bullets_left = 7
colliding_first_time = False
superpower_active = False
superpowers_left = 3
superpower_x = player_x
superpower_y = 300
superpower_width = 50
superpower_height = 50
move_superpower_x = 0
move_superpower_y = 15
colliding_first_time_superpower = False
colliding_first_time_player = False
activity = ""
count = 0
shoot = False
game_over = False
above_height = False
bullet_hit = False
score = 7


# setup is called once at the start
def setup():
	global bg
	global player
	global monster
	global bullet
	global superpower
	
	size(800,600)
	bg = loadImage("stars.jpg")
	player = loadImage("player.png")
	monster = loadImage("monster.png")
	bullet = loadImage("bullet.png")
	superpower = loadImage("strawberry.png")
	textSize(20)
	
def draw():
	pass
	#Defining these variables to be global, meaning their value can be changed in this function(draw)
	global bg
	global player
	global monster_x
	global monster_y
	global move_monster_x
	global move_monster_y
	global player_x
	global player_y
	global bullet_x
	global bullet_y
	global bullet_width
	global bullet_height
	global bullet
	global move_bullet_y
	global bullets_left
	global superpower_y
	global superpowers_left
	global colliding_first_time
	global colliding_first_time_superpower
	global colliding_first_time_player
	global activity
	global count
	global game_over
	global bullet_hit
	global above_height
	global score
	
	if not game_over:
		if bullets_left < 0:
			game_over = True
		else:
			game_over = False
		
		if bullets_left > score:
			score = bullets_left

		#Making the bullet shoot from where the player is
		bullet_x = player_x
		
		if (bullet_y + bullet_height) < 0:
			above_height = True
		else:
			above_height = False
			
		if above_height and not bullet_hit:
			count = 0
		if count == 3:
			superpowers_left = superpowers_left + 1
			activity = "+1 SUPERPOWER! 3 HITS IN A ROW"
			count = 0
			
		image(bg, 0, 0)
		image(player, player_x, player_y)
		if shoot:
			image(bullet, bullet_x, bullet_y)
			image(superpower, superpower_x, superpower_y)
			image(monster, monster_x, monster_y)
			monster_x = monster_x + move_monster_x
			monster_y = monster_y + move_monster_y

		#Making the actual bullet or strawberry superpower move
		bullet_y = bullet_y - move_bullet_y
		superpower_y = superpower_y - move_superpower_y

		#Displaying the recent activity on the screen, such as: +3 BULLETS, +5 BULLETS, -5 BULLETS -1 SUPERPOWER, +1 SUPERPOWER
		fill(255, 0, 255)
		text(activity, 400, 250)

		if bullets_left > 1:
			bullet = loadImage("bullet.png")
			bullet_width = 21
			bullet_height = 30

		if bullets_left > -1:
			fill(255, 255, 255)
			text("BULLETS LEFT: {}".format(bullets_left), 30, 40)
			fill(255, 255, 0)
			text("SUPERPOWERS LEFT: {}".format(superpowers_left), 30, 90)
			fill(0, 255, 0)
			text("SCORE: {}".format(score), 410, 40)
			
			#Putting this text at the bottom of the screen to guide the player
			if shoot == False:
				fill(0, 255, 0)
				text("WASD to move| CLICK MOUSE to shoot| PRESS SPACEBAR to use superpower", 30, 480)
				text("DEFEAT THE MONSTER!", 280, 510)
				text("IF YOU LOSE ALL YOUR BULLETS YOU HAVE FAILED THE MISSION!", 50, 540)
				text("USE YOUR SUPERPOWERS BEFORE YOU LOSE ALL YOUR BULLETS!", 45, 570)
				text("CLICK TO START", 300, 380)

		if monster_x + monster_width > width:
			move_monster_x = -move_monster_x
		if monster_x < 0:
			move_monster_x = -move_monster_x
		if monster_y + monster_height > height:
			move_monster_y = -move_monster_y
		if monster_y < 0:
			move_monster_y = -move_monster_y

		#Checking if the bullet hit, and if it did then +3 BULLETS
		if colliding_first_time == False:
			if isColliding(bullet_x, bullet_y, bullet_width, bullet_height, monster_x, monster_y, monster_width, monster_height):
				bullet_hit = True
				count = count + 1
				bullets_left = bullets_left + 3
				activity = "+3 BULLETS!"
				colliding_first_time = True

		#Checking if the strawberry hit, and if it did then +5 BULLETS
		if colliding_first_time_superpower == False:
			if isColliding(superpower_x, superpower_y, superpower_width, superpower_height, monster_x, monster_y, monster_width, monster_height):
				bullets_left = bullets_left + 5
				activity = "+5 BULLETS!"
				colliding_first_time_superpower = True

		#Checking if the player is colliding with the monster, and if they are colliding then it will -5 bullets and -1 superpower
		if colliding_first_time_player == False:
			if isColliding(monster_x, monster_y, monster_width, monster_height, player_x, player_y, player_width, player_height):
				bullets_left = bullets_left - 5
				activity = "OUCH! -5 BULLETS! -1 SUPERPOWER!"
				colliding_first_time_player = True
				if superpowers_left > 0:
					superpowers_left = superpowers_left -1

		if colliding_first_time_player == True:
			if not isColliding(monster_x, monster_y, monster_width, monster_height, player_x, player_y, player_width, player_height):
				colliding_first_time_player = False

		if bullets_left == 0 and above_height:
			fill(255, 0, 0)
			text("CLICK MOUSE TO ACCEPT DEFEAT", 200, 300)
			
	if game_over:
		size(800, 600)
		image(bg, 0, 0)
		fill(255, 255, 255)
		text("GAME OVER!", 300, 300)
		fill(0, 255, 0)
		text("SCORE: {}".format(score), 320, 350)
		text("PRESS SPACEBAR TO RESTART", 220, 430)

def keyPressed():
	global game_over
	global player_x
	global player_y
	global monster_x
	global monster_y
	global move_monster_x
	global move_monster_y
	global bullet_x
	global bullet_y
	global move_bullet_x
	global move_bullet_y
	global bullets_left
	global colliding_first_time
	global superpower_active
	global superpowers_left
	global superpower_x
	global superpower_y
	global move_superpower_x
	global move_superpower_y
	global colliding_first_time_superpower
	global colliding_first_time_player
	global activity
	global count
	global shoot
	global above_height
	global bullet_hit
	global score
	
	old_player_y = player_y

	#Making it so that if the player presses the SPACEBAR it will shoot the strawberry
	if keyboard.keyCode == 32 and superpowers_left > 0 and bullets_left > 0:
		shoot = True
		superpowers_left = superpowers_left - 1
		superpower_y = player_y
		superpower_x = player_x
		colliding_first_time_superpower = False
		
	if keyboard.keyCode == 32 and game_over:
		game_over = False
		player_x = 350
		player_y = 300
		monster_x = 400
		monster_y = 300
		move_monster_x = 7
		move_monster_y = 4
		bullet_x = player_x
		bullet_y = 300
		move_bullet_x = 0
		move_bullet_y = 15
		bullets_left = 7
		colliding_first_time = False
		superpower_active = False
		superpowers_left = 3
		superpower_x = player_x
		superpower_y = 300
		move_superpower_x = 0
		move_superpower_y = 15
		colliding_first_time_superpower = False
		colliding_first_time_player = False
		activity = ""
		count = 0
		shoot = False
		above_height = False
		bullet_hit = False
		score = 7
				
	old_player_x = player_x
	
	#Letting the player move with WASD
	if keyboard.key == "d":
		player_x = player_x + 5
	if keyboard.key == "a":
		player_x = player_x - 5
	if keyboard.key == "w":
		player_y = player_y - 5
	if keyboard.key == "s":
		player_y = player_y + 5
	if player_x < 0 or player_x + player_width > width:
		player_x = old_player_x
	if player_y < 0 or player_y + player_height > height:
		player_y = old_player_y

def mouseClicked():
	global bullet_y
	global bullets_left
	global colliding_first_time
	global shoot
	global bullet_hit

	shoot = True

	#Making it so that if the player clicks it will shoot the bullet from where the player is and they will lose one bullet
	if bullets_left > -1:
		bullet_hit = False
		bullets_left = bullets_left - 1
		bullet_y = player_y
		colliding_first_time = False
	
#Defining the function to check if two specific sprites are colliding
def isColliding(first_x, first_y, first_width, first_height, second_x, second_y, second_width, second_height):
	first = (first_x + first_width) > second_x
	second = first_x < (second_x + second_width)
	third = (first_y + first_height) > second_y
	fourth = first_y < (second_y + second_height)
	
	return first and second and third and fourth

run()
