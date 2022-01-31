# Write a program to sift list items in right.....
a= []
size= int(input("Enter Size Of The List: "))
for i in range(size):
    val=int(input("Enter The List Items: "))
    a.append(val)
print("Original List Is: ", a)

first_element=a[0]
for i in range(1,size):
    a[i-1]=a[i]
a[size-1]=first_element
print("Modified List is: ", a)    