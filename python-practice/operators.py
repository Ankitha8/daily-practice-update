#Logical operators 
# and # Both conditions must be true
age = 23
has_id = True
if age >=23 and has_id:
    print("eligible")
else: 
    print("not eligible")

# or Either condition can be true
age = 21
has_id = True
if age >=23 or has_id:
    print("eligible")
else: 
    print("not eligible")

# not not reverses the Boolean value
is_blocked = True
if not is_blocked:
    print("Account is active")
else:
    print("Account is blocked")

#Assignment operators
# = Assign a value
a = 10
print(a)
# += Add and update
a = 10
a += 5
print(a)
# -= Subtract and update
a = 10
a -= 3
print(a)
# *= Multiply and update
a = 5
a *= 2
print(a)
# /= Divide and update
a = 10
a /= 2
print(a)
#Membership operators
#in – Check whether an item exists
#not in – Check whether an item doesn't exist
fruits = ["apple", "mango", "banana"]
print("mango" in fruits)
print("orange" not in fruits)
#Identity operators
#is – Check whether two variables refer to the same object
a = [10, 20]
b = a
print(a is b)
#is not – Check whether they are different objects
a = [10, 20]
b = [10, 20]
print(a is not b)
#is None – Check whether a variable has no value
name = None
print(name is None)
#Bitwise operators
#& Bitwise AND, | Bitwise OR, ^ Bitwise XOR,~ Bitwise NOT,<< Left shift,>> Right shift
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)