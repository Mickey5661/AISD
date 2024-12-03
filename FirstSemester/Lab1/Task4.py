def linear_search(arr, value):
    indices = []
    count = 0
    for index in range(len(arr)):
        if arr[index] == value:
            indices.append(index)
            count += 1
    if count > 0:
        return count, indices
    else:
        return -1

with open('input.txt', 'r') as f:

    numbers = list(map(int, f.readline().strip().split()))
    value_to_find = int(f.readline().strip())

result = linear_search(numbers, value_to_find)

with open('output.txt', 'a') as f:
    if result == -1:
        f.write('-1\n')
    else:
        count, indices = result
        f.write(str(result))
        