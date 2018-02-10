import numpy as np
import matplotlib.pyplot as plt
import operator
# Fix the indentation
def plotFrequencyBar(freqDict):
    # Turns the dictionary into a list of tuples.
    # The [0:10] makes the list return its first 10 key-value pairs, and the reverse=True sorts the list from highest to lowest.
    lists = sorted(freqDict.items(), key=operator.itemgetter(0), reverse=False)[0:10]
    # Divides the tuples in the list into separate lists of keys (terms) and values (counts)
    terms, counts = zip(*lists)
    # This is the range of the plotting of the graph.
    r = range(len(terms))
    # This is necessary to print strings on the x axis.
    plt.xticks(r, terms)
    # This shows bars for the Y value instead of points, and aligns each bar to the center of each X value.
    plt.plot(r, counts)
    # Shows the bar chart.
    plt.show()