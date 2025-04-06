def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

with open("input4.txt", "r") as infile:
    a_line = infile.readline().split()
    n = int(a_line[0])
    a = list(map(int, a_line[1:n+1]))

    b_line = infile.readline().split()
    k = int(b_line[0])
    b = list(map(int, b_line[1:k+1]))

# Поиск каждого элемента из b в a
results = []
for number in b:
    index = binary_search(a, number)
    results.append(str(index))

with open("output4.txt", "w") as outfile:
    outfile.write(" ".join(results))
