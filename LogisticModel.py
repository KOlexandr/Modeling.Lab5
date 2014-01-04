__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def logistic_model(x0, u1, u2):
    """
    x - describes the number of individuals in the population
    u1 - coefficient of population growth rate
    u2 - factor of exclusion from the population of individuals per unit time
    x0 - initial value of x

    default: x0 = 2.5, u1 = 1.4, u2 = 1.5
    """
    t, y = euler(lambda x: u1*x - x**2 - u2, x0, dt=0.001, all_steps=1000)
    plot(t, y, 'g', label="Graph of the number of time")
    legend(loc='lower left', numpoints=1)
    show()

logistic_model(2.5, 1.4, 1.5)