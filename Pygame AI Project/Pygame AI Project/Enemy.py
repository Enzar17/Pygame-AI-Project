from Vector import Vector

import pygame
from pygame.locals import *

import Constants

from Agent import Agent

class Enemy(Agent):
    # We need this variable later for behavior
    def __init__(self, vecPosition, size, speed):
        super().__init__(vecPosition, size, speed)
        self.seek = True        # We need this variable later for behavior

    # Draw some unique stuff for our enemy
    def draw(self, player, screen):
        """Draws an extra line from the enemy to the player if it is active"""
        super().draw(screen)

        if Vector.length(self.velocity) != 0:
            pygame.draw.line(screen, (255,0,0), (self.center.x, self.center.y), (player.center.x, player.center.y), 3)

    # Update the enemy's values
    def update(self, player, screenBounds, canSwitchTag):
        """Updates the enemy's position and velocity"""
        pressed = pygame.key.get_pressed()

        # Calculate a vector pointing at the player
        target = player.position - self.position

        # If the player is within range, act
        if super().collision(player) == True:
            self.seek = not self.seek

        if Vector.length(target) < Constants.ENEMY_ATTACK_RANGE and self.seek == True:
            self.velocity = target

        elif Vector.length(target) < Constants.ENEMY_ATTACK_RANGE and self.seek == False:
            self.velocity = Vector(-target.x, -target.y)

        else:
            self.velocity = Vector(0, 0)

        super().update(screenBounds, canSwitchTag)