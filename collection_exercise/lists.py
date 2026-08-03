mylist=[1,2,3,4,4]
print(type(mylist))
print(mylist[0])#accessing the first element of the list

print(len(mylist))#length of the list

mylist.append(5)#adding an element to the list
print(mylist)

mylist.remove(4)#removing an element from the list
print(mylist)

#remove at specific index
mylist.pop(2)#removing the element at index 2   
print(mylist)

mylist.pop()#removing the last element of the list
print(mylist)

#del mylist[0]#deleting the first element of the list
#print(mylist)

#mylist.clear()#removing all the elements of the list
#print(mylist)

fruit_list=["apple","banana","cherry"]

print(fruit_list[1])#accessing the second element of the list 

fruit_list.append("orange")#adding an element to the list

print(fruit_list)

mylist.extend(fruit_list)#adding all the elements of fruit_list to mylist
print(mylist)

#list comprehension
new_list=[]
for x in fruit_list:
    if "a" in x:    
        new_list.append(x)

print(new_list)

new_list=[x for x in fruit_list if "a" in x]#list comprehension
print(new_list)

#ranging list
ranged_list=[x for x in range(11)]#creating a list of numbers from 0 to 10
print(ranged_list)

ranged_list[0:5]
print(ranged_list[0:5])#slicing the list from index 0 to 4

ranged_list[5:]#slicing the list from index 5 to the end
print(ranged_list[5:])