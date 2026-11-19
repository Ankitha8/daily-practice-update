numbers = {10,10,40,50,80,20,40,70}
print(numbers) 
print(type(numbers))             #created a set

numbers.add(60)                  #adding a new element to set
print(numbers)

number1 = {10,30}                #updating
number1.update({60, 90})
print(number1)

number1.remove(10)               #removing a element from the set throws error element doesn't exist
print(number1)

number2 = {10, 20, 30}            #removing a element from the set but doesn't throw error even if it doesn't exist
number2.discard(40)
print(number2)

numbers3 = {10, 20, 30}
removed_value = numbers3.pop()    #popping a element from set removes a element randomly
print("Removed:", removed_value)
print("Remaining:", numbers3)

numbers3.clear()                   #clearing the whole set
print(numbers3)

   #set mathematical operations

a = {10,20,40,80}
b = {30,10,40,70}
c = a.union(b)         #Combines all unique elements from two sets
print(c)

d = a.intersection(b)  #Returns common elements from two sets
print(d)

e = a.difference(b)    #Returns elements present in the first set but not in the second set
print(e)

f = a.symmetric_difference(b) #Returns elements that are not common in both sets
print(f)

    #set relationship methods

line1 = {"red","black","orange"}  #Checks whether all elements of one set exist in another set
line2 = {"pink","blue","maroon"}
result = line1.issubset(line2)
print(result)

output = line1.issuperset(line2)   #Checks whether one set contains all elements of another set
print(output)

answer = line1.isdisjoint(line2)   #Checks whether two sets have no common elements
print(answer)