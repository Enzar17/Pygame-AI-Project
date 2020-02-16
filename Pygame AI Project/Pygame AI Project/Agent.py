import pygame
from pygame.locals import *

from Vector import Vector

class Agent:
    # Constructor
    def __init__(self, vecPosition, size, speed):
        """Constructor that accepts a vector for position and velocity, and a size"""
        self.position = vecPosition
        self.velocity = Vector(0, 0)
        self.size = size
        self.speed = speed
        self.center = Vector(self.position.x + (self.size/2.0), self.position.y + (self.size/2.0))
        self.drawRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.canTag = True

    def __str__(self):
        """Prints string data to the console about our agent for easier debugging"""
        return("Position: " + str(self.position) + "\nCenter: " + str(self.center)
               + "\nVelocity: " + str(self.velocity) + "\nSize: " + str(self.size))

    # Draw the enemy to the screen
    def draw(self, screen, color):
        """Draws the enemy to the screen that is passed in"""
        pygame.draw.rect(screen, color, self.drawRect)

        # Calculate the movement vector from the center of the enemy
        self.movementVector = self.center + Vector.scale(self.velocity, 5)

        # Draw a line from the center of the object to where the object thinks it's moving
        pygame.draw.line(screen, (0,0,255), (self.center.x, self.center.y), (self.movementVector.x, self.movementVector.y), 3)

    def update(self, screenBounds, switchTag):
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

        # Change over our canTag if need be
        if self.canTag == True:


    def collision(self, other):
        if self.drawRect.colliderect(other.drawRect) and self.canTag == True:
            #pygame.time.set_timer(USEREVENT, 1000, True)
            self.canTag = False
            return True
        else:
            return False