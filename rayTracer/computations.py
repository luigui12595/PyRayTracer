from .intersection import Intersection 
from .lights import Lights 
from .tuples import Tuples 
from .colors import Colors 

EPSILON = 0.0001

class Computations:

    def __init__(self):
        pass

    def prepare_computations(self, i, r):
        comps = Computations()
        comps.t = i.t
        comps.object = i.obj

        comps.point = r.position(comps.t)
        comps.eyev = -r.direction
        comps.normalv = comps.object.normal_at(comps.point)

        if Tuples().dot(comps.normalv, comps.eyev) < 0:
            comps.inside = True
            comps.normalv = -comps.normalv
        else:
            comps.inside = False
        comps.over_point = comps.point + comps.normalv * EPSILON
        return comps


    def shade_hit(self, w, comps):
        shadowed = w.is_shadowed(comps.over_point)
        l = Lights()
        return l.lighting(comps.object.material, w.light, comps.over_point, comps.eyev, comps.normalv, shadowed)

    def color_at(self, w, r):
        inter = Intersection()
        inters = inter.intersect_world(w, r)
        i = inter.hit(inters)
        if i is None:
            return Colors(0, 0, 0)
        else:
            comps = self.prepare_computations(i, r)
            color = self.shade_hit(w, comps)
            return color