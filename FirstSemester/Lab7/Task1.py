import time

def min_coins(money, coins):
    # Инициализация массива для хранения минимального количества монет
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    # Заполнение массива dp
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1

def process_input(input_file, output_file):
    with open(input_file, 'r') as infile:
        money, k = map(int, infile.readline().strip().split())
        coins = list(map(int, infile.readline().strip().split()))

    result = min_coins(money, coins)

    with open(output_file, 'w') as outfile:
        outfile.write(f"{result}\n")

def main():
    start_time = time.perf_counter()

    process_input('input1.txt', 'output1.txt')

    end_time = time.perf_counter()
    print(f"Время выполнения: {end_time - start_time:.9f} секунд")

if __name__ == "__main__":
    main()