num = float(input("Enter a number: ")) #identify whether a number is positive, negative, or zero
if num > 0:
   print("positive")
elif num < 0:
  print("negative")
else:
  print("Zero")

num1 = 32
num2 = 40
num3 = 45
if num1 > num2 & num1 > num3: #find the greatest among three numbers.
  print("num1 is greater")
elif num2 > num1 and num2 > num3:
   print("num2 is greater")
else:
  print("num3 is greater")


num1 = 32
num2 = 40
num3 = 45
greatest = max(num1, num2, num3) #find the greatest among three numbers.
print("The greatest number is:", greatest)

marks = 35            #assign grades based on marks
if marks >= 90:
  print("A")
elif marks >= 75:
  print("B")
elif marks >= 60:
  print("C")
elif marks >= 35:
  print("D")
else:
  print("Fail")

ch = input("Enter a character: ") # identify whether a character is a vowel or consonant.
if ch in "aeiouAEIOU":
  print("it's a vowel")
else:
    print("Consonant")

units = 1000
if units >= 2000: #calculate electricity charges using slab-based conditions.
  print("200rs")
elif units >= 1000:
  print("100rs")
else:
  print("500rs")

username = "ankitha"
password = "12345"

u = input("Enter username: ") 
p = input("Enter password: ")

if u == username and p == password:  #validate a username and password.
    print("Login successful")
else:
    print("Invalid username or password")

side1 = input("enter side1:") #check whether a triangle is valid using its three sides
side2 = input("enter side2:")
side3 = input("enter side3:")
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2: 
  print("valid")
else:
  print("invalid")

age = int(input("enter your age:")) # classify a person by age group.
if age <= 10:
  print("child")
elif age <= 18:
  print("teenager")
elif age <= 50:
  print("adult")
else:
  print("Senior citizen")

a = int(input("Enter first number: ")) #create a calculator using if-elif-else
b = int(input("Enter second number: "))
op = input("Enter operator: ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")

year = int(input("Enter year: "))
if year % 400 == 0:            #whether a year is a leap year
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")