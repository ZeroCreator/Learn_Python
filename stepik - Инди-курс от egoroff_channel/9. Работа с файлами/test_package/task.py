# Задача урока 9.1.
# Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное
# слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, нужно вернуть
# слово, которое встречается последнее в тексте.
# При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.
# И также учитывайте, что слова в тестах будут как на русском языке, так и на английском
# Все возможные знаки пунктуации можно получить из модуля string:
# from string import punctuation
def longest_word_in_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    max_word = ''
    for line in file:
        words = line.split()
        for word in words:
            word_without_punc = remove_punctuation(word)
            if len(word_without_punc) >= len(max_word):
                max_word = word_without_punc
    file.close()
    return max_word


def remove_punctuation(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word = word.replace(punc, '')
    return word


print(longest_word_in_file('test.txt'))