import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt



def random_line(size ,start, max, max_angle, smoothness, noise):
    #TODO: replace this test code

    # d2 = np.random.normal(scale=1, size=size)
    d2 = np.random.random(size=size)-0.5
    d1 = integral(d2*5)
    d = integral(d1)
    y = d+(start-d.min())
    return y, d1, d2


def integral(line):
    ia = np.zeros(line.shape[0])
    for i, d in enumerate(line):
        ia[i] = ia[i-1]+d
    return ia


def sine(length=1000, amplitude=1.0, frequency=1.0, shift=0):
    x = (np.arange(length)+shift)*2*np.pi*(frequency/1000.0)
    y = amplitude * np.sin(x)
    return y

def show_line(line):
    return show_lines((line, ))

def show_lines(lines):

    x = np.arange(lines[0].shape[0])
    fig, ax = plt.subplots()
    ls = []
    for line in enumerate(lines):
        col = np.random.rand(3)
        axn = plt.twinx(ax)
        ls.append(axn.plot(x, line, c=col))
    plt.legend(handles=ls)
    plt.show()


def pendulum(momentum_curve, min, max, max_angle=45.0):
    angle = np.cumsum(momentum_curve)
    #angle bias
    # w = angle.max()-angle.min()
    # c = angle.min()+0.5*w
    # angle = angle-c
    # angle = angle*45/(0.5*w)
    max = np.abs(angle).max()
    angle = angle*45/max
    #
    dy = np.tan(np.radians(angle))
    y = np.cumsum(dy)

    plt.plot(momentum_curve, "black")
    plt.plot(y, "r")
    plt.show()
    return y


def quadratic_factory(a, b, c):
    def quadratic(x):
        y = a*x**2 + b*x + c
        return y

    return quadratic

if __name__ == "__main__":
    s1 = sine(length=3000, amplitude=0.2, frequency=0.6)
    s2 = sine(length=3000, amplitude=0.5, frequency=1)
    s3 = sine(length=3000, amplitude=0.8, frequency=1.8)
    mom = s1+s2*s3

    l = pendulum(mom, 1, 2)

    # show_lines((l, mom))