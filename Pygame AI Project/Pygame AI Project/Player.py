##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# This comprises the logic of the player object, which inherits
# most of its functionality from the Agent class, but needs 
# unique player control in its update function
###########################################################

# Import everything we'll need
import pygame
from pygame.locals import *

from Agent import Agent
from Vector import Vector

import Constants

class Player(Agent):
    def update(self, screenBounds):
        """Updates the enemy's position and velocity"""
        pressed = pygame.key.get_pressed()

        # Calculates vertical movement
        if pressed[pygame.K_w] or pressed[pygame.K_UP]: self.velocity.y = -1
        elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]: self.velocity.y = 1
        else: self.velocity.y = 0

        # Calculates horizontal movement
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]: self.velocity.x = -1
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]: self.velocity.x = 1
        else: self.velocity.x = 0

        # Take care of the rest of update with Agent's update method
        super().update(screenBounds)
