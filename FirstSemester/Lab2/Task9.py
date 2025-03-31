# Простой метод умножения матриц
def simple_matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# Метод Штрассена
def strassen(A, B):
    n = len(A)
    if n == 1:  # Базовый случай
        return [[A[0][0] * B[0][0]]]

    # Разделение матриц на блоки
    mid = n // 2
    A11, A12, A21, A22 = A[:mid][:mid], A[:mid][mid:], A[mid:][:mid], A[mid:][mid:]
    B11, B12, B21, B22 = B[:mid][:mid], B[:mid][mid:], B[mid:][:mid], B[mid:][mid:]

    # Вычисление промежуточных матриц P1...P7
    P1 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P2 = strassen(add_matrices(A21, A22), B11)
    P3 = strassen(A11, subtract_matrices(B12, B22))
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A12), B22)
    P6 = strassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    P7 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Вычисление блоков результирующей матрицы
    C11 = add_matrices(subtract_matrices(add_matrices(P1, P4), P5), P7)
    C12 = add_matrices(P3, P5)
    C21 = add_matrices(P2, P4)
    C22 = add_matrices(subtract_matrices(add_matrices(P1, P3), P2), P6)

    # Объединение блоков в одну матрицу
    return combine_blocks(C11, C12, C21, C22)


# Вспомогательные функции
def add_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def subtract_matrices(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def combine_blocks(C11, C12, C21, C22):
    n = len(C11) * 2
    C = [[0] * n for _ in range(n)]

    mid = len(C11)

