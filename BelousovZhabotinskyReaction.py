__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def belousov_zhabotinsky_reaction(x0, y0, z0, l, c):
    """
    Belousov-Zhabotinsky Reaction
    x - concentration of cerium ions
    y - concentration of avto catalyst
    z - concentration of bromide
    l - rate of reaction rates
    c - coefficient of catalyst
    """

    t, x, y, z = euler_system3(lambda x, y, z: l[0] * y * (c - x) - l[2] * x,
                               lambda x, y, z: l[0] * y * (c - x) - l[1] * y * z + l[4],
                               lambda x, y, z: l[2] * x + l[5] * (l[6] * y - l[7]) * (l[6] * y - l[7]) * x - l[3] * z,
                               x0, y0, z0, dt=0.01, all_steps=2000)
    plot(t, x, 'r', label="x of time")
    plot(t, y, 'b', label="y of time")
    plot(t, z, 'g', label="z of time")
    legend(loc='best', numpoints=1)
    show()


belousov_zhabotinsky_reaction(0.5, 0.5, 0.4, [0.1, 0.5, 1, 1.5, 0.91, 1, 1, 1.9], 15)