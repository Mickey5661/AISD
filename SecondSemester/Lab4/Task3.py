def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)

    if p_len > t_len:
        return []

    base = 256  # основание (кол-во возможных символов)
    mod = 10**9 + 7  # большое простое число для хэширования

    # Вычисляем хэш шаблона и первую "окну" текста
    pattern_hash = 0
    current_hash = 0
    power = 1  # base^(p_len-1)

    for i in range(p_len):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        current_hash = (current_hash * base + ord(text[i])) % mod
        if i != p_len - 1:
            power = (power * base) % mod

    positions = []

    for i in range(t_len - p_len + 1):
        if pattern_hash == current_hash:
            if text[i:i + p_len] == pattern:
                positions.append(i + 1)  # +1, т.к. индексация с единицы

        if i < t_len - p_len:
            # Удаляем первый символ из окна и добавляем следующий
            current_hash = (current_hash - ord(text[i]) * power) % mod
            current_hash = (current_hash * base + ord(text[i + p_len])) % mod
            current_hash = (current_hash + mod) % mod  # избегаем отрицательного значения

    return positions

with open("input3.txt", "r") as file:
    pattern = file.readline().strip()
    text = file.readline().strip()

# Поиск всех вхождений
matches = rabin_karp(pattern, text)

with open("output3.txt", "w") as file:
    file.write(f"{len(matches)}\n")
    if matches:
        file.write(" ".join(map(str, matches)))
