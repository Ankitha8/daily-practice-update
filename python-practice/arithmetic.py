num1 = 11
num2 = 5
addition = num1 + num2        #adding two numbers gives sum
subtraction = num1 - num2     #subtracting num2 from num1
multiplication = num1 * num2  #gives the product of num1 multiplied by num2
division = num1/num2          #divides num1 from num2
floor_division = num1 // num2 #Divides num1 by num2 and rounds the result down to the nearest whole number (integer)
modulus = num1 % num2         #Divides num1 by num2 and returns only the remainder
exponent = num1 ** num2       #Raises num1 to the power of num2
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(floor_division)
print(modulus)
print(exponent)

n1 = -10
n2 = -4
addition1 = n1 + n2
subtraction1 = n1 - n2
multiplication1 = n1 * n2
division1 = n1/n2
floor_division1 = n1 // n2
modulus1 = n1 % n2
exponent1 = n1 ** n2
print(addition1)
print(subtraction1)
print(multiplication1)
print(division1)
print(floor_division1)
print(modulus1)
print(exponent1)


a = "Good"
b = "Evening"
print(a + b)    #adds both the strings
#print("a" /0 )  #divides string a from 0
print(a + " " + b) #joins both string with space in between
print(a * 3)  #multiples string a 3 times

result1 = (10 + 5) * 2  #adds two numbers and multiples the sum with 2
print(result1)     

#print(10 / 0) # anything trying to divide by zero gives ZeroDivisionError

# LIST

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Joining two lists
print(list1 + list2)

# Repeating a list
print(list1 * 2)

fruits = ["apple", "banana", "mango"]
print("apple" in fruits)       # True
print("grapes" in fruits)     # False
print("apple" not in fruits)  # False
print("grapes" not in fruits) # True

# TUPLE

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Joining two tuples
print(tuple1 + tuple2)

# Repeating a tuple
print(tuple1 * 2)

colors = ("red", "blue", "green")
print("red" in colors)         # True
print("yellow" in colors)      # False
print("red" not in colors)     # False
print("yellow" not in colors)  # True


# SET

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Difference (elements present in set1 but not in set2)
print(set1 - set2)

# Difference (elements present in set2 but not in set1)
print(set2 - set1)

numbers = {10, 20, 30, 40}
print(20 in numbers)           # True
print(50 in numbers)           # False
print(20 not in numbers)      # False
print(50 not in numbers)      # True

#note: + and * is supported to lists and tuples not sets,- is supported to sets only not to lists n tuples,
