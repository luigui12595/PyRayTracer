from rayTracer.canvas import Canvas
from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection
from rayTracer.lights import Lights
from rayTracer.sphere import Sphere
from rayTracer.materials import Materials

def main():
    ray_origin = Tuples().Point(0, 0, -5)

    wall_z = 10
    wall_size = 7

    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = Canvas(canvas_pixels, canvas_pixels)
    color = Colors(1, 0, 0)

    shape = Sphere()
    mat = Materials()
    shape.material = mat
    material_color = Colors(1, 0.2, 1)
    shape.material.color = material_color

    light_position = Tuples().Point(-10, 10, -10)
    light_color = Colors(1, 1, 1)
    light = Lights()
    light.point_light(light_position, light_color)

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x
            position = Tuples().Point(world_x, world_y, wall_z)
            direction = (position - ray_origin).normalize()
            r = Rays(ray_origin, direction)
            inter = Intersection()
            xs = inter.intersect(shape, r)
            hit = inter.hit(xs)
            if hit is not None:
                point = r.position(hit.t)
                normal = shape.normal_at(point)
                eye = -r.direction
                color = light.lighting(hit.obj.material, light, point, eye, normal)
                canvas.write_pixel(x, y, color)

    canvas.canvas_to_ppm("purpleCircle.ppm")
    

if __name__ == "__main__":
    main()