class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def owner(self):
        return self.__owner

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self.__balance += amount
        print('Деньги успешно внесены')
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('Недостаточно средств')
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        self.__balance -= amount
        print('Деньги успешно сняты')
        
while True:
    name = input('Введите имя: ')
    if name:
        break
    else:
        print('Имя не может быть пустым')

acc = BankAccount(name)
print(f'Владелец: {acc.owner}')

print(f'Баланс: {acc.balance}')
print('\n1. Пополнить счет')
print('2. Снять деньги со счета')
print('3. Выход')
num = int(input('Выберите действие от 1 до 3: '))