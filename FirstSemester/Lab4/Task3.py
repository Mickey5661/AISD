def is_correct_sequence(s):
    stack = []
    bracket_map = {')': '(', ']': '['}

    for char in s:
        if char in ('(', '['):
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack


with open('input3.txt', 'r') as fin, open('output3.txt', 'w') as fout:
    n = int(fin.readline())
    for _ in range(n):
        seq = fin.readline().strip()
        if is_correct_sequence(seq):
            fout.write("YES\n")
        else:
            fout.write("NO\n")
