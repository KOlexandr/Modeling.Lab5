__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def distribution_of_microorganisms(n10, n20, t1, t2, d):
    """
    The distribution of microorganisms by age
    n1 - young cells
    n2 - old cells
    d - flow rate ratio
    t1 - average rate of growth time young cells
    t2 - coefficient of average residence time of old cells in the reproductive age

    default: n10 = 50, n20 = 10, t1 = 1, t2 = 1, d = 1
    """

    t, x, y = euler_system(lambda n1, n2: 2/t2*n2-1/t1*n1-d*n1, lambda n1, n2: 1/t1*n1-1/t2*n2-d*n2, n10, n20, dt=0.01)
    plot(t, x, 'r', label="young cells of time")
    plot(t, y, 'g', label="old cells of time")
    legend(loc='best', numpoints=1)
    show()

distribution_of_microorganisms(50, 10, 1, 1, 1)