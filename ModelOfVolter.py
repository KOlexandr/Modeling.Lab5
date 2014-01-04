__author__ = 'KOL'

from Solve import *
from matplotlib.pyplot import plot, show, legend


def model_of_volter(x0, y0, a, b, c, d, e, m, p):
    """
    Modification of Voltaire model considering the limited substrate
    x - victims
    y - predators
    a - victims of natural reproduction
    b - mortality of predators
    c - coefficient victims exterminated predators
    d - multiplication factor predators
    e - coefficient of competition between victims
    m - coefficient of competition between predators

    default: x0 = 0.5, y0 = 0.5, a = 2, b = 1, c = 1, d = 0.1, e = 1, m = 2, p = 1
    """

    t, x, y = euler_system(lambda x, y: a*x-b*x*y/(1+p*x)-e*x**2, lambda x, y: -c*y-d*x*y/(1+p*x)-m*y**2,
                           x0, y0, dt=0.01)
    plot(t, x, 'r', label="Graph of the number of victims of time")
    plot(t, y, 'g', label="Graph of the number of predators of time")
    legend(loc='upper right', numpoints=1)
    show()

model_of_volter(0.5, 0.5, 2, 1, 1, 0.1, 1, 2, 1)