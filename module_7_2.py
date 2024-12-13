import string

import string

class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = self.get_all_words()

    def get_all_words(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            content = content.translate(str.maketrans('', '', string.punctuation))
            words = content.split()
        return words

    def find(self, word):
        """Находит слово и возвращает его порядковый номер (1-индексация) в тексте."""
        word = word.lower()
        try:
            index = self.words.index(word) + 1  # 1-индексация
            return {self.file_name: index}
        except ValueError:
            return {self.file_name: None}  # Если слово не найдено

    def count(self, word):
        """Считает количество вхождений слова в тексте."""
        word = word.lower()
        total_count = self.words.count(word)
        return {self.file_name: total_count}

# Функция для создания файла с примерным содержимым
def create_test_file():
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        content = """It's a text for task. Найти везде, используйте его для самопроверки. 
        Успехов в решении задачи. Text text text."""
        file.write(content)

# Создаем тестовый файл
create_test_file()

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # 3 слово по счёту
print(finder2.count('teXT'))     # 4 слова teXT в тексте всего
