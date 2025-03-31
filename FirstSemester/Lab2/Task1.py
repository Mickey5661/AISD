def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Добавление оставшихся элементов
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))

# Сортировка
sorted_arr = merge_sort(arr)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_arr)))
