__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def model_of_chernavskiy(x0, y0, a, b):
    """
    Model selection based on competitive relationships Chernavskiy
    x - describes the number of individuals in the first population
    y - describes the number of individuals in the second population
    a - multiplication factor
    b - factor inhibition of one species by another, and vice versa

    default: x0 = 0.1, y0 = 0.2, a = 20, b = 10
    """
    #u = 1
    #v = 5
    t, x, y = euler_system(lambda x, y: a*x-b*x*y, lambda x, y: a*y-b*x*y, x0, y0, dt=0.001, all_steps=100)
    plot(t, x, 'r', label="Graph of the number of first population of time")
    plot(t, y, 'g', label="Graph of the number of second population of time")
    legend(loc='upper left', numpoints=1)
    show()

model_of_chernavskiy(0.1, 0.2, 20, 10)