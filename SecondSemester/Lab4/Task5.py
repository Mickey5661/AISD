def compute_prefix_function(s):
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix

with open("input5.txt", "r") as file:
    s = file.readline().strip()

# Вычисление префикс-функции
prefix_values = compute_prefix_function(s)

with open("output5.txt", "w") as file:
    file.write(''.join(map(str, prefix_values)))
