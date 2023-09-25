import math
from typing import List
from .rays import Rays 
from .tuples import Tuples
from .worlds import Worlds

class Intersection:

    def __init__(self, t=0, obj=None):
        self.t = t
        self.obj = obj

    def intersect(self, s, ray):
        ray2 = self.transform(ray, s.transform.inverse())
        point = Tuples().Point(0, 0, 0)
        v = []
        sphereToRay = ray2.origin - point
        a = Tuples().dot(ray2.direction, ray2.direction)
        b = 2 * Tuples().dot(ray2.direction, sphereToRay)
        c = Tuples().dot(sphereToRay, sphereToRay) - 1
        discriminant = math.pow(b, 2) - (4 * a * c)       
        if discriminant >= 0:
            int1 = Intersection((-b - math.sqrt(discriminant)) / (2 * a), s)
            int2 = Intersection((-b + math.sqrt(discriminant)) / (2 * a), s)
            v.append(int1)
            v.append(int2)
        return v

    def intersect_world(self, w: Worlds, ray: Rays):
        v = []
        for obj in w.objects:
            result = Intersection().intersect(obj, ray)
            for i in result:
                v.append(i)
        v.sort(key=lambda x: x.t)
        return v

    def __lt__(self, i1):
        return self.t < i1.t

    def intersections(*args):
        v = []
        for inter in args:
            v.append(inter)
        return v

    def hit(self, ints: List["Intersection"]):
        lowest = 1e10
        ans = False
        selected = Intersection()
        for inter in ints:
            if inter.t < lowest and inter.t >= 0:
                ans = True
                selected.obj = inter.obj
                selected.t = inter.t
                lowest = selected.t
        if ans:
            return selected
        else:
            return None

    def __eq__(self, inter):
        return self.t == inter.t and self.obj.id == inter.obj.id

    def transform(self, ray, m):
        new_origin = m * ray.origin
        new_direction = m * ray.direction
        return Rays(new_origin, new_direction)