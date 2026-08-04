my_lambda=lambda x: x * 2  # A simple lambda function that doubles the input
print(my_lambda(5))  # Output: 10

x=lambda a,b: a+b  # A lambda function that adds two numbers
print(x(3,4))  # Output: 7

def my_function(n):
    return lambda a: a * n  # A function that returns a lambda function

my_function(2)  # Returns a lambda function that doubles the input
double=my_function(2)  # Assign the returned lambda function to a variable
print(double(5))  # Output: 10

words=["apple", "banana", "cherry", "date", "elderberry"]
sorted_words=sorted(words,key=lambda x: len(x))  # Sort the list of words by length using a lambda function
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']


