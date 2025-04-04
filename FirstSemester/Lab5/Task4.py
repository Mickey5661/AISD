def sift_down(arr, i, swaps, n):
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[min_index]:
        min_index = left
    if right < n and arr[right] < arr[min_index]:
        min_index = right

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps, n)


def build_min_heap(arr, n):
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps, n)
    return swaps


# Читаем входные данные
with open("input4.txt", "r") as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

# Строим кучу
swaps = build_min_heap(arr, n)

# Записываем результат в output.txt
with open("output4.txt", "w") as file:
    file.write(f"{len(swaps)}\n")
    for i, j in swaps:
        file.write(f"{i} {j}\n")