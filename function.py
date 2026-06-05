#A function is a block of code that runs when called
#importance of function-helps repeat a code
#DRY- means dont repeat yourself

#when defining a function you start by defining it and in python we use-def
def greet():
    print("Hello world")
greet()
#functions with parameters
#parameter-its a value you passed into a function(a variable inside a function)
#an argument-the exact value
def greetings(name):
    print("Hello", name)

greetings("Brian")
greetings("Alce")
greetings("Benjamin")
greetings("Lucy")
greetings("Monica")

#functions with multiple parameters
def add(a,b,c,):
    print(a+b+c)
add(10,20,30)
add(8,7,5)

#functions with return values
def price(amount,quantity):
    return amount*quantity
total_amount=price(1000,5)
print(total_amount)

#functions- conditional statements
def check_numbers(number):
    if number % 2==0:
        print("even number")
    else:
        print("odd number")

check_numbers(10)
check_numbers(11)

def login(username,password):
    if username == "admin" and password == "1234":
        print("login successful")
    else:
        print("invalid credentials")
login("admin","1234")
login("admin","1345")

