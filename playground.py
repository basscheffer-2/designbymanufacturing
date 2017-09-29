from surface_features import loft
import polylines as poly
# import viewers
import numpy as np
import trimesh


def polygon():
    circle1 = poly.Circle(1.5)
    print circle1.points.__len__()
    # viewers.polylineviewer(circle1)

def trimesh_test():
    # import trimesh
    m = trimesh.load_mesh('models/ballA.off')
    m.show()

def loft_test():
    circle1 = poly.Circle(1.5)
    circle2 = poly.Circle(1.5)
    v, f = loft.loft_between_polylines([circle1, circle2])
    m = trimesh.Trimesh(vertices=v, faces=f, process=False, validate_faces=False)
    m.show()

if __name__=='__main__':
    # polygon()
    # trimesh_test()
    loft_test()