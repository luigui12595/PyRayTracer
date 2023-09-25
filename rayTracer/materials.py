from .colors import Colors

class Materials:
    
    def __init__(self):
        self.color = Colors(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200

    def __eq__(self, m2):
        return (
            self.ambient == m2.ambient and
            self.diffuse == m2.diffuse and
            self.specular == m2.specular and
            self.shininess == m2.shininess and
            self.color == m2.color
        )

    def __copy__(self, m2):
        self.color = m2.color
        self.ambient = m2.ambient
        self.diffuse = m2.diffuse
        self.specular = m2.specular
        self.shininess = m2.shininess