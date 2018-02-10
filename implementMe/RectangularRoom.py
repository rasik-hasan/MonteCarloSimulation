# Problem Set 11: Simulating robots
# Implementation of Rectangular Class
# Name: Mohammad Ehsanul Karim
# Collaborators: None
# Start: July 1, 2016; 11:20pm

import random
from Position import *

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        
        self.locState = {}
        self.width = width
        self.height = height        

        # Initialize all tiles as unclean.
        for x in range(self.width):
            for y in range(self.height):
                self.locState[(x, y)] = False
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = int(pos.getX())
        y = int(pos.getY())

        if self.locState[(x, y)] == False:
            self.locState[(x, y)] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.locState[(m, n)]:
            return True
        
        return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return sum(self.locState.values())

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        xRandPos = random.uniform(0, self.width)
        yRandPos = random.uniform(0, self.height)
        
        return Position(xRandPos, yRandPos)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()

        if x < 0: return False      
        if y < 0: return False
        if x > self.width: return False
        if y > self.height: return False

        return True

# End: July 12, 2016; 11:20pm
