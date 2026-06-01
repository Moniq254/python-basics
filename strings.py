#string ndexing-accessing a single character in a string
name="Lucy" 
print(name[0])
print(name[3])

#string length
password="students123"
print(len(password))

#.upper().converts text to uppercase
language="Python"
print(language.upper())

#. lower()-converts text to lowercase
email="janedoe@gmail.com"
print(email.lower())

#. title()-capitalies the first letter of every word
full_name="jane doe"
print(full_name.title())

#,strip()- we use it to remove unnecessary whitespace
student_name="     Brian    "
print(student_name.strip())

#.replace()
text="I love JavaScript"
print(text.replace("JavaScript","Python"))

#.find()-find character position
city="Nairobi"
print(city.find("r"))

# String Contatenation-joining or combining Strings
#using the + operator
greetings="Hello"
client="Dennis"
print(greetings+""+client)

#f - strings -modern way of formating strings
patient_name="Susan Moraa"
patient_age=27
print(f"Hello, my name is {patient_name} and I am {patient_age} years old")

amount=1000
balance=2000
print(f"Confirmed KES {amount} sent. New balance is {balance}")