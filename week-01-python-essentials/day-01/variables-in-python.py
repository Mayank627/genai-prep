#Python determines type automatically based on the value assigned to the variable.
#In Java, we have to define the type of the variable (String name), 
# and we have to create a constructor to initialize the variable.

name = "Mayank"
age = 25
is_engineer = True

#You can also change the value of the variable, 
# and Python will automatically update the type if necessary. 
name = 30  # This will change the type of 'name' from string to integer

#You can still use the variable 'name' as a string, but it will now hold an integer value.
print(name)  # Output: 30   

#You can still use type hints
name: str = "Mayank"
age: int = 25           
is_engineer: bool = True
name: str = "Ujjwal"  # This will change the value of 'name' to "Ujjwal", but it is still a string.     