#Functions and f-strings in Python

def greet(name):
    return f"Hello, {name}"

name = greet("Mayank")
print(name)

# f-strings are a way to format strings in Python. 
# They allow you to embed variables directly inside strings.
# You can embed variables, expressions, function calls, and even complex expressions inside f-strings.

age = 25
greeting = f"My name is {name} and I am {age} years old."
print(greeting)