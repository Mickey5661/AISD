import time
import tracemalloc

def max_gold(W, weights):
    dp = [0] * (W + 1)
    for weight in weights:
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)
    return dp[W]

# Чтение входных данных
with open("input11.txt", "r") as f:
    W, n = map(int, f.readline().split())
    weights = list(map(int, f.readline().split()))

# Замер памяти
tracemalloc.start()

# Засекаем время
start_time = time.time()

# Вычисление результата
result = max_gold(W, weights)

# Засекаем время
end_time = time.time()

# Получаем информацию о памяти
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Запись результата
with open("output11.txt", "w") as f:
    f.write(str(result))

# Вывод в консоль
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Использовано памяти: {current / 1024:.2f} KB")
print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
