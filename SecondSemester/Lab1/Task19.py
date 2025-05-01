import time
import tracemalloc

def matrix_chain_order(p):
    n = len(p) - 1  # Количество матриц
    dp = [[0]*n for _ in range(n)]
    s = [[0]*n for _ in range(n)]

    for l in range(2, n+1):  # длина цепочки
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k

    return dp, s

def build_optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i+1}"
    else:
        return "(" + build_optimal_parenthesization(s, i, s[i][j]) + \
               build_optimal_parenthesization(s, s[i][j]+1, j) + ")"

# Чтение данных
with open("input19.txt", "r") as f:
    n = int(f.readline())
    dims = []
    for _ in range(n):
        a, b = map(int, f.readline().split())
        dims.append(a)
    dims.append(b)  # добавляем последний столбец последней матрицы

# Замер памяти и времени
tracemalloc.start()
start_time = time.perf_counter()

dp, s = matrix_chain_order(dims)
result = build_optimal_parenthesization(s, 0, n-1)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Запись результата
with open("output19.txt", "w") as f:
    f.write(result)

# Вывод в консоль
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Использовано памяти: {current / 1024:.2f} KB")
print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
