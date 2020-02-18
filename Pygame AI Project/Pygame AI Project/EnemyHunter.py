##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# Defines behavior that is unique to our enemy hunter object,
# which is really just the calculation of a different target to
# manifest the pursue and evade behaviors
###########################################################

# Import everything we'll need
import pygame
from pygame.locals import *

from Vector import Vector
from Enemy import Enemy

import Constants

class EnemyHunter(Enemy):
    def __init__(self, vecPosition, size, speed, color):
        '''Create an enemy hunter with a starting position, size, speed, and color'''
        super().__init__(vecPosition, size, speed, color)
        self.targetTime = 0     # We'll use this to calcualte where the player WILL be

    def draw(self, player, screen, target):
        '''Draw the enemy object, and draws a line from the enemy to the player if it is close'''
        # Modify the target position
        target = (player.center + Vector.scale(player.velocity, self.targetTime))

        # The Enemy's draw can handle the rest
        super().draw(player, screen, target)

    def calculateTargetVector(self, player):
        '''Calculate the vector to our target for the pursue behavior'''
        # Calculate the amount of time it would take to reach the player
        self.targetTime = Vector.length(player.center - self.center) / Constants.ENEMY_SPEED
        Vector.normalize(player.velocity)
        target = (player.center + Vector.scale(player.velocity, self.targetTime))

        targetVector = target - self.center
        return targetVector