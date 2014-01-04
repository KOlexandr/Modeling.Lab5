__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def continuous_cultures(x0, u, v):
    """
    Model of continuous culture of microorganisms
    x - concentration of cells in the cultivator
    u - multiplication factor of population
    v - leaching rate of speed

    default: x0 = 5, u = 2.5, v = 2
    """
    #u = 1
    #v = 5
    t, y = euler(lambda x: x*(u-v), x0, dt=0.01)
    plot(t, y, 'g', label="Graph of the number of time")
    legend(loc='upper left', numpoints=1)
    show()

continuous_cultures(5, 2.5, 2)