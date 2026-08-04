set1={1,2,3,4,5}
print(type(set1))
print(set1)
print(len(set1))

#add new element
set1.add(6)
print(set1)
print(len(set1))

#add a set to another set
fruit_set={"apple","banana","cherry"}
set1.update(fruit_set)
print(set1)

#remove an element
set1.remove(3)
print(set1)

#discard an element
set1.discard(1) #does not raise an error if the element is not present
print(set1)
set1.discard("grape") #does not raise an error if the element is not present
print(set1)

set1.pop() #removes and returns an arbitrary element from the set
print(set1)

set1.clear() #removes all elements from the set
print(set1)

del set1 #deletes the set completely
print(set1) #this will raise an error since set1 is deleted