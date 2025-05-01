import time
import tracemalloc

def collect_signatures(segments):
    # Сортируем по правому краю
    segments.sort(key=lambda x: x[1])
    points = []
    last_point = -1

    for seg in segments:
        if last_point < seg[0]:
            last_point = seg[1]
            points.append(last_point)

    return points

# Чтение входных данных
with open("input4.txt", "r") as f:
    n = int(f.readline())
    segments = [tuple(map(int, f.readline().split())) for _ in range(n)]

# Запускаем замер памяти
tracemalloc.start()

# Засекаем время до вызова функции
start_time = time.time()

# Вызываем функцию
points = collect_signatures(segments)

# Засекаем время после вызова
end_time = time.time()

# Получаем информацию о памяти
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Запись результата в файл
with open("output4.txt", "w") as f:
    f.write(f"{len(points)}\n")
    f.write(" ".join(map(str, points)))

# Выводим время и память в консоль
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Использовано памяти: {current / 1024:.2f} KB")
print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
