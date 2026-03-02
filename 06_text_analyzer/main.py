from string import punctuation

LINE_WIDTH = 45

def del_punctuation(value):
    for punct in punctuation:
        value = value.replace(punct, '')
    return value

def clean(text):
    clean_text = {del_punctuation(word).lower() for word in text.split() if len(word) > 1}
    return clean_text

print('=' * LINE_WIDTH)
print('АНАЛИЗАТОР ТЕКСТА')
print('=' * LINE_WIDTH)
print()

text1 = input('Введите первый текст:\n')
print()
text2 = input('Введите второй текст:\n')
set_text1 = clean(text1)
set_text2 = clean(text2)

print()
print(f'Всего символов в первом тексте: {len(text1)}')
print(f'Всего символов во втором тексте: {len(text2)}')

unique_word = set_text1 & set_text2

if unique_word:
    print('Общие слова:', *sorted(unique_word), sep=', ')
else:
    print('Общих слов не найдено.')