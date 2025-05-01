import time
import tracemalloc

def max_unique_sum(n):
    result = []
    current = 1
    while n > 0:
        if n - current > current:
            result.append(current)
            n -= current
            current += 1
        else:
            result.append(n)
            break
    return result

# Чтение входных данных
with open("input5.txt", "r") as f:
    n = int(f.readline())

# Запускаем замер памяти
tracemalloc.start()

# Засекаем время до вызова функции
start_time = time.time()

# Вызываем функцию
result = max_unique_sum(n)

# Засекаем время после вызова
end_time = time.time()

# Получаем информацию о памяти
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Запись результата в файл
with open("output5.txt", "w") as f:
    f.write(f"{len(result)}\n")
    f.write(" ".join(map(str, result)))

# Выводим время и память в консоль
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Использовано памяти: {current / 1024:.2f} KB")
print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
