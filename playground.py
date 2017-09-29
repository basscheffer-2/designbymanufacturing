from surface_features import loft
import polylines as poly
import viewers
import numpy as np


def polygon():
    circle1 = poly.Circle(1.5, 0.5, 45)
    print circle1.points.__len__()
    viewers.polylineviewer(circle1)

if __name__=='__main__':
    polygon()