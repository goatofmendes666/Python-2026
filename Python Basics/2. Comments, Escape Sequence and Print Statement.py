# We can print any string in python no matter how long it is, provided that It should not be in multiple lines.
# Examples
print("Garv is a Successful Man") # This is correct and won't give me errors.
# Se below how using multiple lines for 1 print statement shows error.
# The error is called "EOL" End of Line error, which means, that the line should have ended at "Man"
## But it has not, thus --> error.  
##
#print("Garv is a Successful Man
#and is also charming and hot")

# Escape Characters
# By using Escape characters I can achieve what we wanted.
print("Garv is a Successful Man \nand he is charming and hot.")
# Note --> We can comment or uncomment multiple comment lines by using a shortcut key --> ctrl + /
# We can also make multi-Line Comments using triple single/double inverted quotes. Eg-->
'''
Hello!
How Are you?
I am fine.
'''
# If you want to use Double Quotes in side strings then we use (\") for this.
print("Hello! My name is \"Garv Garwal\" and I am \"26\" years old.")

## We don't just use "Print Statement" for printing Strings
# We can also use it for many other things like -->
print("Hey! My name is Garv Agarwal, and I am", 26, "Years old." ) # This way we didn't used any escape characters.
print ("Garv", 26, "Male", "Height", 5.7, sep= "~") # "Sep" seperates each value with the "~" where commas are present.
print("Garv", 26, "Male", "Height", 5.7, sep= "~", end="Bye!\n")
print("Hi")
# using (end=" ") helps to end the print statement with any value specified.
