# write a program to delete element given list...
a = []
size= int(input("Enter The Size Of List: "))
for i in range(size):
    val= int(input("Enter the list of items:"))
    a.append(val)
print("Original list is: ",a)
key = int(input("Enter number to delete in given list: "))
flag=0
for i in range(size):
    if a[i]==key:
        pos=i
        flag=1
        break
if flag==0:
    print("Element Not Found:")
else:
    for i in range(pos,size-1):
        a[i]=a[i+1]
    a.pop()
    print("List After Deletion: ",a)            