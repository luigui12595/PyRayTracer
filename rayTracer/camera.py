from .matrix import Matrix
from .tuples import Tuples
from .rays import Rays
from .canvas import Canvas
from .computations import Computations

import math

class Camera:
    
    hsize = vsize = field_of_view = pixel_size = half_width = half_height = 0
    
    transform = Matrix(4,4)
    
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = self.transform.identity()
        
        half_view = math.tan(self.field_of_view/2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else: 
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width*2)/self.hsize
        
    def ray_for_pixel(self, px, py):
        xoffset = ( px + 0.5 ) * self.pixel_size
        yoffset = ( py + 0.5 ) * self.pixel_size
        
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset
        
        pixel = self.transform.inverse() * Tuples().Point(world_x, world_y, -1)
        origin = self.transform.inverse() * Tuples().Point(0, 0, 0)
        direction = (pixel - origin).normalize()
        return Rays(origin, direction)
    
    def render(self, world):
        image  =  Canvas(self.hsize, self.vsize)
        for y in range(self.vsize - 1):
            for x in range(self.hsize - 1):
                ray  = self.ray_for_pixel(x, y)
                color = Computations().color_at(world, ray)
                image.write_pixel(x,y,color)
        return image