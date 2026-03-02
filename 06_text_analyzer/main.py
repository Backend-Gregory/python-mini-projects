from string import punctuation

LINE_WIDTH = 45

def del_punctuation(value):
    for punct in punctuation:
        value = value.replace(punct, '')
    return value

def clean(text, as_set=True):
    clean_text = [del_punctuation(word).lower() for word in text.split() if len(word) > 1]
    return set(clean_text) if as_set else clean_text

def count_pred(text):
    text = text.replace('...', '.')
    count_pred = text.count('.') + text.count('!') + text.count('?')
    return count_pred

def print_res(count_pred, count_word, count_sim, unique_word_text):
    print('Информация для 1 текста:')
    print(f'Всего предложений: {count_pred}')
    print(f'Всего слов: {count_word}')
    print(f'Всего символов: {count_sim}')
    print(f'Всего уникальных слов: {len(unique_word_text)}')
    print('Уникальные слова:', *unique_word_text if unique_word_text else ['не найдено'])

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
count_word1 = len(clean(text1, False))
count_word2 = len(clean(text2, False))
count_sim1 = len(text1)
count_sim2 = len(text2)
unique_word = set_text1 & set_text2
unique_word_text1 = set_text1 - set_text2
unique_word_text2 = set_text2 - set_text1

print()
print('=' * LINE_WIDTH)
print('РЕЗУЛЬТАТЫ АНАЛИЗА')
print('=' * LINE_WIDTH)
print()
print('Общая информация:')

if unique_word:
    print('Общие слова:', *sorted(unique_word), sep=', ')
else:
    print('Общих слов не найдено.')

print_res(count_pred_text1, count_word1, count_sim1, unique_word_text1)
print_res(count_pred_text2, count_word2, count_sim2, unique_word_text2)