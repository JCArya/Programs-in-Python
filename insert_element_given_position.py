# Write a program for insert elements at a given position in a list......
a = []
size= int(input("Enter The Size Of List: "))
for i in range(size):
    val= int(input("Enter the list of items:"))
    a.append(val)
print("Original list is: ",a)
a.append(None)
pos= int(input("Enter Position: "))
key= int(input("Enter to Insert Elements: "))
for i in range(size-1,pos-2,-1):
    a[i+1]=a[i]
a[pos-1]=key 
print("List After Insertion is: ",a)   