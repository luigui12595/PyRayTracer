import math
from .matrix import Matrix 

class Transformations:

    @staticmethod
    def translation(x, y, z):
        translation = Matrix(4,4)
        translation = translation.identity()
        translation[0][3] = x
        translation[1][3] = y
        translation[2][3] = z
        return translation

    @staticmethod
    def scaling(x, y, z):
        scaling = Matrix(4,4)
        scaling = scaling.identity()
        scaling[0][0] = x
        scaling[1][1] = y
        scaling[2][2] = z
        return scaling

    @staticmethod
    def rotation_x(radians):
        rotation = Matrix(4,4)
        rotation = rotation.identity()
        rotation[1][1] = math.cos(radians)
        rotation[1][2] = -math.sin(radians)
        rotation[2][1] = math.sin(radians)
        rotation[2][2] = math.cos(radians)
        return rotation

    @staticmethod
    def rotation_y(radians):
        rotation = Matrix(4,4)
        rotation = rotation.identity()
        rotation[0][0] = math.cos(radians)
        rotation[0][2] = math.sin(radians)
        rotation[2][0] = -math.sin(radians)
        rotation[2][2] = math.cos(radians)
        return rotation

    @staticmethod
    def rotation_z(radians):
        rotation =  Matrix(4,4)
        rotation = rotation.identity()
        rotation[0][0] = math.cos(radians)
        rotation[0][1] = -math.sin(radians)
        rotation[1][0] = math.sin(radians)
        rotation[1][1] = math.cos(radians)
        return rotation

    @staticmethod
    def shearing(xy, xz, yx, yz, zx, zy):
        shearing = Matrix(4,4)
        shearing = shearing.identity()
        shearing[0][1] = xy
        shearing[0][2] = xz
        shearing[1][0] = yx
        shearing[1][2] = yz
        shearing[2][0] = zx
        shearing[2][1] = zy
        return shearing
    
    @staticmethod
    def view_transform(pfrom, to, up):
        forward = (to - pfrom).normalize()
        upn  = up.normalize()
        left = forward.cross(upn)
        true_up = left.cross(forward)
        orientation = Matrix(4,4).identity()
        orientation[0][0] = left.x
        orientation[0][1] = left.y
        orientation[0][2] = left.z
        
        orientation[1][0] = true_up.x
        orientation[1][1] = true_up.y
        orientation[1][2] = true_up.z
        
        orientation[2][0] = -forward.x
        orientation[2][1] = -forward.y
        orientation[2][2] = -forward.z
        
        return orientation * Transformations().translation(-pfrom.x, -pfrom.y, -pfrom.z)