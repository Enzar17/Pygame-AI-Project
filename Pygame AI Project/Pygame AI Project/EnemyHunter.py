from Vector import Vector
from Enemy import Enemy
from Agent import Agent
import Constants

import pygame
from pygame.locals import *

class EnemyHunter(Enemy):
    # We need this variable later for behavior
    def __init__(self, vecPosition, size, speed):
        super().__init__(vecPosition, size, speed)
        self.pursue = True       # We need this variable later for behavior

    # Draw some unique stuff for our enemy
    def draw(self, player, screen, color):
        """Draws an extra line from the enemy to the player if it is active"""
        super().draw(player, screen, color, (player.center + player.velocity))

    def update(self, player, screenBounds, canSwitchTag):
        """Updates the enemy hunter's position and velocity"""
        # Calculate a vector pointing at the player
        self.target = (player.position + player.velocity) - self.position

        # If the player is within range, act
        if Agent.collision(self, player) == True:
            self.pursue = not self.pursue

        if Vector.length(self.target) < Constants.ENEMY_ATTACK_RANGE and self.seek == True:
            self.velocity = self.target

        elif Vector.length(self.target) < Constants.ENEMY_ATTACK_RANGE and self.seek == False:
            self.velocity = Vector(-self.target.x, -self.target.y)

        else:
            self.velocity = Vector(0, 0)

        Agent.update(self, screenBounds, canSwitchTag)