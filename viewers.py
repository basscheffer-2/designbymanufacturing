import numpy as np
from matplotlib.patches import Polygon, Circle
from matplotlib import pyplot as plt

def polylineviewer(polyline, closed=False):

    fig, ax = plt.subplots(1, figsize=(6, 6))
    pol = Polygon(polyline.points, closed)
    ax.add_patch(pol)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.grid()

    plt.show()