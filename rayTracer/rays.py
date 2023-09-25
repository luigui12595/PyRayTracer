from .tuples import Tuples  

class Rays:
    
    def __init__(self, ori = None, dir = None):
        if(ori == None or dir == None):
            self.origin = Tuples(0, 0, 0, 0)
            self.direction = Tuples(0, 0, 0, 0)
        else:
            self.direction = Tuples(dir.x, dir.y, dir.z, dir.w)
            self.origin = Tuples(ori.x, ori.y, ori.z, ori.w)   

    def position(self, t):
        return self.origin + (self.direction * t)