#a loop is used to repeat code multiple times
#for loop used to repeat code over a sequeence
for number in range(5): 
    print(number)

#starting and ending range
for num in range(6,25): 
    print(num)

#loopingg through a list
products=["TV","Laptop","speaker","Charger"]
print(products)
for product in products:
    print(product)
marks=[40,78,56,90,27]
print(marks)
#loop through it
for mark in marks:
    print(mark)
#break stops the loop competely

for x in range(10): 
    if x==5:
        break
    print(x)

#continue skips the current iteration
for y in range(25):
    if y==13:
        continue
    print(y)

#while loop- repeats code as long as the condition is true
count=3
while count <=20:
    print(count)
    count+=1

z=0
while z<=100:
    print(z)
    z+=5