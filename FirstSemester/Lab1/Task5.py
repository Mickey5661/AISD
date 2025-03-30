def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Чтение входного файла
with open('input.txt') as f:
    arr = [int(line.strip()) for line in f]

# Сортировка
sorted_arr = selection_sort(arr)

# Запись в выходной файл
with open('output.txt', 'w') as f:
    for num in sorted_arr:
        f.write(f"{num}\n")
