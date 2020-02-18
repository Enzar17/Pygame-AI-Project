##########################################################
# Author: Liam McAleavey
# Date: 2/18/2020
# Email: lmcaleav@uccs.edu
#
# The Vector class is for use specifically with 2D vectors
# (those with only an x and y component). It provides functionality
# for creating, printing, scaling, and normalizing a 2D vector, 
# as well as calculating the dot product, addition, and subtraction
# of two 2D vectors
###########################################################

# Import the math library
import math

class Vector:
    def __init__(self, x, y):
        """Creates a two dimensional vector"""
        self.x = x
        self.y = y

    def __str__(self):
        """Overloads the str() function to print a vector value to the console for debugging"""
        return("Vector (" + str(self.x) + " , " + str(self.y) + ")")

    def __add__(self, other):
        """Overloads the addition operator to work on two vectors"""
        return(Vector(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        """Overloads the subtraction operator to work on two vectors"""
        return(Vector(self.x - other.x, self.y - other.y))

    def dot(self, other):
        """Produces the dot products of two vectors"""
        return((self.x * other.x) + (self.y * other.y))

    def scale(self, scalar):
        """Scales a vector by a numerical scalar value"""
        return Vector(self.x * scalar, self.y * scalar)

    def length(self):
        """Returns the length (magnitude) of a vector"""
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def normalize(self):
        """Returns the normalized (length of 1) version of a vector"""
        len = Vector.length(self)          # Get the length of the current vector

        # Ensure we're never dividing by 0 before we normalize
        if self.x != 0:
            self.x = self.x / len

        if self.y != 0:
            self.y = self.y / len

        return Vector(self.x, self.y)