import time
import os


def can_partition_into_three_subsets(nums):
    total_sum = sum(nums)

    # Если сумма не делится на 3, то невозможно разделить на три подмножества с одинаковыми суммами
    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(nums)

    # dp[i][j] будет True, если можно получить сумму j, используя первые i элементов
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target, -1, -1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
            dp[i][j] = dp[i][j] or dp[i - 1][j]

    return 1 if dp[n][target] else 0

start_time = time.perf_counter()

with open('input13.txt', 'r') as file:
    lines = file.readlines()

    # Проверка на наличие хотя бы двух строк в файле
    if len(lines) < 2:
        raise ValueError("Файл input13.txt должен содержать как минимум две строки: количество чисел и сами числа.")

    # Чтение количества чисел
    n = int(lines[0].strip())

    # Чтение чисел и преобразование их в список целых чисел
    nums = list(map(int, lines[1].strip().split()))

# Проверка возможности разделить на три подмножества с одинаковыми суммами
result = can_partition_into_three_subsets(nums)

with open('output13.txt', 'w') as file:
    file.write(str(result))

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")