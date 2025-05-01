import time
import tracemalloc

def has_cycle(graph, n):
    visited = [0] * n  # 0 = не посещена, 1 = посещается, 2 = полностью обработана

    def dfs(v):
        visited[v] = 1
        for neighbor in graph[v]:
            if visited[neighbor] == 1:
                return True  # цикл обнаружен
            if visited[neighbor] == 0 and dfs(neighbor):
                return True
        visited[v] = 2
        return False

    for i in range(n):
        if visited[i] == 0:
            if dfs(i):
                return True
    return False

def main():
    # Старт замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Чтение входных данных
    with open("input3.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u - 1].append(v - 1)

    # Проверка наличия цикла
    cycle = has_cycle(graph, n)

    # Запись результата
    with open("output3.txt", "w") as f:
        f.write("1" if cycle else "0")

    # Завершение замеров
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Вывод в консоль
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

if __name__ == "__main__":
    main()
