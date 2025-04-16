def collect_signatures(segments):
    # Сортируем по правому краю
    segments.sort(key=lambda x: x[1])
    points = []
    last_point = -1

    for seg in segments:
        if last_point < seg[0]:  # если текущий отрезок не покрыт
            last_point = seg[1]  # добавляем точку в конец отрезка
            points.append(last_point)

    return points

# Чтение из input.txt
with open("input4.txt", "r") as f:
    n = int(f.readline())
    segments = [tuple(map(int, f.readline().split())) for _ in range(n)]

points = collect_signatures(segments)

# Запись в output.txt
with open("output4.txt", "w") as f:
    f.write(f"{len(points)}\n")
    f.write(" ".join(map(str, points)))
