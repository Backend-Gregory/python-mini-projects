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