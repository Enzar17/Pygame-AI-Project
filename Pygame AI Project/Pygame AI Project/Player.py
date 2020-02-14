from Vector import Vector

import pygame
from pygame.locals import *

import Constants
from Agent import Agent

class Player(Agent):
    # Update the player's values
    def update(self, screenBounds, canSwitchTag):
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

        super().update(screenBounds, canSwitchTag)
