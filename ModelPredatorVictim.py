__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def model_predator_victim(x0, y0, a, b, c, d):
    """
    x - describes the number of individuals number of victims
    y - describes the number of individuals number of predators
    a - victims of natural reproduction
    b - mortality of predators
    c - victims killed by predators
    d - breeding predators

    default: x0 = 0.2, y0 = 0.5, a = 4, b = 2, c = 2, d = 3
    """
    #u = 1
    #v = 5
    t, x, y = euler_system(lambda x, y: a*x-b*x*y, lambda x, y: c*x*y-d*y, x0, y0, dt=0.01, all_steps=1000)
    plot(t, x, 'r', label="Graph of the number of victims of time")
    plot(t, y, 'g', label="Graph of the number of predators of time")
    legend(loc='upper left', numpoints=1)
    show()

model_predator_victim(0.2, 0.5, 4, 2, 2, 3)