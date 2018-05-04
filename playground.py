from surface_features import loft
import polylines as poly
# import viewers
import numpy as np
import trimesh
from trimesh.creation import triangulate_polygon
from shapely.geometry.polygon import Polygon as shp
# from trimesh.path import path
from trimesh.path import path
from trimesh.path import entities
from trimesh.util import three_dimensionalize
from trimesh.boolean import union

def polygon():
    circle1 = poly.Circle(1.5)
    print circle1.points.__len__()
    # viewers.polylineviewer(circle1)

def trimesh_test():
    # import trimesh
    m = trimesh.load_mesh('models/ballA.off')
    m.show()


def loft_test():
    p0 = shp(shell=three_dimensionalize(poly.Circle(1.5).points, return_2D=False))
    p1 = shp(shell=three_dimensionalize(poly.Circle(2).points, return_2D=False))

    t = [[_p[0], _p[1]] for _p in p0.exterior.coords]

    b = shp(shell=[[_p[0], _p[1]] for _p in p0.exterior.coords])

    v_b, t_b = triangulate_polygon(b)
    v_s, t_s = loft.loft_between_polylines([p0, p1])

    t_s += v_b.shape[0]

    v = np.stack((v_b, v_s))
    f = np.stack((t_s, t_b))

    m = trimesh.Trimesh(vertices=v, faces=f, process=True, validate_faces=True)

    with open("loft_test.stl", "wb") as fh:
        m.export(fh, "stl")

    # m.show()

def triangulate_poly():
    circle1 = poly.Circle(1.5)
    p = shp(shell=circle1.points)
    x = triangulate_polygon(p)
    return x

def trimesh_extrusion():
    coord = [[0, 0], [2, 0], [1, 2]]
    points = [0, 1, 2, 0]
    ent = entities.Line(points)

    pth = path.Path2D([ent], coord)
    msh = pth.extrude(1)

    msh.show()



if __name__=='__main__':
    # polygon()
    # trimesh_test()
    loft_test()
    # triangulate_poly()
    #trimesh_extrusion()