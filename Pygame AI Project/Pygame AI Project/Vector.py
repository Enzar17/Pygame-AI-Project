
import math

class Vector:

    # Constructor
    def __init__(self, x, y):
        """Creates a two dimensional vector"""
        self.x = x
        self.y = y

    # convert vector to string (for printing)
    def __str__(self):
        """Overloads the str() function to print a vector value to the console for debugging"""
        return("Vector (" + str(self.x) + " , " + str(self.y) + ")")

    # Add two vectors together
    def __add__(self, other):
        """Overloads the addition operator to work on two vectors"""
        return(Vector(self.x + other.x, self.y + other.y))

    # Subtract other from self
    def __sub__(self, other):
        """Overloads the subtraction operator to work on two vectors"""
        return(Vector(self.x - other.x, self.y - other.y))

    # dot product of two vectors
    def dot(self, other):
        """Produces the dot products of two vectors"""
        return((self.x * other.x) + (self.y * other.y))

    # scales a vector by a scalar (real number) value
    def scale(self, scalar):
        """Scales a vector by a numerical scalar value"""
        return Vector(self.x * scalar, self.y * scalar)

    # gives the magnitude of the vector
    def length(self):
        """Returns the length (magnitude) of a vector"""
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    # normalize a vector
    def normalize(self):
        """Returns the normal of a vector"""
        len = Vector.length(self)

        # Ensure we're never dividing by 0 before we normalize
        if self.x != 0:
            self.x = self.x / len

        if self.y != 0:
            self.y = self.y / len

        return Vector(self.x, self.y)