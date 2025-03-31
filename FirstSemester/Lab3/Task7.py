def radix_sort(strings, n, m, k):
    indices = list(range(n))
    for phase in range(k):
        indices.sort(key=lambda x: strings[m - phase - 1][x])
    return indices

# Чтение данных из input.txt
with open("input.txt", "r") as f:
    lines = f.readlines()
    n, m, k = map(int, lines[0].strip().split())
    strings = [list(line.strip()) for line in lines[1:m + 1]]

sorted_indices = radix_sort(strings, n, m, k)

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, [i + 1 for i in sorted_indices])))  # Индексы строк начинаются с 1
