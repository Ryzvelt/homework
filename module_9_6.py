def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):  # Перебираем длины подпоследовательностей
        for start in range(n - length + 1):  # Перебираем начальные позиции
            yield text[start:start + length]  # Возвращаем подпоследовательность

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)