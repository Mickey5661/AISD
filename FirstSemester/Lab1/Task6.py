def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def read_input(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    return arr


def write_output(filename, arr):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, arr)))

input_file = "input.txt"
output_file = "output.txt"
array = read_input(input_file)

# Выполнение сортировки
bubble_sort(array)

# Запись результата в выходной файл
write_output(output_file, array)

