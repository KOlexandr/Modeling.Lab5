__author__ = 'KOL'

import pylab


def euler(function, x0, dt=0.01, all_steps=1000):
    t = pylab.zeros(all_steps)
    x = pylab.zeros(all_steps)

    x[0] = x0
    t[0] = 0
    for i in range(0, all_steps-1):
        x[i+1] = x[i] + dt*(function(x[i]))
        t[i+1] = t[i] + dt
    return t, x


def euler_system(function_x, function_y, x0, y0, dt=0.001, all_steps=1000):
    t = pylab.zeros(all_steps)
    x = pylab.zeros(all_steps)
    y = pylab.zeros(all_steps)
    x[0] = x0
    y[0] = y0
    t[0] = 0
    for i in range(0, all_steps-1):
        x[i+1] = x[i] + dt*(function_x(x[i], y[i]))
        y[i+1] = y[i] + dt*(function_y(x[i], y[i]))
        t[i+1] = t[i] + dt
    return t, x, y


def euler_system3(function_x, function_y, function_z, x0, y0, z0, dt=0.001, all_steps=1000):
    t = pylab.zeros(all_steps)
    x = pylab.zeros(all_steps)
    y = pylab.zeros(all_steps)
    z = pylab.zeros(all_steps)
    x[0] = x0
    y[0] = y0
    z[0] = z0
    t[0] = 0
    for i in range(0, all_steps-1):
        x[i+1] = x[i] + dt*(function_x(x[i], y[i], z[i]))
        y[i+1] = y[i] + dt*(function_y(x[i], y[i], z[i]))
        z[i+1] = z[i] + dt*(function_z(x[i], y[i], z[i]))
        t[i+1] = t[i] + dt
    return t, x, y, z