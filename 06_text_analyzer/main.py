LINE_WIDTH = 45
print('=' * LINE_WIDTH)
print('АНАЛИЗАТОР ТЕКСТА')
print('=' * LINE_WIDTH)
print()

text1 = input('Введите первый текст:\n')
print()
text2 = input('Введите второй текст:\n')
set_text1 = set(text1.split())
set_text2 = set(text2.split())

print()
print(f'Всего символов в первом тексте: {len(text1)}')
print(f'Всего символов во втором тексте: {len(text2)}')

unique_word = set_text1 & set_text2

if unique_word:
    print('Общие слова:', *sorted(unique_word), sep=', ')
else:
    print('Общих слов не найдено.')