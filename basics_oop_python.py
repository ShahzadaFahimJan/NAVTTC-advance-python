x = 5
print(x)
print(type(x))
print(x.bit_length())

y = [1,2,3]
print(y)
print(type(y))

y.append(4)
print(y)

print(isinstance(x, object))  # Output:
print(isinstance(y, object))  # Output:

x = 5
print(id(x))

####Functions and method####
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


##class
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(5, 3)
print(result)

###Procedural vs. the object-oriented approach
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)
obj = BankAccount(1000000)
obj.deposit(50000)
print(obj.balance)