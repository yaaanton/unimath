'''
Производственная сфера народного хозяйства состоит из трёх отраслей и
характеризуется структурной матрицей A . Рассчитать равновесные цены по отраслям при заданном векторе норм добавленной стоимости
(v1, v2 , v3 ). Как изменятся цены на продукцию, если норму добавленной стоимости по i -й отрасли увеличить на p % ?
'''
import numpy as np

a11 = 0.1;   a12 = 0.2;   a13 = 0.3
a21 = 0.2;   a22 = 0.3;   a23 = 0.4
a31 = 0.3;   a32 = 0.2;   a33 = 0.2

v1 = 7
v2 = 10
v3 = 4

i = 2
p = 3 # в %

V = np.array([v1, v2, v3])

A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])

''' матрица полных затрат '''
E = np.eye(3)
print(f'E:\n{E}')
print(f'E-A:\n{E-A}')

detEA = np.linalg.det(E-A)
print(f'det(E-A) = {detEA}')
print('нужно найти матрицу алгебраических дополнений но хуй с ней')

S = np.linalg.inv(E-A)
STranspose = np.transpose(S)
print(f'обратная матрица S \n {S}')
print(f'транспонированая обратная матрица S \n {STranspose}')
P = np.dot(STranspose, V)


print(f'Теперь по заданному вектору норм добавленной стоимости v находим вектор равновесных цен \n{P}')
print(f'V:{V}\n(E-A)T^-1\n{STranspose}\nP:\n{P}')

V1 = np.array([V[0],V[1]*1.03,V[2]])
print(f'V1:{V1} ')
P1 = np.dot(STranspose,V1)
print(f'P1: {P1} \n')