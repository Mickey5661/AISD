import sys
sys.setrecursionlimit(1_000_000)

class Node:
    def __init__(self, key, idx):
        self.key = key
        self.left = None
        self.right = None
        self.idx = idx
        self.balance = 0

def build_tree(data):
    nodes = [None] + [Node(k, i) for i, (k, _, _) in enumerate(data, start=1)]
    for i, (k, l, r) in enumerate(data, start=1):
        nodes[i].left = nodes[l] if l != 0 else None
        nodes[i].right = nodes[r] if r != 0 else None
    return nodes[1]

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def compute_balance(node):
    if not node:
        return 0
    node.balance = height(node.right) - height(node.left)
    compute_balance(node.left)
    compute_balance(node.right)

def small_left_rotate(a):
    b = a.right
    a.right = b.left
    b.left = a
    return b

def big_left_rotate(a):
    b = a.right
    c = b.left

    b.left = c.right
    a.right = c.left
    c.left = a
    c.right = b
    return c

def left_rotate(root):
    compute_balance(root)
    if root.right.balance >= 0:
        return small_left_rotate(root)
    else:
        return big_left_rotate(root)

def serialize(root):
    result = []
    idx_map = {}
    counter = [1]

    def dfs(node):
        if not node:
            return 0
        idx = counter[0]
        counter[0] += 1
        idx_map[node] = idx
        l = dfs(node.left)
        r = dfs(node.right)
        result.append((node.key, l, r))
        return idx

    dfs(root)
    return result[::-1]

def main():
    with open("input13.txt", "r") as fin:
        n = int(fin.readline())
        data = [tuple(map(int, fin.readline().split())) for _ in range(n)]

    root = build_tree(data)
    root = left_rotate(root)
    output = serialize(root)

    with open("output13.txt", "w") as fout:
        fout.write(f"{len(output)}\n")
        for k, l, r in output:
            fout.write(f"{k} {l} {r}\n")

if __name__ == "__main__":
    main()
