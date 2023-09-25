from math import sqrt

class Tuples:

    x = y = z = w = 0.0
    EPSILON = 0.00001

    def __init__(self, x=0.0, y=0.0, z=0.0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def Vector(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0.0
        return self

    def Point(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1.0
        return self

    def isPoint(self):
        if self.w == 1.0:
            return True
        return False
    
    def isVector(self):
        if self.w == 0.0:
            return True
        return False
    
    def equal(self, a, b):
        if abs(a-b) < self.EPSILON:
            return True
        return False
    
    def __eq__(self, t):
        if t == None:
            return False
        if self.equal(self.x, t.x) and self.equal(self.y, t.y) and self.equal(self.z, t.z) and self.equal(self.w, t.w):
            return True
        return False
        
    def __add__(self, t):
        t1 = Tuples()
        t1.x = self.x + t.x
        t1.y = self.y + t.y
        t1.z = self.z + t.z
        t1.w = self.w + t.w
        return t1
    
    def __sub__(self, t):
        t1 = Tuples()
        t1.x = self.x - t.x
        t1.y = self.y - t.y
        t1.z = self.z - t.z
        t1.w = self.w - t.w
        return t1
    
    def __mul__(self, scalar):
        t1 = Tuples()
        t1.x = self.x * scalar
        t1.y = self.y * scalar
        t1.z = self.z * scalar
        t1.w = self.w * scalar
        return t1
    
    def __truediv__(self, scalar):
        t1 = Tuples()
        t1.x = self.x / scalar
        t1.y = self.y / scalar
        t1.z = self.z / scalar
        t1.w = self.w / scalar
        return t1
    
    def __neg__(self):
        t1 = Tuples()
        t1.x = -self.x 
        t1.y = -self.y 
        t1.z = -self.z 
        t1.w = -self.w 
        return t1
    
    def __str__(self):
        return "X: "+str(self.x)+"\nY: "+str(self.y)+"\nZ: "+str(self.z)+"\nW: "+str(self.w)
    
    def magnitude(self):
        return sqrt(pow(self.x,2)+ pow(self.y, 2) + pow(self.z, 2) + pow(self.w, 2))
    
    def normalize(self):
        t1 = Tuples()
        t1.x = self.x / self.magnitude()
        t1.y = self.y / self.magnitude()
        t1.z = self.z / self.magnitude()
        t1.w = self.w / self.magnitude()
        return t1
    
    def dot(self, t1, t2 = None):
        if t2 != None:
            return (t1.x*t2.x) + (t1.y*t2.y) + (t1.z*t2.z) + (t1.w*t2.w)
        else: 
            return (self.x*t1.x) + (self.y*t1.y) + (self.z*t1.z) + (self.w*t1.w)
    
    def cross(self, t1):
        return Tuples().Vector((self.y*t1.z) - (self.z*t1.y), (self.z*t1.x) - (self.x*t1.z), (self.x*t1.y) - (self.y*t1.x))
    
    def reflect(self, tNormal):
        return self - tNormal * 2 * self.dot(tNormal)