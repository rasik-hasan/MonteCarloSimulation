import numpy as np
import matplotlib.pyplot as plt
import operator
# Fix the indentation
def plotFrequencyBarT(freqDict,fdict ):
    # Turns the dictionary into a list of tuples.
    # The [0:10] makes the list return its first 10 key-value pairs, and the reverse=True sorts the list from highest to lowest.
    lists = sorted(freqDict.items(), key=operator.itemgetter(0), reverse=False)
    lists2 = sorted(fdict.items(), key=operator.itemgetter(0), reverse=False)
    # Divides the tuples in the list into separate lists of keys (terms) and values (counts)
    terms, counts = zip(*lists)
    terms2, counts2 = zip(*lists2)
    # This is the range of the plotting of the graph.
    r = range(len(terms))
    # This is necessary to print strings on the x axis.
    #plt.xticks(np.arange(min(terms), max(terms), 20))
    #plt.xticks(r,terms)
    #print min(terms)
    #print max(terms)
    # This shows bars for the Y value instead of points, and aligns each bar to the center of each X value.
    plt.plot(terms,counts, label="standard robot")
    plt.plot(terms2,counts2, label="random robot")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

    # Shows the bar chart.
    plt.show()