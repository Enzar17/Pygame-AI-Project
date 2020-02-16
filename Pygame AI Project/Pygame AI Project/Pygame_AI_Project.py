# Import everything we'll need
import pygame
from pygame.locals import *

from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter

import Constants

# Define our main method
def main():
    # Initizalize pygame, create an 800 x 600 display, and fill it with cornflower blue
    pygame.init()
    screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
    screen.fill(Constants.BACKGROUND_COLOR)

    # Create a Player object
    player = Player(Vector((Constants.WORLD_WIDTH / 2.0), (Constants.WORLD_HEIGHT / 2.0)),
                    Constants.PLAYER_SIZE, Constants.PLAYER_SPEED)

    # Create an enemy object
    enemy = Enemy(Vector(100, 100), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED)

    # Create an enemy hunter object
    enemyHunter = EnemyHunter(Vector(300, 100), Constants.ENEMY_SIZE, 3)

    # Create an event check for the no-tag-backs feature
    canSwitchTag = False

    # Create a clock object so we can correctly calculate 60fps
    clock = pygame.time.Clock()

    # Create a sentinel value for whether or not we're done
    done = False

    # MAIN GAME LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Always refresh the screen with cornflower blue
        screen.fill(Constants.BACKGROUND_COLOR)

        # Check the noTagBacksEvent
        if pygame.event.get(pygame.USEREVENT):
            canSwitchTag = True
            print("It's ON")

        # Update and draw our player
        player.update(Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT), canSwitchTag)
        player.draw(screen, Constants.PLAYER_COLOR)

        # Update and draw our enemy
        enemy.update(player, Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT), canSwitchTag)
        enemy.draw(player, screen, Constants.ENEMY_COLOR, player.center)

        # Update and draw our enemy hunter
        enemyHunter.update(player, Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT), canSwitchTag)
        enemyHunter.draw(player, screen, Constants.ENEMY_HUNTER_COLOR)

        # Now that the update is over, turn our canSwitchTag off if necessary
        if canSwitchTag:
            canSwitchTag = False
            print("It's OFF")

        # Flip the double-buffered display
        pygame.display.flip()

        # Use our clock method to make sure we're running at our set frame rate
        clock.tick(Constants.FRAME_RATE)

# Run the main method
main()
