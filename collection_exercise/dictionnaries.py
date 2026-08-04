my_dict={
    "name": "John",
    "age": 30,
    "age": 31  # This will overwrite the previous "age" key
}

print(type(my_dict))  # Output: <class 'dict'>
print(len(my_dict))   # Output: 2

#accessing values
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30

new_dict = {
    "name": "John",
    "age": 30,
    "colors":["red", "green", "blue"]
}
print(new_dict)  # Output: {'name': 'John', 'age': 30, 'colors': ['red', 'green', 'blue']}

new_dict["name"]="Jane"  # Update the value of the "name" key
print(new_dict)  # Output: {'name': 'Jane', 'age': 30

my_dict.update({"age": 32, "city": "New York"})  # Update existing key and add a new key
print(my_dict)  # Output: {'name': 'John', 'age': 32

my_dict.update({"city": "Los Angeles"})  # Update the value of the "city" key   
print(my_dict)  # Output: {'name': 'John', 'age': 32, 'city': 'Los Angeles'}

my_dict["city"] = "Chicago"  # Update the value of the "city" key using assignment
print(my_dict)  # Output: {'name': 'John', 'age': 32

my_dict["country"] = "USA"  # Add a new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 32

my_dict.pop("age")  # Remove the "age" key-value pair
print(my_dict)  # Output: {'name': 'John', 'city': 'Chicago', 'country': 'USA'}

del my_dict["city"]  # Remove the "city" key-value pair using del
print(my_dict)  # Output: {'name': 'John', 'country': 'USA

my_dict.clear()  # Remove all key-value pairs from the dictionary
print(my_dict)  # Output: {}