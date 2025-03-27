import numpy as np


class Matrix:
    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def _check_matrix_instance(self, other):
        if not all(len(x) == len(self.matrix[0]) for x in self.matrix):
            raise ValueError("Все строки матрицы должны содержать одинаковое количество чисел")
        if not all(len(x) == len(other.matrix[0]) for x in other.matrix):
            raise ValueError("Все строки матрицы должны содержать одинаковое количество чисел")

    def _check_matrix_elements(self, other):
        for i in range(len(self.matrix)):
            if not all([isinstance(x, np.int32) or isinstance(x, np.float) for x in self.matrix[i]]):
                raise ValueError("Элементы матриц должны быть числами")
        for i in range(len(other.matrix)):
            if not all([isinstance(x, np.int32) or isinstance(x, np.float) for x in other.matrix[i]]):
                raise ValueError("Элементы матриц должны быть числами")

    def __add__(self, other):
        self._check_matrix_instance(other)
        self._check_matrix_elements(other)
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError(
                f"Невозможно выполнить сложение матриц размерностями {len(self.matrix)}x{len(self.matrix[0])} и {len(other.matrix)}x{len(other.matrix[0])}"
            )
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        self._check_matrix_instance(other)
        self._check_matrix_elements(other)
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError(
                f"Невозможно выполнить умножение матриц размерностями {len(self.matrix)}x{len(self.matrix[0])} и {len(other.matrix)}x{len(other.matrix[0])}"
            )
        result = [
            [self.matrix[i][j] * other.matrix[i][j]
             for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __matmul__(self, other):
        self._check_matrix_instance(other)
        self._check_matrix_elements(other)
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                f"Невозможно выполнить умножение матриц размерностями {len(self.matrix)}x{len(self.matrix[0])} и {len(other.matrix)}x{len(other.matrix[0])}"
            )
        result = [
            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix)))
             for j in range(len(other.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __str__(self):
        return "\n".join(" ".join(f"{value:3d}" for value in row) for row in self.matrix)


def write_to_file(matrixes, file_path):
    with open(file_path, "w") as file:
        for title, matrix in zip(["Matrix 1", "Matrix 2", "Operation result"], matrixes):
            file.write(f"{title}\n")
            file.write(f"{matrix}\n\n")


np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

write_to_file([matrix1, matrix2, matrix1 + matrix2], "artifacts/task1/matrix+.txt")
write_to_file([matrix1, matrix2, matrix1 * matrix2], "artifacts/task1/matrix_mul.txt")
write_to_file([matrix1, matrix2, matrix1 @ matrix2], "artifacts/task1/matrix@.txt")
