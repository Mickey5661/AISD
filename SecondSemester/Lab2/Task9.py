import sys
import time
import tracemalloc

sys.setrecursionlimit(1_000_000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1
        self.parent = None

def build_tree(nodes_info):
    nodes = [None]
    for key, _, _ in nodes_info:
        nodes.append(Node(key))

    for i, (key, l, r) in enumerate(nodes_info, start=1):
        node = nodes[i]
        if l != 0:
            node.left = nodes[l]
            nodes[l].parent = node
        if r != 0:
            node.right = nodes[r]
            nodes[r].parent = node

    def compute_sizes(node):
        if not node:
            return 0
        left = compute_sizes(node.left)
        right = compute_sizes(node.right)
        node.size = 1 + left + right
        return node.size

    compute_sizes(nodes[1])
    return nodes[1]

def find_node(root, key):
    node = root
    while node:
        if key < node.key:
            node = node.left
        elif key > node.key:
            node = node.right
        else:
            return node
    return None

def delete_subtree(node):
    if not node:
        return 0
    size = node.size
    parent = node.parent
    if parent:
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
    return size

def main():
    # Старт измерений
    tracemalloc.start()
    start_time = time.perf_counter()

    with open('input9.txt', 'r') as fin:
        n = int(fin.readline())
        nodes_info = [tuple(map(int, fin.readline().split())) for _ in range(n)]
        m = int(fin.readline())
        deletion_keys = list(map(int, fin.readline().split()))

    root = build_tree(nodes_info)
    total_nodes = root.size
    result = []

    for key in deletion_keys:
        target = find_node(root, key)
        if target:
            removed = delete_subtree(target)
            total_nodes -= removed
        result.append(str(total_nodes))

    with open('output9.txt', 'w') as fout:
        fout.write('\n'.join(result))

    # Завершение измерений
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Вывод статистики
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

if __name__ == "__main__":
    main()
