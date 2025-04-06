def radix_sort(strings, k):
    # Создаем список для хранения строк вместе с их индексами
    indexed_strings = [(s, i) for i, s in enumerate(strings)]

    # Проведение k фаз цифровой сортировки
    for phase in range(k):
        # Создаем списки для каждой буквы алфавита
        buckets = [[] for _ in range(26)]

        # Распределяем строки по спискам в зависимости от текущего символа
        for s, idx in indexed_strings:
            char_code = ord(s[-phase - 1]) - ord('a')
            buckets[char_code].append((s, idx))

        # Объединяем списки обратно в один
        indexed_strings = []
        for bucket in buckets:
            indexed_strings.extend(bucket)

    # Возвращаем индексы строк в отсортированном порядке
    return [idx for _, idx in indexed_strings]


def read_input(filename):
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())

        # Читаем строки по вертикали
        strings = [''] * n
        for i in range(m):
            line = file.readline().strip()
            for j in range(n):
                strings[j] += line[j]

    return n, m, k, strings


def write_output(filename, indices):
    with open(filename, 'w') as file:
        file.write(' '.join(map(lambda x: str(x + 1), indices)))


def main():
    n, m, k, strings = read_input('input7.txt')
    sorted_indices = radix_sort(strings, k)
    write_output('output7.txt', sorted_indices)


if __name__ == '__main__':
    main()
