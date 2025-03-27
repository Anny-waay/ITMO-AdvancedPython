import numpy as np


class MatrixOperations:
    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __matmul__(self, other):
        return self.__class__(self.data @ other.data)

class MatrixIO:
    def __str__(self):
        np.array2string(self.data)

    def write_to_file(self, file_path):
        with open(file_path, "a") as file:
            file.write(f"{self.data}\n")


class MatrixWithNp(MatrixOperations, MatrixIO):
    def __init__(self, data):
        self.data = np.array(data)

    @property
    def matrix(self):
        return self.matrix

    @matrix.setter
    def matrix(self, data):
        self.data = np.array(data)


def write_to_file(matrixes, file_path):
    for title, matrix in zip(["Matrix 1", "Matrix 2", "Operation result"], matrixes):
        with open(file_path, "a") as file:
            file.write(f"{title}\n")
        matrix.write_to_file(file_path)


np.random.seed(0)
matrix1 = MatrixWithNp(np.random.randint(0, 10, (10, 10)))
matrix2 = MatrixWithNp(np.random.randint(0, 10, (10, 10)))

write_to_file([matrix1, matrix2, matrix1 + matrix2], "artifacts/task2/matrix+.txt")
write_to_file([matrix1, matrix2, matrix1 * matrix2], "artifacts/task2/matrix_mul.txt")
write_to_file([matrix1, matrix2, matrix1 @ matrix2], "artifacts/task2/matrix@.txt")
