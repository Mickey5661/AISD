def has_negative_cycle(n, edges):
    # Запускаем алгоритм Беллмана-Форда из каждой вершины
    for start in range(n):
        dist = [float('inf')] * n
        dist[start] = 0

        # Основной цикл: n - 1 раз обновляем расстояния
        for _ in range(n - 1):
            updated = False
            for u, v, weight in edges:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    updated = True
            if not updated:
                break  # Никаких изменений — выходим раньше

        # Проверка: если после n - 1 итераций есть обновления — найден отрицательный цикл
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                return True  # есть цикл с отрицательным весом

    return False  # всё нормально, цикла нет


# Чтение входных данных
with open("input9.txt", "r") as file:
    n, m = map(int, file.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = file.readline().split()
        u = int(u) - 1  # делаем индексы с 0
        v = int(v) - 1
        w = int(w)
        edges.append((u, v, w))

# Проверяем наличие отрицательного цикла
result = has_negative_cycle(n, edges)

# Запись ответа
with open("output9.txt", "w") as file:
    file.write("1" if result else "0")
