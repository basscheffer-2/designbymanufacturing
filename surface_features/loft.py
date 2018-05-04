import numpy as np

from shapely.geometry.polygon import Polygon

def loft_between_polylines(profiles):

    if isinstance(profiles[0], Polygon):
        _new_prof = []
        for _prof in profiles:
            _new_prof.append(np.array([[_p[0], _p[1]] for _p in _prof.exterior.coords]))

    poly_size_list = [pl.n_points for pl in profiles]
    if max(poly_size_list) != min(poly_size_list):
        raise NameError('can\'t create a loft between polylines with unequal number of segments')

    vertices = np.concatenate([poly.points for poly in profiles])

    n_verts = poly_size_list[0]
    n_profs = len(poly_size_list)

    tri_list = []
    for i in range(n_profs-1):
        p1_ix = np.arange(i*n_verts, (i+1)*n_verts)
        p2_ix = np.arange((i+1)*n_verts, (i+2)*n_verts)

        # tris1 = np.stack((p1_ix, np.roll(p2_ix, -1), p2_ix), axis=1)
        # tris2 = np.stack((p1_ix, p2_ix, np.roll(p1_ix, 1)), axis=1)

        tris1 = np.stack((p2_ix, np.roll(p2_ix, -1), p1_ix), axis=1)
        tris2 = np.stack((np.roll(p1_ix, 1), p2_ix, p1_ix), axis=1)

        tris = np.concatenate((tris1, tris2))

        tri_list.append(tris)

    faces = np.concatenate(tri_list)

    return vertices, faces