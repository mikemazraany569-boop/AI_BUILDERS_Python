def my_function():
    print("Hello from my_function!")

my_function()  # Output: Hello from my_function!   

temp1=77
# celsius1=(temp1-32)*5/9
# print(f"{temp1}°F is equal to {celsius1:.2f}°C")  # Output: 77°F is equal to 25.00°C
temp2=25
# celsius2=(temp2-32)*5/9
# print(f"{temp2}°F is equal to {celsius2:.2f}°C")  # Output: 25°F is equal to -3.89°C    

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

celsius1=fahrenheit_to_celsius(77)
celsius2=fahrenheit_to_celsius(25)
print(f"{temp1}°F is equal to {celsius1:.2f}°C")  # Output: 77°F is equal to 25.00°C
print(f"{temp2}°F is equal to {celsius2:.2f}°C")  # Output: 25°F is equal to -3.89°C

def my_name(name,country="USA"):
    print("Hello," + name + " from " + country)

my_name("Alice")
my_name("Bob")
my_name("Charlie")
my_name("David", "Canada")  # Output: Hello, David from Canada





