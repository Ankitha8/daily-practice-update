#Access elements using negative indexing
names = ["Anu", "Ravi", "Kiran", "Manoj"]

print(names[-1])
print(names[-2])

#Extract the first three elements
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])

#Extract the last three elements
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[-3:])

#Print every second element
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])

#Add an element using append()
languages = ["Python", "Java"]

languages.append("JavaScript")

print(languages)

#Add multiple elements using extend()
numbers = [1,2,3,4]

numbers.extend([5,6])
print(numbers)

#Sort a list in ascending order
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

#Sort a list in descending order
numbers = [10, 50, 20, 40, 30]

numbers.sort(reverse=True)

print(numbers)