numbers = [10,30,10,80,99,45,50]

number1 = sorted(set(numbers)) #sorted the list  and removed duplicates using set
second_largest = number1[4] #found second largest number by giving index of that number after sorted
print(number1)
print(second_largest)
     

countries = (["IND" ,"USA"],["UK","PAK"])

print(countries)
     
print(countries[0])   #accessing first element in tuple
print(countries[-1])  #last element
countries[0].append("BAN") #adding extra element to first list inside tuple
print(countries)
print(countries[0])
print(countries.count("UK")) #count how many times UK is there
position = countries[0].index("USA") #check index of USA
print(position)
print(len(countries)) #checking length of tuple
print(min(countries)) #finding minimum
print(max(countries)) #finding maximum

numbers = (1,2,0,6,4)
print(sum(numbers))  #added all the numbers in tuple
print(sorted(numbers)) #sorted the numbers in tuple
print(min(numbers)) #finding minimum
print(max(numbers)) #finding maximum

numbers = [10,20,30,40]

converted = tuple(numbers) #converting a list to tuple
print(converted)

numbers = (10,20,30,40)

converted = list(numbers) #converting tuple to list
print(converted)

numbers = [10,20,80,60]

numbers[0],numbers[-1] = numbers[-1],numbers[0] #interchanging first and last element
print(numbers)

reversed = numbers[::-1] #reversing list using slicing
print(reversed)

numbers.reverse() #another method to reverse
print(numbers)

numbers2 = numbers.copy() # copying
print(numbers2)

counting = numbers.count(10) #counting how many 10's
print(counting)

print(sum(numbers)) #finding sum of numbers

total = sum(numbers)
average = total / len(numbers) #finding average of numbers in list
print(average)


numbers.pop(0) #removing first element from list using pop
print(numbers)

numbers.pop() #popping removes last element from list
print(numbers) 

numbers3 = [10,20,30,10,20]
unique = list(set(numbers3)) #removing duplicates 
print(unique)

numbers3.insert(0, 100) #inserting a new value 100 in the 0th index in the list
print(numbers3)

num1 = [10,20]
num2 = [30,40]
merged = num1 + num2 # merging or combing two lists
print(merged)