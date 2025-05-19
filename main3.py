class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Депозит на {amount} руб. Успешно!")
        else:
            print("Ошибка: сумма депозита должна быть положительной")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Снятие {amount} руб. Успешно!")
            else:
                print("Ошибка: недостаточно средств")
        else:
            print("ошибкаа: сумма снятия должна быть положительной")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print("Текущий баланс: ", account.get_balance())

account.deposit(500)
print("Текущий баланс: ", account.get_balance())

account.withdraw(150)
print("Текущий баланс: ", account.get_balance())

account.withdraw(2000)
account.withdraw(-100)
