__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def biological_processes(x0, y0, c, kmx, kmy, k, q, ksmy):
    """
    The vibrations and rhythms in biological processes
    x - fructose-6-phosphate, a key substrate reaction
    y - reaction product of x

    default1: x0 = 0.5, y0 = 0.5, c = 1.5, kmx = 3.5, kmy = 4, k = 1.5, q = 3.5, ksmy = 1.5
    default2: x0 = 0.5, y0 = 0.5, c = 2.5, kmx = 4.5, kmy = 3, k = 1.5, q = 2, ksmy = 1.5
    """

    t, x, y = euler_system(lambda x, y: k-(c*x*y)/(kmx+x)*(kmy+y), lambda x, y: (c*x*y)/(kmx+x)*(kmy+y)-q*y/(ksmy+y),
                           x0, y0, dt=0.01, all_steps=2000)
    plot(t, x, 'r', label="x of time")
    plot(t, y, 'g', label="y of time")
    legend(loc='best', numpoints=1)
    show()

biological_processes(0.5, 0.5, 1.5, 3.5, 4, 1.5, 3.5, 1.5)
#biological_processes(0.5, 0.5, 2.5, 4.5, 3, 1.5, 2, 1.5)