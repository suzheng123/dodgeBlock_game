import pygame
import random
import sys


pygame.init()

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR_BLACK = (0,0,0)
APPLE_GREEN = (124, 229, 82)
GOLDEN_ORANGE = (241, 172, 9)
LIGHT_PURPLE = (227, 161, 234)

block_speed = 5

BACKGROUND = pygame.image.load('imgs/background.png')


PLAYER_ORIGINAL = pygame.image.load('imgs/watermelon_whole.jpg')
player_size = 50
PLAYER_ORIGINAL = pygame.transform.scale(PLAYER_ORIGINAL,(player_size,player_size))
player_position = [WIDTH/4,HEIGHT-2*player_size]

ENEMY_IMG = pygame.image.load('imgs/knift.jpg')
enemy_size = 50
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG,(enemy_size,enemy_size))
enemy_number = 5
enemy_position = [random.randint(0,WIDTH-enemy_size),0]
enemy_list = [enemy_position]

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace",35)	# printout the score

def draw_window(screen):
	screen.blit(BACKGROUND,(0,0))	# background
	screen.blit(PLAYER_ORIGINAL,(player_position[0],player_position[1]))


def draw_enemies(enemy_list):
	for enemy_position in enemy_list:
		screen.blit(ENEMY_IMG,(enemy_position[0],enemy_position[1],\
	 									enemy_size,enemy_size))


def drop_enemies(enemy_list):	
	delay = random.random()
	if len(enemy_list) < enemy_number and delay < 0.05:
		x_position = random.randint(0,WIDTH-enemy_size)
		y_position = 0
		enemy_list.append([x_position,y_position])

def update_enemy_position(enemy_list,score):
	for index, enemy_position in enumerate(enemy_list):
		# check the enemy block is on the screen
		if enemy_position[1] >= 0 and enemy_position[1] < HEIGHT:
			enemy_position[1] += block_speed
		else:
			enemy_list.pop(index)
			score += 1
	return score

def show_score(score):
	text = "SCORE: " + str(score)
	lable = myFont.render(text, 1, LIGHT_PURPLE)
	screen.blit(lable,(WIDTH-200,HEIGHT-40))


def collision_check(enemy_list,player_position):
	for enemy_position in enemy_list:
		if detect_collision(enemy_position,player_position):
			return True
	return False

def detect_collision(player_position,enemy_position):
	player_x = player_position[0]
	player_y = player_position[1]

	enemy_x = enemy_position[0]
	enemy_y = enemy_position[1]

	if (player_x > enemy_x and player_x < enemy_x+enemy_size) or \
		(enemy_x >= player_x and enemy_x < player_x+player_size): 
		if (enemy_y >= player_y and enemy_y < player_y+player_size) or \
			(player_y >= enemy_y and player_y < enemy_y+enemy_size):
			return True
	return False

	

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	# user click the 'X' icon
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x = player_position[0]
			y = player_position[1]
			if event.key == pygame.K_LEFT: 	# move the player to right
				x -= player_size			# by player_size
			if event.key == pygame.K_RIGHT:	# move the player to left
				x += player_size			# by player_size

			player_position = [x,y]

	draw_window(screen) # fill background, draw player	
	drop_enemies(enemy_list)
	score = update_enemy_position(enemy_list,score)
	show_score(score)
	

	if collision_check(enemy_list,player_position):
		game_over = True
		break 
	draw_enemies(enemy_list)

	clock.tick(30)	# set speed to 30 frames/second
	pygame.display.update() # need to update the screen after iteration







