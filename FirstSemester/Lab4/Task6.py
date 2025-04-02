from collections import deque

def process_queue(commands):
    queue = deque()
    min_queue = deque()
    results = []

    for command in commands:
        if command.startswith('+'):
            _, number = command.split()
            number = int(number)
            queue.append(number)

            while min_queue and min_queue[-1] > number:
                min_queue.pop()
            min_queue.append(number)

        elif command == '-':
            if queue:
                removed = queue.popleft()
                if removed == min_queue[0]:
                    min_queue.popleft()

        elif command == '?':
            if min_queue:
                results.append(min_queue[0])

    return results

with open('input6.txt', 'r') as file:
    lines = file.readlines()

# Первая строка содержит количество команд
M = int(lines[0].strip())

# Остальные строки содержат команды
commands = [line.strip() for line in lines[1:M + 1]]

output = process_queue(commands)

with open('output6.txt', 'w') as file:
    for result in output:
        file.write(f"{result}\n")