import random
import time
import tracemalloc

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def main():
    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    with open('input1.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    randomized_quick_sort(array, 0, n - 1)

    with open('output1.txt', 'w') as file:
        file.write(' '.join(map(str, array)))

    # Подсчет времени и памяти
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.9f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")

if __name__ == "__main__":
    main()