def max_gold(W, weights):
    dp = [0] * (W + 1)
    for weight in weights:
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)
    return dp[W]

# Чтение из input.txt
with open("input11.txt", "r") as f:
    W, n = map(int, f.readline().split())
    weights = list(map(int, f.readline().split()))

# Вычисляем результат
result = max_gold(W, weights)

# Запись в output.txt
with open("output11.txt", "w") as f:
    f.write(str(result))
