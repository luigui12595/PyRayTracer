from .tuples import Tuples
EPSILON = 0.00001
class Matrix:
    

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = [[0] * cols for _ in range(rows)]
    

    @staticmethod
    def equals(a, b):
        return abs(a - b) < EPSILON

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
            for j in range(self.cols):              
                if not self.equals(self.mat[i][j], other.mat[i][j]):
                    return False
        return True


    def __str__(self):
        str_matrix=""
        for i in range(self.rows):
            for j in range(self.cols):
                str_matrix += str(self.mat[i][j])+" "
            str_matrix += "\n"
        return str_matrix
                
    def __getitem__(self, index):
        return self.mat[index]

    def __setitem__(self, index, value):
        self.mat[index] = value

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                return Matrix(0, 0)
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result[i][j] = sum(self[i][k] * other[k][j] for k in range(self.cols))
            return result
        elif isinstance(other, Tuples):
            if self.cols != 4:
                return Tuples()
            result = Tuples(0, 0, 0, 0)
            for i in range(self.rows):
                if i == 0:
                    result.x = self[i][0] * other.x + self[i][1] * other.y + self[i][2] * other.z + self[i][3] * other.w
                elif i == 1:
                    result.y = self[i][0] * other.x + self[i][1] * other.y + self[i][2] * other.z + self[i][3] * other.w
                elif i == 2:
                    result.z = self[i][0] * other.x + self[i][1] * other.y + self[i][2] * other.z + self[i][3] * other.w
                elif i == 3:
                    result.w = self[i][0] * other.x + self[i][1] * other.y + self[i][2] * other.z + self[i][3] * other.w
            return result

    def identity(self):
        if self.rows != self.cols:
            return Matrix(0, 0)
        identity = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                identity[i][j] = 1 if i == j else 0
        return identity

    def transposing(self):
        transposed = Matrix(self.rows, self.cols)
        for i in range(self.cols):
            for j in range(self.rows):
                transposed[i][j] = self[j][i]
        return transposed

    def determinant(self):
        if self.rows != self.cols:
            return 0
        if self.rows == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        det = 0
        for col in range(self.cols):
            det += self[0][col] * self.cofactor(0, col)
        return det

    def submatrix(self, row, col):
        sub = Matrix(self.rows - 1, self.cols - 1)
        r_idx = 0
        for r in range(self.rows):
            if r == row:
                continue
            c_idx = 0
            for c in range(self.cols):
                if c == col:
                    continue
                sub[r_idx][c_idx] = self[r][c]
                c_idx += 1
            r_idx += 1
        return sub

    def minor(self, row, col):
        sub = self.submatrix(row, col)
        return sub.determinant()

    def cofactor(self, row, col):
        minor = self.minor(row, col)
        return minor if (row + col) % 2 == 0 else -minor

    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        if not self.is_invertible():
            return Matrix(0, 0)
        det = self.determinant()
        m2 = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                cof = self.cofactor(r, c)
                m2[c][r] = cof / det
        return m2