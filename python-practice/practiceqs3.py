for i in range(1, 51): #print 1 to 50
    print(i)

for i in range(1,100): #even numbers from 1 to 100
    if (i % 2 == 0):
        print(i)

n = 5
fact = 1
for i in range(1,6): #factorial of n
    fact = fact * i
    print(fact)

numbers = [10, 20, 30, 40, 50] #sum of all numbers in a list
total = 0  # Start the sum from 0
for i in numbers:  # Visit each number in the list
    total = total + i  # Add current number to total
print("Sum:", total)  # Print the final sum

n = 2
for i in range(1, 11):       #multiplication table of a num 2
    print(n, "x", i, "=", n * i)

numbers = [10, 5, 20, 3, 15] #smallest num in a list without using min()
smallest = numbers[0]  # Assume the first number is the smallest
for i in numbers:  # Check each number in the list
    if i < smallest:  # Check if current number is smaller
        smallest = i  # Update the smallest number
print("Smallest number:", smallest)  # Print the final smallest number

n= int(input("Enter a number: ")) # sum of a number taken from user
total = 0  # Start sum from 0
for i in range(1, n + 1): # Run loop from 1 to n
    total = total + i  # Add each number to total
    print("Sum:", total) # Print the final sum

numbers = [10, -5, 0, 20, -8, 0, 7]
positive = 0  # Initially positive count is 0
negative = 0  # Initially negative count is 0
zero = 0      # Initially zero count is 0
for i in numbers:  # Check each number in the list
    if i > 0:     # Check if number is greater than 0
        positive = positive + 1  # Increase positive count

    elif i < 0:   # Check if number is less than 0
        negative = negative + 1  # Increase negative count

    else:         # If neither positive nor negative, it is zero
        zero = zero + 1  # Increase zero count
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)