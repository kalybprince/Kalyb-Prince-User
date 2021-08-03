class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, deposit):
        self.balance += deposit
    def make_withdrawal(self, withdrawal):
        self.balance -= withdrawal
    def display_user_balance(self):
        return self.balance

    def transfer_money(self, payee, amount):
        self.make_withdrawal(amount)
        payee.make_deposit(amount)

monty = User('monty')
guido = User('guido')
python = User('python')

monty.make_deposit(50)
monty.make_deposit(50)
monty.make_deposit(50)
monty.make_withdrawal(100)

print(monty.display_user_balance())     # 50

guido.make_deposit(50)
guido.make_deposit(50)
guido.make_withdrawal(100)
guido.make_withdrawal(100)

print(guido.display_user_balance())     # -100

python.make_deposit(50)
python.make_withdrawal(100)
python.make_withdrawal(100)
python.make_withdrawal(100)

print(python.display_user_balance())    # -250

monty.transfer_money(python, 50)

print(monty.display_user_balance())     # 50 - 50 = 0
print(python.display_user_balance())    # -250 + 50 = -200
