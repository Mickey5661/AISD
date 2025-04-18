def max_unique_sum(n):
    result = []
    current = 1
    while n > 0:
        if n - current > current:
            result.append(current)
            n -= current
            current += 1
        else:
            result.append(n)
            break
    return result

with open("input5.txt", "r") as f:
    n = int(f.readline())

result = max_unique_sum(n)

with open("output5.txt", "w") as f:
    f.write(f"{len(result)}\n")
    f.write(" ".join(map(str, result)))
