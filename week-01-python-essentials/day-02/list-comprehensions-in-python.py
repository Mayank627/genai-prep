#List comprehensions = writing a for loop in a single line

#even_numbers = [x for x in range(10) if x % 2 == 0]
#print(even_numbers)

#squared_numbers = [x * x for x in range(1, 5)]
#print(squared_numbers)

#List comprehensions can also be used to create a new list based on an existing list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)

#Dictionary comprehensions 

squares = {x: x*x for x in range(1, 5)}
print(squares)

