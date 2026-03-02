from string import punctuation

LINE_WIDTH = 45

def del_punctuation(value):
    for punct in punctuation:
        value = value.replace(punct, '')
    return value

def clean(text):
    clean_text = {del_punctuation(word).lower() for word in text.split() if len(word) > 1}
    return clean_text

def count_pred(text):
    text = text.replace('...', '.')
    count_pred = text.count('.') + text.count('!') + text.count('?')
    return count_pred

print('=' * LINE_WIDTH)
print('АНАЛИЗАТОР ТЕКСТА')
print('=' * LINE_WIDTH)
print()

text1 = input('Введите первый текст:\n')
print()
text2 = input('Введите второй текст:\n')
set_text1 = clean(text1)
set_text2 = clean(text2)
count_pred_text1 = count_pred(text1)
count_pred_text2 = count_pred(text2)

print()
print('=' * LINE_WIDTH)
print('РЕЗУЛЬТАТЫ АНАЛИЗА')
print('=' * LINE_WIDTH)
print()
print('Общая информация:')

unique_word = set_text1 & set_text2

if unique_word:
    print('Общие слова:', *sorted(unique_word), sep=', ')
else:
    print('Общих слов не найдено.')

print()
print('Информация для 1 текста:')
print(f'Всего предложений в первом тексте: {count_pred_text1}')
print(f'Всего символов в первом тексте: {len(text1)}')
print()
print('Информация для 2 текста:')
print(f'Всего предложений во втором тексте: {count_pred_text2}')
print(f'Всего символов во втором тексте: {len(text2)}')