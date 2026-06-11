#OOP-(is object oriented programming)
#its a way of writing code using classes and objects
#when we say classes we mean-Blueprints
#objects - real instances
#a method is a function inside a class

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
Jeep=Car("jeep","wrangler",2023)
print(Jeep.brand)
print(Jeep.model)
print(Jeep.year)

toyota=Car("Toyota","Filder",2020)
print(toyota.brand)
print(toyota.model)
print(toyota.year)

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount}successfuly deposited ne balance is{self.balance}")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance-=amount
            print(f"{amount} successfully withdrawn new balance is{self.balance}")
        else:
            print("insufficient balance")

account1=Account("Jane doe",5000)
account1.deposit(5000)
account1.withdraw(2000)

account2=Account("John doe",20000)
account2.deposit(10000)
account2.withdraw(5000)

