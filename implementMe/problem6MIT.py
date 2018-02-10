from Robot import *
from Position import *
from ps6_visualize import *
from RectangularRoom import *
from runSimulation import *
from matlibbTwo import *

stanrobot= {}

stanrobot["20X20"]=(runSimulation(1, 1.0, 20, 20, .80, 1000, StandardRobot,False))
stanrobot["25X16"]=(runSimulation(1, 1.0, 25, 16, .80, 1000, StandardRobot,False))
stanrobot["40X10"]=(runSimulation(1, 1.0, 40, 10, .80, 1000, StandardRobot,False))
stanrobot["50X8"]=(runSimulation(1, 1.0, 50, 8, .80, 1000, StandardRobot,False))
stanrobot["80X5"]=(runSimulation(1, 1.0, 80, 5, .80, 1000, StandardRobot,False))
stanrobot["100X4"]=(runSimulation(1, 1.0, 100, 4, .80, 1000, StandardRobot,False))

randRobot = {}

randRobot["20X20"]=(runSimulation(1, 1.0, 20, 20, .80, 1000, RandomWalkRobot,False))
randRobot["25X16"]=(runSimulation(1, 1.0, 25, 16, .80, 1000, RandomWalkRobot,False))
randRobot["40X10"]=(runSimulation(1, 1.0, 40, 10, .80, 1000, RandomWalkRobot,False))
randRobot["50X8"]=(runSimulation(1, 1.0, 50, 8, .80, 1000, RandomWalkRobot,False))
randRobot["80X5"]=(runSimulation(1, 1.0, 80, 5, .80, 1000, RandomWalkRobot,False))
randRobot["100X4"]=(runSimulation(1, 1.0, 100, 4, .80, 1000, RandomWalkRobot,False))

plotFrequencyBarT(stanrobot, randRobot)

def multirobots(totalnumber, robottype):
    scores={}
    robotcount = 1

    while robotcount<=totalnumber:
        avg = runSimulation(robotcount, 1.0, 20, 20, .80, 1000, robottype ,False)#(num_robots, speed, width, height, min_coverage, num_trials,robot_type, visualize = False)
        scores[robotcount] = avg
        robotcount+=1

    return scores

plotFrequencyBarT(multirobots(10,StandardRobot), multirobots(10,RandomWalkRobot))
