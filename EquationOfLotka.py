__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def equation_of_lotka(x0, y0, b0, k0, k1, k2):
    """
    x, y, b - concentration of chemical elements
    k0, k1, k2 - rate constant transformation of molecules

    default: x0 = 0.2, y0 = 0.5, z0 = 0.3, k0 = 2.5, k1 = 1.5, k2 = 1.5
    """

    t, x, y, b = euler_system3(lambda x, y, z: k0-k1*x*y, lambda x, y, z: k1*x*y-k2*y, lambda x, y, z: k2*y,
                               x0, y0, b0, dt=0.01)
    plot(t, x, 'r', label="x of time")
    plot(t, y, 'b', label="y of time")
    plot(t, b, 'g', label="b of time")
    legend(loc='best', numpoints=1)
    show()

equation_of_lotka(0.2, 0.5, 0.3, 2.5, 1.5, 1.5)