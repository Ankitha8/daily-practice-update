#Insert an element at a specific position
flowers = ['Daisy','Lily','Rose']

flowers.insert(2,'Sunflower')
print(flowers)

#Remove an element using remove()
groceries = ['Salt','Sugar','Spice']

groceries.remove('Sugar')
print(groceries)

#Remove an element using pop()
numbers = [10, 20, 30, 40]

removed = numbers.pop()

print(removed)
print(numbers)

#Delete an element using del
numbers = [10, 20, 30, 40]

del numbers[2]
print(numbers)

#count duplicate elements
numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))

#Find the index of an element
languages = ["Python", "Java", "C", "JavaScript"]

print(languages.index("C"))