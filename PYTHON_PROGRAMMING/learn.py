
# PRIMITIVE DATATYPES IN PYTHON ARE INT, FLOAT, BOOL, STRING Stores a single value

name = 'vijay'      # string
age = 25   # integer
ratings = 4.9       # float values
is_published = True  # boolean only 0, None, False, empty values are false in bool function remains are true
course_name = 'python'  # strings quoted with '' or ""
messages = """hi,       
this is vijay
from the world of hello"""     # multiline string
state = f"hi i am {name} and i am {age},younger";  # formatted string we can use any expression inside {} like {2+2}

print(len(messages))        # length of a string
print(len("45"))            # length of a number
print(type(name),type(ratings),type(is_published),type(course_name), type(age))     # data type of veriable


#Escape sequences
#\'
#\"
#\n
#\\

# STRING METHODS

course = "  python programming"

print(course.upper())   # uppercase the string
print(course.title())   # titles the string
print(course.lower())   # lowercase the string
print(course.strip())   # remove the whitespace from string
print(course.lstrip())  # remove left side whitespace
print(course.rstrip())  # remove right side whitespace
print(course.find("pro")) # return index of the character in string
print(course.replace("pro","Pro"))  # replace the old string with new one
print( "pro" in course)     # return true if string present in course value
print( "python" not in course)  # return false because string present in string
print( course.split(" "), "\n\n\n\n")
print(course.count("python"))
print(course[1])            # string is array of characters with indexes
print(course[2:])           # start index : end index  default is start and end value
print(ord("b"))             # gives ASCII value of a string

# ARITHMETIC OPERATOR

print(10 + 3)   # addition
print(10 - 3)   # substraction
print(10 * 3)   # multiplication
print(10 / 3)   # division
print(10 // 3)  # division with result integer value
print(10 % 3)   # modules
print(10 ** 3)  # exponent left to the power of right

# RELATION OPERATOR

x = 10 > 3
x = 10 >= 3
x = 10 < 3
x = 10 <= 3     # less than equals
x = 10 == 10   # equals with respect to type
x = 5 !=  "10"  # not quals with respect to type true bcz int != str
x = "bag" == "BAG"  # false bcz its char values are not same  b = 95 B = 66  in ASCII

x = x + 10      # aug
# mentad assignment operator
x += 10
x = 10.7
print(round(x))  # round the value
print(abs(-2.8))   # absolute

# use math module for more methods import math
# math.ceil(2.2)

# CONSOLE INPUT

# x = input("x: ")        # input always come in string type
x= int(x)               # type cast into int
x += 5
print(x)

# TYPE CASTS
# Always know the data type you are working with.
# int(x)
# float(x)
# str(x)
# bool(x)

# CONDITIONS

# Conditions don't always have to be strict Booleans. In Python, "falsy" values include 0, None, empty strings "",
# and empty collections (like [] or {}). Almost all other values are "truthy".

temperature = 45
if temperature > 30:
    print("too hot")
elif temperature < 30:
    print("too cold")
else:
    print("ok")

print("done")

# Shorthand of if else block
score = 54
result = "pass" if score > 35 else "fail"
print(result)

# Logical operators and, or, not

high_income = True
good_credits = True

if high_income and good_credits :
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credits :
    print("Eligible")
else:
    print("Not eligible")

if not (high_income and good_credits) :
    print("Eligible")
else:
    print("Not eligible")

# MATCH CASE

x = int(input("Enter a number:"))

match x:            # check the matching cases and execute it
    case 1:             # multiple cases
        print('x is 1')
    case 2:
        print('case is 2')
    case _ if x != 90:          # multiple default cases
        print(x, 'is not 90')
    case _:
        print('final default case')


# LOOPS

# The for loop is used when you know in advance how many times you want to iterate
# or when you need to traverse a sequence like a list, string, or range.

# A for loop iterates over a sequence (list, string, range, etc.)

#for variable in sequence:
#    code to repeat
# Python automatically picks one item at a time
# for loop will iterate each item one by one at a time
for vijay in range(3):
    print("Attempt: ",vijay + 1)

for letter in "vijay":
    print(letter)

# A while loop runs as long as a condition is true
# while condition:
#     code to repeat
# Loop will execute code until the condition becomes false and it will keep running for the time of condition true

count = 1

while count:
    print(count)
    count = 0

# break – Stop the loop
for i in range(10):
    if i  == 5:
        break
    print(i)

# continue – Skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass – Do nothing (placeholder)
for i in range(3):
    pass


for i in range(5):
    for j in range(5):
        print(i,j)

# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# for else we can use else statement with for loop if the loop exits normally without break statement then else block will executes
for i in range(10):
    print(i * "*")
    if i == 5:
        break
else:
    print("printed all * ")


# DATA TYPES

'''
x = "Hello World"	                str	
x = 20	                            int	
x = 20.5	                        float	
x = 1j	                            complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	                    range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                        bool	
x = b"Hello"	                    bytes	
x = bytearray(5)	                bytearray	
x = memoryview(bytes(5))	        memoryview	
x = None	                        NoneType
'''

# DATA STRUCTURES ( DATA + LOGIC )

# List is a ordered collection of data and it is mutable ( can change and resize ) , can store ,mixed data types
# Can store mixed data types, and its can be indexed and iterable

list = ["vijay", 25, True, 3.8]
m = list        # m stores the reference of the list veriable if m changes list also changes bcx both var names refer same memory object
list[0] = 32
print(list[0])
print(list[0])      # list can be indexed
print(list[-1])
print(list[1:3:2])  # list slicing [start:end:jump_sequence]
list.append(30)     # add at end of list
list.insert(2, 40)      # add at index
list.remove(3.8)        # remove value
list.pop()          # remove last value

print(list)

for item in list:           # list can iterable
    print(item)


# TUPLE ( READ-ONLY LIST )
# a tuple is a built-in data type used to store an ordered collection of elements
# Ordered: Elements maintain a defined order that will not change during the tuple's lifetime.
# Immutable: Once created, you cannot change, add, or remove individual elements.
# Heterogeneous: A single tuple can store elements of different data types (e.g., integers, strings, and even lists).
# my_tuple = (1, 2, "Python"), empty = (), single = (5,), tup = 1, 2, 3 - without () it will treat as tuple
# Indexing & Slicing tuple[0], tuple[0:1]
# Unpacking = name, age = ("Alice", 25)
# Concatenation & Repetition = (1, 2) + (3, 4) results in (1, 2, 3, 4)
# Membership Test = in and not in
# tuples have only two built-in methods: count(value) to get the number of occurrences of a value,
# and index(value) to find the index of the first occurrence

tuple = 1,5,4

print(tuple)

