class ThreadedMap:
    def __init__(self):
        # Инициализация словаря для хранения ключ-значение и списка для порядка вставки
        self.map = {}
        self.order = []

    def put(self, x, y):
        # Добавление или обновление значения
        if x not in self.map:
            self.order.append(x)
        self.map[x] = y

    def delete(self, x):
        # Удаление ключа, если он существует
        if x in self.map:
            del self.map[x]
            self.order.remove(x)

    def get(self, x):
        # Получение значения по ключу или 'none', если ключа нет
        return self.map.get(x, 'none')

    def prev(self, x):
        # Получение предыдущего значения в порядке вставки
        if x not in self.map:
            return 'none'
        index = self.order.index(x)
        if index == 0:
            return 'none'
        return self.map[self.order[index - 1]]

    def next(self, x):
        # Получение следующего значения в порядке вставки
        if x not in self.map:
            return 'none'
        index = self.order.index(x)
        if index == len(self.order) - 1:
            return 'none'
        return self.map[self.order[index + 1]]


def process_operations(input_file, output_file):
    # Обработка операций из входного файла и запись результатов в выходной файл
    threaded_map = ThreadedMap()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        n = int(infile.readline().strip())

        for _ in range(n):
            operation = infile.readline().strip().split()
            op_type = operation[0]
            x = operation[1]

            if op_type == 'put':
                y = operation[2]
                threaded_map.put(x, y)
            elif op_type == 'delete':
                threaded_map.delete(x)
            elif op_type == 'get':
                result = threaded_map.get(x)
                outfile.write(f"{result}\n")
            elif op_type == 'prev':
                result = threaded_map.prev(x)
                outfile.write(f"{result}\n")
            elif op_type == 'next':
                result = threaded_map.next(x)
                outfile.write(f"{result}\n")


def main():
    # Основная функция для запуска обработки операций
    process_operations('input4.txt', 'output4.txt')


if __name__ == "__main__":
    main()