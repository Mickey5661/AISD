def insertion_sort(arr):
    # Реализация сортировки вставкой
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещение элементов, которые больше ключа, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    # Сортировка массива
    insertion_sort(arr)

    # Запись отсортированного массива в файл output.txt
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, arr)))

if __name__ == '__main__':
    main()