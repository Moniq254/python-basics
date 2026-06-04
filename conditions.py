#Conditional-statements allows a program to make decisions
#if statement-runs only when the condition is TRUE
age=18
if age>=18:
    print("you can vote")
#indentation -used in python to define or declare block of code
if(5>3):
    print("test")

#else statement-runs when condtion is FALSE(has no condition)
student_age=19
if student_age>=18:
    print("you are an adult")
else: 
    print("you are a minor")
amount=5000
if amount>=3000:
    print("you are eligible for 20% discount")
else: 
    print("you are not eligible for 20% discount")

#elif statement- used to check multiple conditions
marks=46
if marks>=80: 
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60: 
    print("Grade c")
elif marks>=50: 
    print("Grade D")
else: 
    print("fail")

#Multiple conditions(and, or)
#and operator-means both conditions must be true for it to be true
client_age=30
has_id=True
if client_age>=18 and has_id: 
    print("Access granted")
#or operator-means only one condition needs to bet True
day="Sunday"
if day=="Saturday"or day=="Sunday":
    print("weekend")