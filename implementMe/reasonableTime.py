from runSimulation import *
from matlibbbb import *
from matlibb3 import *




def reasonabletTwo(robottype):
    strike = 0
    start = 100
    scoress = {}
    while strike!=2:
        avg=runSimulation(1,1,10,10,1,start,robottype,False)
        print avg
        scoress[start]=avg
        if start>100:
            print abs(scoress[start / 2] - avg)
            if abs(scoress[start/2]-avg) > 0 and abs(scoress[start/2]-avg)<7:
                if strike==0 or start/data==2 :
                    strike+=1
                    data = start
                else:
                    strike=0
        start=start*2


    print scoress[start/4]
    return scoress

#plotFrequencyBar(reasonable(StandardRobot))
#plotFrequencyBar(reasonable(RandomWalkRobot))

def reasonablePlusTen(robottype, tolerance):
    strike = 0
    start = 100
    scoress = {}
    times=0
    while start<=10000:
        avg = runSimulation(1, 1, 10, 10, 1, start, robottype, False)
        #print avg
        scoress[start] = avg
        if start > 100:
            #print abs(scoress[start-10] - avg)
            if abs(scoress[start-10] - avg) > 0 and abs(scoress[start-10] - avg) < tolerance:
                if strike == 0 or start - data == 10:
                    strike += 1
                    data = start
                else:
                    strike = 0
        if strike>=3:
            times=scoress[start-20]
        start = start + 10

    #print scoress[start-20]

    if times!=0:
        print times
    return scoress


plotFrequencyBarT(reasonablePlusTen(StandardRobot,5), reasonablePlusTen(RandomWalkRobot,15))