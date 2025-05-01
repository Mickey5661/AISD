import time
import tracemalloc

def compute_prefix_function(s):
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix

def main():
    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Чтение строки
    with open("input5.txt", "r") as file:
        s = file.readline().strip()

    # Вычисление префикс-функции
    prefix_values = compute_prefix_function(s)

    # Запись результата
    with open("output5.txt", "w") as file:
        file.write(''.join(map(str, prefix_values)))

    # Завершение замеров
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Вывод статистики
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

if __name__ == "__main__":
    main()
