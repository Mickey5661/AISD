import time

with open("input.txt", "r") as file:
    n = int(file.readline())

if n < 0 or n > 10**7:
    print("Wrong input value")
else:
    def mod_fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, (a+b) % 10
        return b

    res = mod_fib(n)

    with open("output.txt", "a") as f:
        f.write(str(res))

start_time = time.time()
mod_fib(n)
end_time = time.time()

print(f"Время выполнения: {end_time - start_time} секунд")

