# Problem Set 11: Simulating robots
# Implementation of Robot Class.
# Name: Mohammad Ehsanul Karim
# Collaborators: None
# Start: July 1, 2016; 11:20pm

import random
from Position import *
from RectangularRoom import *

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed = 1):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randrange(360)
        self.location = room.getRandomPosition()
        self.room.cleanTileAtPosition(self.location)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.location
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.location = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        candidateLocation = self.location.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(candidateLocation):
            self.setRobotPosition(candidateLocation)
            self.room.cleanTileAtPosition(candidateLocation)
        else:            
            self.setRobotDirection(random.uniform(0, 360))

# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        candidateLocation = self.location.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(candidateLocation):
            self.setRobotPosition(candidateLocation)
            self.room.cleanTileAtPosition(candidateLocation)

        self.setRobotDirection(random.uniform(0, 360))           

# End: July 12, 2016; 11:20pm 
