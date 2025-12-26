
# PRIMITIVE DATATYPES IN PYTHON ARE INT, FLOAT, BOOL, STRING

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

x = x + 10      # agumentad assignment operator
x += 10
x = 10.7
print(round(x))  # round the value
print(abs(-2.8))   # absolute

# use math module for more methods import math
# math.ceil(2.2)

# CONSOLE INPUT

x = input("x: ")        # input always come in string type
x= int(x)               # type cast into int
x += 5
print(x)

# TYPE CASTS

# int(x)
# float(x)
# str(x)
# bool(x)

