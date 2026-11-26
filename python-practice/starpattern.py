num = 4
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

for row in range(5):
    for column in range(5): #square star pattern
        print("*", end=" ")
    print()

for row in range(1, 6):
    for column in range(row): #Right-Angled Triangle
        print("*", end=" ")
    print()

for row in range(6, 0, -1):
    for column in range(row): #Inverted Right-Angled Triangle
        print("*", end=" ")
    print()

rows = 5
for row in range(1, rows + 1): # Right-Aligned Triangle
    for space in range(rows - row):
        print("  ", end="")
    for star in range(row):
        print("* ", end="")
    print()

rows = 5
for row in range(1, rows + 1): #Pyramid Pattern
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("* ", end="")
    print()

rows = 5
for row in range(rows, 0, -1): #Inverted Pyramid
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("* ", end="")
    print()

rows = 5                       #Diamond Pattern
for row in range(1, rows + 1):
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("* ", end="")
    print()
## Lower half
for row in range(rows - 1, 0, -1):
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("* ", end="")
    print()

num = 1234
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)


text = "ankitha"
reverse = ""
for i in text:
    reverse = i + reverse
print("Reversed:", reverse)
