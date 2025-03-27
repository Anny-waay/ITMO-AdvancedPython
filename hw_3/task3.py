import numpy as np


class Hash:
    # Хэш от суммы элементов и формы матрицы
    def __hash__(self):
        return hash((np.sum(self.data), self.data.shape))


class MatrixIO:
    def __str__(self):
        np.array2string(self.data)

    def write_to_file(self, file_path):
        with open(file_path, "a") as file:
            file.write(f"{self.data}\n")


class Matrix(Hash, MatrixIO):
    def __init__(self, data):
        self.data = np.array(data)

    def __matmul__(self, other):
        hash_key = (hash(self), hash(other))
        if hash_key not in self.__class__._cache:
            res = np.dot(self.data, other.data)
            self.__class__._cache[hash_key] = Matrix(res)
        return self.__class__._cache[hash_key]

    def real_matmul(self, other):
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(len(other.data)))
             for j in range(len(other.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    _cache = {}


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
C = Matrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
D = B

A.write_to_file("artifacts/task3/A.txt")
B.write_to_file("artifacts/task3/B.txt")
C.write_to_file("artifacts/task3/C.txt")
D.write_to_file("artifacts/task3/D.txt")

A_B = A @ B
C_D = C @ D

A_B.write_to_file("artifacts/task3/AB.txt")
(C.real_matmul(D)).write_to_file("artifacts/task3/CD.txt")

with open("artifacts/task3/hash.txt", "w") as file:
    file.write(f"Hash of AB: {hash(A_B)}\nHash of CD: {hash(C_D)}")
