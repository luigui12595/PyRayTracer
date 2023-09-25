from .matrix import Matrix
from .tuples import Tuples  
from .materials import Materials

class Sphere:

    IDSeed = 0
    transform = Matrix(4,4)
    material = Materials()

    def __init__(self):
        self.id = self.helper_seed()
        self.transform = Matrix(4,4).identity()
        self.material = Materials()

    @staticmethod
    def helper_seed():
        Sphere.IDSeed += 1
        return Sphere.IDSeed

    def set_transform(self, t):
        self.transform = t
        return self

    def normal_at(self, world_point):
        object_point = self.transform.inverse() * world_point
        object_normal = object_point - Tuples().Point(0, 0, 0)
        world_normal:Tuples = self.transform.inverse().transposing() * object_normal
        world_normal.w = 0
        return world_normal.normalize()

    def __eq__(self, other):
        return self.material == other.material and self.transform == other.transform