def count_beds(garden, n, m):
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        # Помечаем текущую ячейку как посещённую
        visited[x][y] = True
        # Двигаемся только по 4 сторонам
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Проверка границ и условий
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


# Чтение данных
with open("input13.txt", "r") as file:
    n, m = map(int, file.readline().split())
    garden = [list(file.readline().strip()) for _ in range(n)]

# Подсчёт грядок
result = count_beds(garden, n, m)

# Запись результата
with open("output13.txt", "w") as file:
    file.write(str(result))
