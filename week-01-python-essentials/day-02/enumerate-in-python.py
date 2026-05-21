
#Enumerate ----- Used for Lists

skills = ['Python', 'Django', 'Flask', 'Pandas']
for index, skill in enumerate(skills):
    print(index, skill)


#Zip ----- Used for Lists
#For unequal lengths, zip stops at the shortest list.


names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)


#Items ----- Used for Dictionaries

skills = {"Python": "Intermediate", 
          "C++": "Advanced",
          "Java": "Expert"}
for a, b in skills.items():
    print(a, b)


#Keys

for a in skills.keys():
    print(a)

#Values

for b in skills.values():
    print(b)


