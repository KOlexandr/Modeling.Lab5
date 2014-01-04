__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def three_genus(u10, u20, u30, a, b):
    """
    Model competition of three genus

    default1: u10 = 0.1, u20 = 0.2, u30 = 0.3, a = 0, b = 1.5
    default2: u10 = 0.1, u20 = 0.2, u30 = 0.3, a = 0.49, b = 1.5
    """

    m = [[1, b, a], [a, 1, b], [b, a, 1]]

    t, u1, u2, u3 = euler_system3(lambda x, y, z: x*(1-m[0][0]*x-m[0][1]*y-m[0][2]*z),
                                  lambda x, y, z: y*(1-m[1][0]*x-m[1][1]*y-m[1][2]*z),
                                  lambda x, y, z: z*(1-m[2][0]*x-m[2][1]*y-m[2][2]*z), u10, u20, u30, dt=0.1)
    plot(t, u1, 'r', label="u1 of time")
    plot(t, u2, 'b', label="u2 of time")
    plot(t, u3, 'g', label="u3 of time")
    legend(loc='best', numpoints=1)
    show()

three_genus(0.1, 0.2, 0.3, 0, 1.5)