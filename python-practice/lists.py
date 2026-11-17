#Create and print a list
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

#Find the length of a list
numbers = [10, 20, 30, 40, 50]

print(len(numbers))

#Access first and last elements
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])

#Reverse a list
numbers = [10, 20, 30, 40]

print(numbers[::-1])

#Modify an element in a list
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

#Print every element using a for loop
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#Convert a string into a list
name = "Python"

result = list(name)

print(result)

#Check whether two variables refer to the same list
a = [10, 20, 30]
b = a

print(id(a) == id(b))