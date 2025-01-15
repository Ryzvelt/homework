def add_everything_up(a, b):
    try:
        # Проверка случаев, когда один аргумент - строка, а другой - число
        if type(a) == str and (type(b) == int or type(b) == float):
            return a + str(b)  # Конкатенация строки и числа
        elif type(b) == str and (type(a) == int or type(a) == float):
            return str(a) + b  # Конкатенация числа и строки
        # Проверка случая, когда оба аргумента - числа
        elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
            return a + b  # Сложение двух чисел
        # Если типы не поддерживаются, выбросим TypeError
        else:
            raise TypeError("Unsupported types")
    except TypeError as e:
        return str(e)  # Возвращаем текст ошибки в виде строки

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))      # яблоко4215
print(add_everything_up(123.456, 7))           # 130.456
print(add_everything_up('текст', 'другой текст'))  # Unsupported types