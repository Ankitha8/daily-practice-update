numbers = [10,30,10,80,99,45,50]

number1 = sorted(set(numbers))
second_largest = number1[4]
print(number1)
print(second_largest)
     

countries = (["IND" ,"USA"],["UK","PAK"])

print(countries)
     
print(countries[0])   #accessing first element in tuple
print(countries[-1])  #last element
countries[0].append("BAN") #adding extra element to first list inside tuple
print(countries)
print(countries[0])
print(countries.count("UK"))
position = countries[0].index("USA")
print(position)
print(len(countries))
print(min(countries))
print(max(countries))

numbers = [1,2,0,6,4]
print(sum(numbers))
print(sorted(numbers))
print(min(numbers))
print(max(numbers))

numbers = [10,20,30,40]

converted = tuple(numbers)
print(converted)

numbers = (10,20,30,40)

converted = list(numbers)
print(converted)

numbers = [10,20,80,60]
print(max(numbers))
print(len(numbers))
print(min(numbers))
numbers[0],numbers[-1] = numbers[-1],numbers[0]
print(numbers)
reversed = numbers[::-1]
print(reversed)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
counting = numbers.count(10)
print(counting)
print(sum(numbers))
total = sum(numbers)
average = total / len(numbers)
print(average)
print(min(numbers))
for num in numbers:
    if num % 2 == 0:
        print(num)
numbers.pop(0)
print(numbers)

numbers3 = [10,20,30,10,20]
unique = list(set(numbers3))
print(unique)
numbers3.insert(0, 100)
print(numbers3)

num1 = [10,20]
num2 = [30,40]
merged = num1 + num2
print(merged)