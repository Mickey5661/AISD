import time
import tracemalloc


def can_partition_into_three_subsets(nums):
    total_sum = sum(nums)

    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(nums)

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target, -1, -1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
            dp[i][j] = dp[i][j] or dp[i - 1][j]

    return 1 if dp[n][target] else 0


# Чтение входных данных
with open('input13.txt', 'r') as file:
    lines = file.readlines()

    if len(lines) < 2:
        raise ValueError("Файл input13.txt должен содержать как минимум две строки: количество чисел и сами числа.")

    n = int(lines[0].strip())
    nums = list(map(int, lines[1].strip().split()))

# Запуск замера времени и памяти
tracemalloc.start()
start_time = time.perf_counter()

# Основной вызов
result = can_partition_into_three_subsets(nums)

# Завершение замеров
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Запись результата
with open('output13.txt', 'w') as file:
    file.write(str(result))

# Вывод в консоль
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Использовано памяти: {current / 1024:.2f} KB")
print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
