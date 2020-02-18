##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# Defines behavior that is common between all agents in the game,
# including drawing to the screen, updating position and velocity,
# and handling collisions between agents
###########################################################

# Import everything we'll need
import pygame
from pygame.locals import *

from Vector import Vector

class Agent:
    def __init__(self, vecPosition, size, speed, color):
        """Creates an agent with a position, size, speed, and color"""
        self.position = vecPosition     # Starting position (top left corner)
        self.velocity = Vector(0, 0)    # Velocity should always start at 0
        self.size = size                # The width and height of our agent
        self.speed = speed              # The speed the agent is allowed to move per frame
        self.color = color;             # The displayed color of our agent

        # Computes the actual center of the agent based on its position and its size
        self.center = Vector(self.position.x + (self.size/2.0), self.position.y + (self.size/2.0))

        # Define our draw rectangle for use with the collision computation
        self.drawRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

    def __str__(self):
        """Prints string data to the console about our agent for easier debugging"""
        return("Position: " + str(self.position) + "\nCenter: " + str(self.center)
               + "\nVelocity: " + str(self.velocity) + "\nSize: " + str(self.size))

    def draw(self, screen):
        """Draws the agent to the screen that is passed in"""
        pygame.draw.rect(screen, self.color, self.drawRect)

        # Calculate the movement vector from the center of the agent
        self.movementVector = self.center + Vector.scale(self.velocity, 5)

        # Draw a line from the center of the object to where the object thinks it's moving
        pygame.draw.line(screen, (0,0,255), (self.center.x, self.center.y), (self.movementVector.x, self.movementVector.y), 3)

    def update(self, screenBounds):
        '''Adjusts the agent's position, speed, and center'''
        # Normalize and then scale the movement vector
        self.velocity = Vector.normalize(self.velocity)
        self.velocity = Vector.scale(self.velocity, self.speed)

        # Update the position based on the movement vector
        self.position += self.velocity

        # Keep the position within bounds
        self.position.x = sorted((0, self.position.x, screenBounds.x - self.size))[1]
        self.position.y = sorted((0, self.position.y, screenBounds.y - self.size))[1]

        self.drawRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

        # Update our centerpoint
        self.center = Vector(self.position.x + (self.size/2.0), self.position.y + (self.size/2.0))

    def collision(self, other):
        '''Returns true if we're colliding with another agent, and false otherwise'''
        if self.drawRect.colliderect(other.drawRect):
            return True
        else:
            return False