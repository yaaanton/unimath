'''
Вар. № 24.
'''
import numpy as np


def make_identity(matrix):
    # перебор строк в обратном порядке
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor*row
    return matrix


def gaussPivotFunc(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow] # диагональный элемент
        if abs(divider) < 1e-10:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            raise ValueError(f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}")
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow] # элемент строки в колонке nrow
            lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    # приводим к диагональному виду
    make_identity(matrix)
    return matrix


A = np.array([[0.3, 0.5, 0.2, 0.3],
              [0.1, 0.2, 0.4, 0.1],
              [0.2, 0.2, 0.2, 0.3],
              [0.4, 0.1, 0.2, 0.3]])

E = np.eye(4)
AEdiff=A-E
print(f'gauss matrix: \n{gaussPivotFunc(AEdiff)}')


S = 52920


print(E)
B = np.array([0, 0, 0, 0])


SLAU=A-E
print(f'SLAU MASSIV: \n{SLAU}')

#X = np.linalg.solve(SLAU, B)

print ("Матрица A:\n", A)
print ("Вектор B:\n", B)
#print ("Решение системы:\n", X)

