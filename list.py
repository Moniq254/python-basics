# A collection of items stored in a single variable
#ordered,mutable(meaning it can be changed),allows duplicates
fruits=["Apple","Banana", "orange"]
print(fruits)
marks=[40,24,70,80.90,78.7]
print(marks)
data=["python",True,60,5.8]
print(data)

products=["Tv","Laptop","phone"]
print(products)

#Accessing list items-indexing
print(products[1])
print(products[-1])

#changing list items
products[0]="Tablet"
print(products)

#Adding items to a list- .append()
products.append("Camera")
print(products)
products.append("Printer")
print(products)

#Removing items from a list - .remove
products.remove("phone")
print(products)

products.pop()
print(products)

#checking the length of a list
print(len(products))

#checking if items exist in a list
print("Laptop" in products)