# Lambda functions are useful for quick one-liner functions that are not going to be reused elsewhere in the code. 
# They are also known as anonymous functions because they do not have a name.
# Syntax: lambda parameters: expression

#Regular function

def square(x):
    return x * x

#Lambda function

square = lambda x: x * x
#print(square(5))

#Lambda functions can also take multiple parameters
add = lambda x, y: x + y
#print(add(3, 4))

#Lambda functions can also be used in higher-order functions like map, filter, and reduce
numbers = [1, 2, 3, 4, 5]
#squared_numbers = list(map(lambda x: x * x, numbers))
squared = list(map(lambda x: x * x, numbers))
print(squared)
#print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)

#Lambda functions are used in sorting and other operations that require a key function
points = [(1, 2), (3, 4), (5, 6)]
#points.sort(key=lambda point: point[1], reverse=True)
points.sort(key = lambda x: x[1], reverse=True)
print(points)