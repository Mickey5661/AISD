import time
import os


def can_partition_into_three_subsets(nums):
    total_sum = sum(nums)

    # Если сумма не делится на 3, то невозможно разделить на три подмножества с одинаковыми суммами
    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(nums)

    # dp[i
    # ][j] будет True, если можно получить сумму j, используя первые i элементов
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target, -1, -1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
            dp[i][j] = dp[i][j] or dp[i - 1][j]

    return 1 if dp[n][target] else 0


# Запуск таймера
start_time = time.perf_counter()

# Чтение входных данных из файла
with open('input13.txt', 'r') as file:
    lines = file.readlines()

    # Проверка на наличие хотя бы двух строк в файле
    if len(lines) < 2:
        raise ValueError("Файл input13.txt должен содержать как минимум две строки: количество чисел и сами числа.")

    # Чтение количества чисел
    n = int(lines[0].strip())

    # Проверка, что количество чисел больше нуля и не превышает 20
    # if n == 0:
    #     raise ValueError("Количество чисел должно быть больше нуля.")
    # if n > 20:
    #     raise ValueError("Количество чисел не должно превышать 20.")

    # Чтение чисел и преобразование их в список целых чисел
    nums = list(map(int, lines[1].strip().split()))

    # Проверка, что количество чисел соответствует указанному значению n
    # if len(nums) != n:
    #     raise ValueError("Количество чисел не соответствует указанному значению.")

    # Проверка, что все числа в диапазоне от 1 до 30
    # for num in nums:
    #     if num < 1 or num > 30:
    #         raise ValueError(f"Число {num} выходит за пределы допустимого диапазона (1-30).")

# Проверка возможности разделить на три подмножества с одинаковыми суммами
result = can_partition_into_three_subsets(nums)

# Запись результата в файл
with open('output13.txt', 'w') as file:
    file.write(str(result))

# Остановка таймера и вывод времени выполнения
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")