EPSILON = 0.00001
class Colors:
    
    r=g=b=0

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def equals(ab, ba):
        return abs(ab - ba) < EPSILON

    def __eq__(self, other):
        print(str(self))
        print(str(other))
        return (
            Colors.equals(self.r, other.r) and
            Colors.equals(self.g, other.g) and
            Colors.equals(self.b, other.b)
        )

    def __add__(self, other):
        return Colors(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Colors(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Colors(self.r * other, self.g * other, self.b * other)
        elif isinstance(other, Colors):
            return Colors(self.r * other.r, self.g * other.g, self.b * other.b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"Colors({self.r}, {self.g}, {self.b})"