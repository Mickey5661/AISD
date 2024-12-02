def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            swap(arr, j + 1, j)
            j -= 1
        arr[j + 1] = key
def main():

    with open("input.txt", "r") as f:
        n = f.readline().strip()
        arr = f.readline().strip().split()

    insertion_sort_desc(arr)

    with open('output.txt', 'w') as f:
        f.write(str(arr))

if __name__ == '__main__':
    main()