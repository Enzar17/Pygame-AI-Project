##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# Defines behavior that is unique to our enemy object, including
# seeking, fleeing, and a no-tag-backs feature
###########################################################

# Import everything we'll need
import pygame
from pygame.locals import *

from Agent import Agent
from Vector import Vector

import Constants

class Enemy(Agent):
    def __init__(self, vecPosition, size, speed, color):
        '''Create an enemy object with a starting position, size, speed, and color'''
        super().__init__(vecPosition, size, speed, color)
        self.seek = True            # Determines whether the enemy is seeking or fleeing
        self.canTag = True          # Determines whether or not we can tag the player
        self.tagTimer = 0           # Times the no-tag-backs feature
        self.startingColor = color  # Stores the base color so we can return to it after flashing
        self.isRealColor = True     # Allows us to flash white while no-tag-backs is active

    def draw(self, player, screen, target):
        '''Draw the enemy object, and draws a line from the enemy to the player if it is close'''
        # The Agent's draw can handle all the regular drawing
        super().draw(screen)

        # If we're not stationary, then the player is within range, so draw a line to our target
        if Vector.length(self.velocity) != 0:
            pygame.draw.line(screen, (255,0,0), (self.center.x, self.center.y), (target.x, target.y), 3)

    def calculateTargetVector(self, player):
        '''Calculates the target vector between the enemy and player'''
        targetVector = player.position - self.position
        return targetVector

    def update(self, player, screenBounds, targetVector):
        '''Update the enemy's position and velocity'''
        # If we cannot tag, then iterate the tag timer
        if self.canTag == False:
            self.tagTimer += 1

        # Every 5 frames (except when the timer is 0), change colors
        if self.tagTimer % 5 == 0 and self.tagTimer > 0:
            self.isRealColor = not self.isRealColor

        # If we've hit the timer max, reset the timer and color and let us tag again
        if self.tagTimer >= Constants.TAG_BACK_TIMER:
            self.tagTimer = 0
            self.realColor = True
            self.canTag = True

        # If we aren't our real color, then we're white
        if self.isRealColor == False:
            self.color = (255,255,255)

        # Otherwise, we're our original color
        else:
            self.color = self.startingColor

        # If we collide with the player, switch behavior and turn off tagging
        if super().collision(player) == True and self.canTag == True:
            self.seek = not self.seek
            self.canTag = False

        # If the player is within range and we're seeking, then go to the target
        if Vector.length(targetVector) < Constants.ENEMY_ATTACK_RANGE and self.seek == True:
            self.velocity = targetVector
        
        # If the player is within range and we're fleeing, then go away from the target
        elif Vector.length(targetVector) < Constants.ENEMY_ATTACK_RANGE and self.seek == False:
            self.velocity = Vector(-targetVector.x, -targetVector.y)

        # Otherwise, do nothing
        else:
            self.velocity = Vector(0, 0)

        # The Agent update can handle the rest
        super().update(screenBounds)