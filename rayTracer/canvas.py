import copy
from .colors import Colors

class Canvas:
    
    width = height = 0 
    
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        if color is None:
            color = Colors(0, 0, 0)
        else:
            color = color * 255
        self.pixel_grid = []
        for i in range(height):
            rowList = []
            for j in range(width):
                rowList.append(copy.deepcopy(color))
            self.pixel_grid.append(rowList)

    def write_pixel(self, x, y, color):
        n_color = color * 255
        if color.r > 1:
            self.pixel_grid[y][x].r = 255
        elif color.r < 0:
            self.pixel_grid[y][x].r = 0
        else:
            self.pixel_grid[y][x].r = round(n_color.r)

        if color.g > 1:
            self.pixel_grid[y][x].g = 255
        elif color.g < 0:
            self.pixel_grid[y][x].g = 0
        else:
            self.pixel_grid[y][x].g = round(n_color.g)

        if color.b > 1:
            self.pixel_grid[y][x].b = 255
        elif color.b < 0:
            
            self.pixel_grid[y][x].b = 0
        else:
            self.pixel_grid[y][x].b = round(n_color.b)  
        


    def pixel_at(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixel_grid[y][x]

    def canvas_to_ppm(self, filename):
        with open(filename, "w") as ppm_file:
            ppm_file.write("P3\n")
            ppm_file.write(f"{self.width} {self.height}\n")
            ppm_file.write("255\n")
            chars = 0
            for id, row in enumerate(self.pixel_grid):
                for color in row:
                    chars += len(str(int(color.r))) + 1
                    if chars >= 70:
                        ppm_file.write("\n")
                        chars = 0
                    ppm_file.write(str(int(color.r))+" ")
                    chars += len(str(int(color.g))) + 1
                    if chars >= 70:
                        ppm_file.write("\n")
                        chars = 0
                    ppm_file.write(str(int(color.g))+" ")
                    chars += len(str(int(color.b))) + 1
                    if chars >= 70:
                        ppm_file.write("\n")
                        chars = 0
                    ppm_file.write(str(int(color.b))+" ")
                ppm_file.write("\n")
                chars = 0