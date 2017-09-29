import numpy as np

class Polyline(object):

    #TODO: points, edges, invert, size, centroid/cog, convex/concave, box
    def __init__(self, xy=np.zeros((0, 2))):
        self.points = xy
        self.n_points = self.points.__len__()

    def append(self, xy):
        self.insert(xy, -1)

    def insert(self, xy, before_point):
        pass

    def scale(self):
        pass

    def rotate(self):
        pass

    def to_vertices(self, Z=None):
        pass

class Polygon(Polyline):

    def __init__(self, n_sides=3, radius=1):
        if n_sides < 3:
            raise NameError('minimum of 3 sides required for polygon')
        xy = np.zeros(shape=(np.int(n_sides), 2))
        angles = np.arange(0, 360, 360.0/n_sides)
        xy[:, 0] = np.sin(np.radians(angles)) * radius
        xy[:, 1] = np.cos(np.radians(angles)) * radius

        super(Polygon, self).__init__(xy)

class Circle(Polygon):

    def __init__(self, radius=1, tolerance=0.1, min_angle=3.0):
        self.radius = radius
        self.tolerance = tolerance
        self.min_angle = min((min_angle, self._calc_min_angle()))
        super(Circle, self).__init__(n_sides=np.ceil(360/self.min_angle), radius=self.radius)

    def _calc_min_angle(self):
        return 2*np.degrees(np.arccos((1-self.tolerance/self.radius)))
