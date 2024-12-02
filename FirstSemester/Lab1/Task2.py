def insertion_sort(arr):
    n = len(arr)
    indexes = list(range(1, n + 1))

    for i in range(1, n):
        key = arr[i]
        key_index = indexes[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            indexes[j + 1] = indexes[j]
            j -= 1

        arr[j + 1] = key
        indexes[j + 1] = key_index

    return indexes

def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    new_indexes = insertion_sort(arr)

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, new_indexes)) + '\n')
        file.write(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()