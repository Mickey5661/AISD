def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    with open('input3.txt.txt', 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        k = int(f.readline())
        targets = list(map(int, f.readline().split()))

    results = [binary_search(arr, target) for target in targets]

    with open('output4.txt', 'w') as f:
        f.write(' '.join(map(str, results)))


if __name__ == "__main__":
    main()
