import numpy as np


def strassen_multiply(A, B):
    """
    Реализация умножения матриц методом Штрассена.
    """
    # Получаем размеры матриц
    n, m = A.shape if isinstance(A, np.ndarray) else (1, len(A))
    p, q = B.shape if isinstance(B, np.ndarray) else (len(B), 1)

    # Проверяем базовый случай для корректного завершения рекурсии
    if n <= 1 or m <= 1 or p <= 1 or q <= 1:
        # Используем np.dot() вместо оператора * для матричного умножения
        return np.dot(A, B)

    # Для поддержки алгоритма Штрассена матрицы должны быть квадратными и размера 2^n
    # Находим ближайшую степень двойки
    max_dim = max(n, m, p, q)
    next_pow2 = 2 ** int(np.ceil(np.log2(max_dim)))

    # Создаем и заполняем расширенные матрицы
    A_padded = np.zeros((next_pow2, next_pow2))
    A_padded[:n, :m] = A

    B_padded = np.zeros((next_pow2, next_pow2))
    B_padded[:p, :q] = B

    # Рекурсивное вычисление произведения
    C_padded = _strassen_recursive(A_padded, B_padded)

    # Извлекаем нужную часть результата
    C = C_padded[:n, :q]
    return C


def _strassen_recursive(A, B):
    """Рекурсивная часть алгоритма Штрассена."""
    n = A.shape[0]

    # Базовый случай
    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])

    # Разделение матриц на блоки
    mid = n // 2

    # Используем обозначения из задания: X = [A B; C D], Y = [E F; G H]
    a = A[:mid, :mid]
    b = A[:mid, mid:]
    c = A[mid:, :mid]
    d = A[mid:, mid:]

    e = B[:mid, :mid]
    f = B[:mid, mid:]
    g = B[mid:, :mid]
    h = B[mid:, mid:]

    # Вычисляем 7 вспомогательных матриц P₁-P₇
    p1 = _strassen_recursive(a, f - h)
    p2 = _strassen_recursive(a + b, h)
    p3 = _strassen_recursive(c + d, e)
    p4 = _strassen_recursive(d, g - e)
    p5 = _strassen_recursive(a + d, e + h)
    p6 = _strassen_recursive(b - d, g + h)
    p7 = _strassen_recursive(a - c, e + f)

    # Вычисляем блоки результирующей матрицы
    # XY = [P₅ + P₄ - P₂ + P₆    P₁ + P₂
    #       P₃ + P₄               P₁ + P₅ - P₃ - P₇]
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Собираем результат
    C = np.zeros((n, n))
    C[:mid, :mid] = c11
    C[:mid, mid:] = c12
    C[mid:, :mid] = c21
    C[mid:, mid:] = c22

    return C


# Чтение матриц из файла
def read_matrices(filename):
    """Чтение матриц из входного файла."""
    try:
        with open(filename, 'r') as f:
            n = int(f.readline().strip())

            # Чтение матрицы A
            A = np.zeros((n, n))
            for i in range(n):
                line = f.readline().strip()
                if line:
                    A[i] = list(map(float, line.split()))

            # Чтение матрицы B
            B = np.zeros((n, n))
            for i in range(n):
                line = f.readline().strip()
                if line:
                    B[i] = list(map(float, line.split()))

        return A, B
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None

def write_matrix(C, filename):
    """Запись результата в выходной файл."""
    with open(filename, 'w') as f:
        for row in C:
            f.write(' '.join(map(str, row)) + '\n')


def main():
    try:
        A, B = read_matrices('input9.txt')
        if A is None or B is None:
            return

        C = strassen_multiply(A, B)
        write_matrix(C, 'output9.txt')
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
