# Changing the variable of 1 datatype into another is Type Casting.
# Let's say that if you want to add a = 25 and b = "25", would it be possible?
# No, cause a is integer and b is String.
# That's why type Casting exists.

a = 25 # Integer DataType
b = "25" # String DataType
#print(a + b) # gives error

c = "25" # String DataType
d = "25" # String DataType
print("The result of string- c + string- d is -->",c + d) # Concatinate string values

# So, how do we convert String datatype to integer datatype
# we do Type Casting
# Basic TypeCasting
c = int(c) + int(d) # Type Casted c and d to Integer.
print("The result of c + d is -->", c)

# Now there are 2 types of Type Casting in Python. One is Explicit and another is Implicit.
'''
Explicit Type Casting --> The conversion of one data type into another data type, done via
developer or programmer's intervention or manually as per the
requirement, is known as explicit type conversion.
'''
#eg -->
e = a + int (b)
print("The value of a + b is", e)

# Implicit Casting
'''
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have
higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of
the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the
Python interpreter itself (automatically). This is called, implicit typecasting in python.
'''
#eg -->
f = 2
g = 10.5
h = f + g 
print("The value of f + g is", h) # the int(f) is automatically casted to float for addition.
