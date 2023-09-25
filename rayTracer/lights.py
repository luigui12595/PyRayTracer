from .tuples import Tuples  
from .colors import Colors 

class Lights:
    
    def __init__(self):
        self.position = Tuples(0, 0, 0)
        self.intensity = Colors(0, 0, 0)

    def point_light(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def __eq__(self, l2):
        print(l2)
        return self.position == l2.position and self.intensity == l2.intensity

    @staticmethod
    def lighting(material, light, point, eyev, normalv):
        effectiveColor = material.color * light.intensity
        lightv = (light.position - point).normalize()
        ambient = effectiveColor * material.ambient
        lightDotNormal = lightv.dot(normalv)
        diffuse, specular = Colors(0, 0, 0), Colors(0, 0, 0)
        if lightDotNormal < 0:
            diffuse = Colors(0, 0, 0)
            specular = Colors(0, 0, 0)
        else:
            diffuse = effectiveColor * material.diffuse * lightDotNormal
            reflectv = (-lightv).reflect(normalv)
            reflectDotEye = reflectv.dot(eyev)
            if reflectDotEye <= 0:
                specular = Colors(0, 0, 0)
            else:
                factor = reflectDotEye ** material.shininess
                specular = light.intensity * material.specular * factor
        return ambient + diffuse + specular