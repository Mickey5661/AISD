import time
import tracemalloc

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def next_greater(self, key):
        return self._next_greater(self.root, key)

    def _next_greater(self, node, key):
        result = 0
        while node:
            if node.key > key:
                result = node.key
                node = node.left
            else:
                node = node.right
        return result

def main():
    input_file = 'input3.txt'
    output_file = 'output3.txt'

    bst = BST()
    results = []

    # Запуск замеров
    tracemalloc.start()
    start_time = time.perf_counter()

    # Обработка входных данных
    with open(input_file, 'r') as fin:
        for line in fin:
            if line.startswith('+'):
                x = int(line[2:])
                bst.insert(x)
            elif line.startswith('>'):
                x = int(line[2:])
                results.append(str(bst.next_greater(x)))

    # Завершение замеров
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Запись результата
    with open(output_file, 'w') as fout:
        fout.write('\n'.join(results))

    # Вывод в консоль
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

if __name__ == '__main__':
    main()
