__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def competition_between_two_species(u10, u20, a1, a2, a12, a21, u1_max, u2_max):
    """
    Model of competition between two species
    a1 - coefficient of population growth rate
    a12, a21 - coefficients of the negative impact of population growth on rival
    u1_max, u2_max - medium-capacity ratios for each genus

    default: u10 = 0.01, u20 = 0.02, a1 = 2.9, a2 = 1.9, a12 = 1, a21 = 2.1, u1_max = 15, u2_max = 20
    """

    t, x, y = euler_system(lambda u1, u2: a1*u1*(1-u1/u1_max-a12*u2/u2_max),
                           lambda u1, u2: a2*u2*(1-u2/u2_max-a21*u1/u1_max), u10, u20, dt=0.01)
    plot(t, x, 'r', label="x of time")
    plot(t, y, 'g', label="y of time")
    legend(loc='best', numpoints=1)
    show()

competition_between_two_species(0.01, 0.2, 2.9, 1.9, 1, 2.1, 15, 20)