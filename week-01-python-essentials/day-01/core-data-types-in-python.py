#List
skills = ["python", "java", "C++"]
skills.append("javascript")
skills.remove("javascript")

#Tuple is immutable
person = ("10", "20")

#Python collections are type-agnostic, meaning they can hold elements of different types.
mixed_list = [1, "hello", 3.14, True]
print(mixed_list[2])

#Set is unordered and does not allow duplicates 
unique_skills = {"python", "java", "C++", "python"}
print(unique_skills)

#Dictionary is a collection of key-value pairs
person_info = {
    "name": "Mayank",
    "experience": 2.5,
    "is_engineer": True
}
print(person_info["experience"])