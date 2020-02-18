##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# These are the constants that govern our game logic
###########################################################

#GAME SETTINGS
FRAME_RATE = 60                         # Frames per second in the game
TAG_BACK_TIMER = 120                    # Frames before the agents can tag again

#WORLD SETTINGS
WORLD_WIDTH = 800                       # Pixel width for the screen
WORLD_HEIGHT = 600                      # Pixel height for the screen
BACKGROUND_COLOR = (100, 149, 237)      # Cornflower blue background

#AGENT SETTINGS
PLAYER_SIZE = 10                        # Width and height of the player
PLAYER_SPEED = 5.5                      # How much the player can move per frame
PLAYER_COLOR = (255, 255, 0)            # Yellow, to color the player

ENEMY_SIZE = 10                         # Width and height of the enemy
ENEMY_SPEED = 5                         # How much the enemy can move per frame
ENEMY_ATTACK_RANGE = 200                # How far away the player can be before the enemy reacts
ENEMY_COLOR = (0, 230, 0)               # Green, the color of the enemy

ENEMY_HUNTER_COLOR = (255, 0, 255)      # Magenta, the color of the enemy hunter