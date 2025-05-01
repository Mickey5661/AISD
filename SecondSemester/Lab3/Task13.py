import time
import tracemalloc

def count_beds(garden, n, m):
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        visited[x][y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if garden[nx][ny] == '#' and not visited[nx][ny]:
                    dfs(nx, ny)

    beds = 0
    for i in range(n):
        for j in range(m):
            if garden[i][j] == '#' and not visited[i][j]:
                dfs(i, j)
                beds += 1

    return beds

def main():
    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Чтение данных
    with open("input13.txt", "r") as file:
        n, m = map(int, file.readline().split())
        garden = [list(file.readline().strip()) for _ in range(n)]

    # Подсчёт грядок
    result = count_beds(garden, n, m)

    # Запись результата
    with open("output13.txt", "w") as file:
        file.write(str(result))

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
