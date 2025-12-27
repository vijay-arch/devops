name = 'vijay'
age = 25

# using variable values inside a string or print statement
print(f"my name is {name} an i am {age} years old")
print('my name is ', name, 'i am ', age,'years old')

alphanum = ('()','{}','[]')

value = input("Enter the value :")
for i in alphanum:
    if i == value:
        print("valid check")

value = input("Enter the value :")
if value in alphanum:
    print("Valid check")

for i in range(10):
    print(i * "*")
    if i == 5:
        break
else:
    print("printed all * ")
