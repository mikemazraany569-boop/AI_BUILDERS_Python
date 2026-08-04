# a=20
# b=10

# if a<b:
#     print("a is less than b")
# elif a>b:
#     print("a is greater than b")       
# else:
#     print("a is equal to b")

# x=1
# if x>10:
#     print("x is greater than 10")
#     if x>20:
#         print("and is greater than 20")
#     else:
#         print("but is not greater than 20")        
# else:
#     print("x is not greater than 10")

age = 18
has_license = True

if age >= 18:
    if has_license:
        print("You are eligible to drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are not eligible to drive.")        

if age >= 18 and has_license:
    print("You are eligible to drive.")

