fruits=["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)
    if fruit=="banana": 
        break

# for i in "banana":
#     print(i)

# for j in range(6):
#     print(j)    

# adj=["red", "big", "tasty"]
# for x in adj:
#     for y in fruits:
#         print(x, y)    

new_list=[x for x in range(10) if x<5]
print(new_list)  # Output: [0, 1, 2, 3, 4]  

