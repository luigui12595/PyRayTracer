from .intersection import Intersection 
from .lights import Lights 
from .tuples import Tuples 
from .colors import Colors 

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
        return comps


    def shade_hit(self, w, comps):
        l = Lights()
        return l.lighting(comps.object.material, w.light, comps.point, comps.eyev, comps.normalv)

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