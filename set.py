#a set is a collection of unique items
products={"Tv","Laptop","phone",}
print(products)

#adding items to a set
#.add()-used to add one item
products.add("Headphones")
print(products)
#.update()-used to add multiple items
products.update(["speaker","Tablet","Charger"])
print(products)

#removing items-use.remove
products.remove("Tablet")
print(products)

#length
print(len(products))