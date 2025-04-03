def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    # Сортировка массива
    selection_sort(array)

    # Запись отсортированного массива в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, array)))

if __name__ == "__main__":
    main()