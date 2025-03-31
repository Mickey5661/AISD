def generate_worst_case(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        return [1] + list(range(n, 1, -1))


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())

# Генерация наихудшей перестановки
worst_case = generate_worst_case(n)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, worst_case)))