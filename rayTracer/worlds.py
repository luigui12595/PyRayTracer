from .lights import Lights
from .tuples import Tuples
from .colors import Colors
from .materials import Materials
from .sphere import Sphere
from .transformations import Transformations

class Worlds:
    def __init__(self):
        self.light = Lights()
        self.objects = []

    def default_world(self):
        light = Lights()
        point = Tuples().Point(-10, 10, -10)
        color = Colors(1, 1, 1)
        light.point_light(point, color)
        self.light = light

        material = Materials()
        material.color = Colors(0.8, 1.0, 0.6)
        material.diffuse = 0.7
        material.specular = 0.2

        s1 = Sphere()
        s1.material = material

        trans = Transformations()
        s2 = Sphere()
        s2.set_transform(trans.scaling(0.5, 0.5, 0.5))

        self.objects.append(s1)
        self.objects.append(s2)
        return self