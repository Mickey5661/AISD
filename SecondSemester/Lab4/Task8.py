import time
import tracemalloc

def find_approx_matches(k, t, p):
    len_t = len(t)
    len_p = len(p)
    result = []

    for i in range(len_t - len_p + 1):
        mismatches = 0
        for j in range(len_p):
            if t[i + j] != p[j]:
                mismatches += 1
                if mismatches > k:
                    break
        if mismatches <= k:
            result.append(i)

    return result

def main():
    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Чтение входных данных
    with open("input8.txt", "r") as file:
        lines = file.readlines()

    # Обработка строк
    with open("output8.txt", "w") as output:
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split()
            k = int(parts[0])
            t = parts[1]
            p = parts[2]

            matches = find_approx_matches(k, t, p)
            output.write(f"{len(matches)} {' '.join(map(str, matches))}\n")

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
