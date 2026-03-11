import random
import string
DIGITS = string.digits
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
PUNCTUATION = string.punctuation

def generate_password(length, chars):
    res = ''
    for i in range(length):
        res += random.choice(chars)
    return res

while True:
    chars = ''
    
    print()
    try:
        count = int(input("Количество паролей для генерации: ") )
        len_password = int(input("Длина одного пароля: " ))
        print("На каждый вопрос отвечай либо 1(да) либо 2(нет)")
        nums = int(input(f"Включать ли цифры {DIGITS}?: " ))
        lower_case = int(input(f"Включать ли заглавные буквы {UPPERCASE_LETTERS}?: " ))
        upper_case = int(input(f"Включать прописные буквы {LOWERCASE_LETTERS}?: " ))
        simvols = int(input("Включать ли символы пунктуации?: "))
        p = str(nums) + str(lower_case) + str(upper_case) + str(simvols)
        
        flag = True
        for i in p:
            if i not in "12":
                flag = False
                break
        if not flag:
            print("На каждый вопрос надо отвечать либо 1(да) либо 2(нет)")
            continue

    except ValueError:
        print("Ошибка! Вводите только цифры")
        continue

    if nums == 1:
        chars += DIGITS
    if lower_case == 1:
        chars += UPPERCASE_LETTERS
    if upper_case == 1:
        chars += LOWERCASE_LETTERS
    if simvols == 1:
        chars += PUNCTUATION

    if len(chars) == 0:
        print("Ошибка! не выбрано ни одного типа символов")
        continue

    print()
    print("Вот ваши пароли")
    for i in range(count):
        print(generate_password(len_password, chars))

    exit_true = False
    while True:
        exit = input("Сгенерировать ещё? (да/нет): ").lower()
        if exit != "нет" and exit != "да":
            print("Ошибка! введите да или нет")
            continue
        if exit == 'нет':
            exit_true = True
            break
        else:
            break
    
    if exit_true:
        break
