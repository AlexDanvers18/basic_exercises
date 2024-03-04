# Вывести последнюю букву в слове
word = 'Архангельск'
print()
print(f'Последняя буква в слове {word} =  {word[-1]}')

# Вывести количество букв "а" в слове
word = 'Архангельск'
count_letter_a = word.lower().count('а')
print(f'Количество букв "а" в слове {word} = {count_letter_a}')



# Вывести количество гласных букв в слове
word = 'Архангельск'
count_vowels = 0
list_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
for letter in word.lower():
    if letter in list_vowels:
        count_vowels += 1
print(f'Количество гласных: {count_vowels}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
list_words = sentence.split()
count_words = len(list_words)
print(f'Количество слов в предложении: {count_words}')



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_words = sentence.split()
print(f'Список первых букв каждого слова на отдельной строке:')
for word in list_words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
list_words = sentence.split()
count_words = len(list_words)
avg_len = int(len(sentence) / count_words)
print(f'Усреднённая длина слова в предложении: {avg_len}')