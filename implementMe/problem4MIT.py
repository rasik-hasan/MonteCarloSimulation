from Robot import *
from Position import *
from ps6_visualize import *
from RectangularRoom import *
from runSimulation import *
from matlibbbb import *

robotcount = 1
scores = {}

#problem 4.1
while robotcount<=10:
    avg = runSimulation(robotcount, 1.0, 20, 20, .80, 1000, StandardRobot,True)#(num_robots, speed, width, height, min_coverage, num_trials,robot_type, visualize = False)
    scores[robotcount] = avg
    robotcount+=1

plotFrequencyBar(scores)
#print scores

#problem 4.2

tworobot = {}

tworobot["20X20"]=(runSimulation(2, 1.0, 20, 20, .80, 1000, StandardRobot,False))
tworobot["25X16"]=(runSimulation(2, 1.0, 25, 16, .80, 1000, StandardRobot,False))
tworobot["40X10"]=(runSimulation(2, 1.0, 40, 10, .80, 1000, StandardRobot,False))
tworobot["50X8"]=(runSimulation(2, 1.0, 50, 8, .80, 1000, StandardRobot,False))
tworobot["80X5"]=(runSimulation(2, 1.0, 80, 5, .80, 1000, StandardRobot,False))
tworobot["100X4"]=(runSimulation(2, 1.0, 100, 4, .80, 1000, StandardRobot,False))

#print tworobot
#plotFrequencyBar(tworobot)