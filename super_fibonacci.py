import numpy as np



def matrix_expn(x, n):
    print(n)
    print(x)
    if n == 1:
        return x
    if n % 2 == 0:
        return matrix_expn(np.matmul(x, x), n // 2)
    return np.matmul(x, matrix_expn(np.matmul(x, x), n // 2))

A = np.array([[1, 1],
              [1, 0]])
v_init = np.array([1, 0])

y = 1000
print(matrix_expn(A, y-1))
