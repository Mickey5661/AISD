import time
import tracemalloc

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)

    if p_len > t_len:
        return []

    base = 256
    mod = 10**9 + 7

    pattern_hash = 0
    current_hash = 0
    power = 1

    for i in range(p_len):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        current_hash = (current_hash * base + ord(text[i])) % mod
        if i != p_len - 1:
            power = (power * base) % mod

    positions = []

    for i in range(t_len - p_len + 1):
        if pattern_hash == current_hash:
            if text[i:i + p_len] == pattern:
                positions.append(i + 1)  # индексация с 1

        if i < t_len - p_len:
            current_hash = (current_hash - ord(text[i]) * power) % mod
            current_hash = (current_hash * base + ord(text[i + p_len])) % mod
            current_hash = (current_hash + mod) % mod  # избегаем отрицательных значений

    return positions

def main():
    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    with open("input3.txt", "r") as file:
        pattern = file.readline().strip()
        text = file.readline().strip()

    matches = rabin_karp(pattern, text)

    with open("output3.txt", "w") as file:
        file.write(f"{len(matches)}\n")
        if matches:
            file.write(" ".join(map(str, matches)))

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
