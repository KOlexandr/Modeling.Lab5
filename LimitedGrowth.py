__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def limited_growth(x0, r, k):
    """
    x - number of individuals in the population
    k - capacity factor of population
    r - coefficient of population growth rate
    x0 - initial value of x

    limited growth: x0 = 8, r = 10, k = 25
    default: x0 = 5, r = 0.5, k = 25
    """
    t, y = euler(lambda x: r*x*(1-x/k), x0, dt=0.1, all_steps=100)
    plot(t, y, 'g', label="Graph of the number of time")
    legend(loc='lower right', numpoints=1)
    show()

limited_growth(5, 0.5, 25)