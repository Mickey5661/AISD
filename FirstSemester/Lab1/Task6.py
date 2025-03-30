def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Чтение входного файла
with open('input.txt') as f:
    arr = [int(line.strip()) for line in f]

# Сортировка
sorted_arr = bubble_sort(arr)

# Запись в выходной файл
with open('output.txt', 'w') as f:
    for num in sorted_arr:
        f.write(f"{num}\n")
