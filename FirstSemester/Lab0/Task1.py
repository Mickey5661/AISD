with open('input.txt', 'r') as file:
    a, b = map(int, file.readline().split())

sum = a + b

with open('output.txt', 'w') as file:
    file.write(str(sum) + '\n')

result_expression = a + b**2

with open('output.txt', 'a') as file:
    file.write(str(result_expression) + '\n')