'''
Вар. № 24.
'''
import numpy as np

A = np.array([[0.2, 0.5, 0.3, 0.3],
              [0.2, 0.1, 0.4, 0.3],
              [0.4, 0.2, 0.1, 0.1],
              [0.2, 0.2, 0.2, 0.3]])

E=np.eye(4)

S = 52920

B = np.array([0, 0, 0, 0])
X = np.linalg.solve(A, B)

print ("Матрица A:\n", A)
print ("Матрица A-E:\n", A-E)


print ("Вектор b:\n", B)
print ("Решение системы:\n", X)

