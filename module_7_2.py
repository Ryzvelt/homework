def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):
            byte_position = f.tell()  # Получаем текущую позицию байта
            f.write(string + '\n')  # Записываем строку с переносом
            strings_positions[(index, byte_position)] = string  # Сохраняем в словарь

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    # Извлекаем ключи и значения без скобок
    key, value = elem
    print(f"{key[0]}, {key[1]}: {value}")

