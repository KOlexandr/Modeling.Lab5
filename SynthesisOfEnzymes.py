__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def synthesis_of_enzymes(p10, p20, a1, a2, b1, b2, q1, q2, m):
    """
    Model alternative synthesis of the two enzymes
    p1, p2 - concentration of products
    a1, a2, b1, b2 - coefficients are expressed in terms of the parameters of their systems
    m - indicates how many molecules are actively represses
    q1, q2 - coefficients of the number of molecules

    default: p10 = 10, p20 = 20, a1 = 1.1, a2 = 10, b1 = 20, b2 = 10, q1 = 50, q2 = 100, m = 200
    """

    t, x, y = euler_system(lambda p1, p2: a1/(b1 + p2**m)-q1*p1, lambda p1, p2: a2/(b2 + p1**m)-q2*p2, p10, p20,
                           all_steps=100)
    plot(t, x, 'r', label="p1 of time")
    plot(t, y, 'g', label="p2 of time")
    legend(loc='best', numpoints=1)
    show()

synthesis_of_enzymes(10, 20, 1.1, 10, 20, 10, 50, 100, 200)