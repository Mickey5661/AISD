import time
import tracemalloc

def has_negative_cycle(n, edges):
    # Запускаем алгоритм Беллмана-Форда из каждой вершины
    for start in range(n):
        dist = [float('inf')] * n
        dist[start] = 0

        for _ in range(n - 1):
            updated = False
            for u, v, weight in edges:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    updated = True
            if not updated:
                break

        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                return True  # Найден отрицательный цикл

    return False

def main():
    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Чтение входных данных
    with open("input9.txt", "r") as file:
        n, m = map(int, file.readline().split())
        edges = []
        for _ in range(m):
            u, v, w = file.readline().split()
            u = int(u) - 1
            v = int(v) - 1
            w = int(w)
            edges.append((u, v, w))

    # Проверка на наличие цикла отрицательного веса
    result = has_negative_cycle(n, edges)

    # Запись результата
    with open("output9.txt", "w") as file:
        file.write("1" if result else "0")

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
