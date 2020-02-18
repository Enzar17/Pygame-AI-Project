##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# This comprises the logic of the main function of our game.
# It establishes the pygame environment, and creates a number
# of objects that act and interact within the game.
###########################################################


# Import everything we'll need
import pygame
from pygame.locals import *

from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter

import Constants
import random

# Define our main method
def main():
    # Initizalize pygame, create a display defined in the Constants, and fill it
    # with a background
    pygame.init()
    screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
    screen.fill(Constants.BACKGROUND_COLOR)

    # Create a Player object
    player = Player(Vector((Constants.WORLD_WIDTH / 2.0), (Constants.WORLD_HEIGHT / 2.0)), \
                    Constants.PLAYER_SIZE, Constants.PLAYER_SPEED, Constants.PLAYER_COLOR)

    enemyList = []      # Create a list of enemies

    # Populate the list with 5 normal enemies
    for i in range(5):
        newEnemy = Enemy(Vector(random.randint(0, Constants.WORLD_WIDTH - Constants.ENEMY_SIZE),   \
                                random.randint(0, Constants.WORLD_HEIGHT) - Constants.ENEMY_SIZE), \
                         Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_COLOR)

        list.append(enemyList, newEnemy)

    # Populate the list with 5 more enemy hunters
    for i in range(5):
        newEnemy = EnemyHunter(Vector(random.randint(0, Constants.WORLD_WIDTH - Constants.ENEMY_SIZE),   \
                                      random.randint(0, Constants.WORLD_HEIGHT) - Constants.ENEMY_SIZE), \
                               Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_HUNTER_COLOR)

        list.append(enemyList, newEnemy)

    # Create a clock object so we can correctly calculate 60fps
    clock = pygame.time.Clock()

    # Create a sentinel value for whether or not we're done
    done = False

    # MAIN GAME LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Always refresh the screen with our background
        screen.fill(Constants.BACKGROUND_COLOR)

        # Update and draw our player
        player.update(Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
        player.draw(screen)

        # Update and draw our list of enemies
        for enemy in enemyList:
            enemy.update(player, Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT), \
                enemy.calculateTargetVector(player))
            enemy.draw(player, screen, player.center)

        # Flip the double-buffered display
        pygame.display.flip()

        # Use our clock method to make sure we're running at our set frame rate
        clock.tick(Constants.FRAME_RATE)

# Run the main method
main()
