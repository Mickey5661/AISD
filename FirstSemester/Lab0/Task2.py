import time
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())

if n >= 45 or n < 0:
    print("Wrong input value")
else:
    def fibonacci_calc(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


    result = fibonacci_calc(n)

    with open("output.txt", "a") as file:
        file.write(str(result) + '\n')

    start_time = time.time()
    fibonacci_calc(n)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time} секунд")