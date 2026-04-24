# We can give different inputs to our python program.
# how do we do it. It's simple. Using input function.
# eg-->
a = input("Enter your name- ")
print("My name is", a)

# But here is the problem. Whatever we enter as the input, it is taken as string.
b = input("Enter a number: ")
print(a + b) # You see how the strings "Garv" and "25" were concatinated. This is because both are strings

# if we want to perform actual arithmatic operations on input variables then we would have to use Type Casting.
c = input("Enter the second number: ")
print(int(b) + int(c))

