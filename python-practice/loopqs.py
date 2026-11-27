for i in range(1,21): #Create a list of numbers from 1 to 20.
  print(i)

for i in range(1,16): #Create a list of squares from 1 to 15.
  print(i * i)

for i in range(1,11): #Create a list of cubes from 1 to 10.
  print(i * i * i)

list = [2,8,4,3,1,9,10] #Extract all even and odd numbers from a list.
for i in list:
  if i % 2 == 0:
    print("even:",i)
  if i % 2!= 0:
    print("odd:",i)

list1 = ["apple","banana","guava"] #Convert all strings in a list to uppercase.
list2 = []
for i in list1:
  list2.append(i.upper())
print(list2)

words = ["apple", "banana", "cat", "orange", "dog"] #Extract words whose length is greater than 5.
result = []
for i in words:
  if len(i) > 5:
    result.append(i)
print(result)

colors = ["pink","blue","black"] #Create a list containing the length of each word.
result = []
for i in colors:
  result.append(len(i))  
print(result)

num = [1,2,3,-1,-2,-4,-8] #Replace every negative number with zero.
result = []
for i in num:
  if i < 0:
    result.append(0)
  else:
    result.append(i)
print(result)

n = [1,2,3,5,12,15,10] #Extract all numbers divisible by both 3 and 5.
n1 = []
for i in n:
  if i % 3 == 0 and i % 5 == 0:
    n1.append(i)
print(n1)

l1 = [] #Create a list of numbers divisible by 2 or 7 between 1 and 100.
for i in range(1,101):
  if i % 2 == 0 or i % 7 == 0:
    l1.append(i)
print(l1)

num = [[1, 2], [3, 4], [5, 6]] #Flatten a nested list.
result = []
for i in num:
  for j in i:
    result.append(j)
print(result)

word = "hello world" #Extract vowels from a string.
result = ""
for i in word:
  if i in "aeiou":
    result = result + i
print(result)

word = "Hi good evening" #Remove spaces from a string using list comprehension.
list = []
for i in word:
  if i != " ":
     list.append(i)
final = "".join(list)
print(final)

a = [1, 2]
b = [3, 4] #Create all possible pairs from two lists.
result = []
for i in a:
  for j in b:
    result.append((i, j))
print(result)

num = [1, 2, 3, 4, 5] #Create a list of tuples containing a number and its square.
result = []
for i in num:
  square = i * i
  result.append((i, square))
print(result)

celsius = [0, 10, 20, 30, 40] #Convert a list of temperatures from Celsius to Fahrenheit.
result = []
for i in celsius:
  f = (i * 1.8) + 32
  result.append(f)
print(result)

words = ["apple", "banana", "ant", "mango", "animal"]
result = [] #Extract words that start with the letter a.
for i in words:
  if i.startswith("a"):
    result.append(i)
print(result)

num = [1, 2, 3, 4, 5, 6] #Create a list of even numbers and odd numbers as labels.
result = []
for i in num: 
   if i % 2 == 0:
     result.append("Even")
else:
     result.append("Odd")
print(result)

num = [10, 20, 30, 40, 50] #numbers greater than the average of a given list
total = sum(num)
average = total / len(num)
result = []
for i in num: 
  if i > average: 
    result.append(i)
print("Average:", average)
print("Result:", result)