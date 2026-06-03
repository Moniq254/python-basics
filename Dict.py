#A dictionary is used to store key value pairs
students={

"name":"Brian",
"age":21,
"course":"Python"

}
print(students)
#Accessing values in a dict -use keys
print(students["course"])

#adding items to a dict
students["school"]="letscode"
print(students)

#changing values in a dict
students["age"]=22
print(students)
students["course"]="Javascript"
print(students)
#you cant change the keys you can always change the values
#removing ites in a dict - using .pop
students.pop("course")
print(students)

#checking the length in a dict
print(len(students))