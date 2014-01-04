__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def model_predator_victim_with_competition_between_victims(x0, y0, a1, d12, b, d2, a21):
    """
    x - victims
    y - predators
    a1 - victims of natural reproduction
    b - intraspecific competition
    d2 - mortality of predators
    d12 - victims killed by predators
    a21 - breeding predators

    default: x0 = 2, y0 = 2, a1 = 3, d12 = 2, b = 3, d2 = 1, a21 = 2
    """

    t, x, y = euler_system(lambda x, y: a1*x-d12*x*y-b*x**2, lambda x, y: -d2*y+a21*x*y, x0, y0, dt=0.01)
    plot(t, x, 'r', label="Graph of the number of victims of time")
    plot(t, y, 'g', label="Graph of the number of predators of time")
    legend(loc='upper right', numpoints=1)
    show()

model_predator_victim_with_competition_between_victims(2, 2, 3, 2, 3, 1, 2)