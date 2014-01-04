__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def symbiosis(u10, u20, a1, b11, b12, a2, b21, b22):
    """
    u1 - first genus
    u2 - second genus
    a1, a2 - coefficients of population growth rate
    b11, b22 - coefficient of intraspecific competition
    b21, b12 - coefficients of symbiosis

    default: u10 = 0.9, u20 = 0.3, a1 = 2, b11 = 5, b12 = 2, a2 = 3, b21 = 3, b22 = 2
    """

    t, x, y = euler_system(lambda x, y: x*(a1-b11*x+b12*y), lambda x, y: y*(a2+b21*x-b22*y), u10, u20, dt=0.01)
    plot(t, x, 'r', label="u1 of time")
    plot(t, y, 'g', label="u2 of time")
    legend(loc='best', numpoints=1)
    show()

symbiosis(0.9, 0.3, 2, 5, 2, 3, 3, 2)