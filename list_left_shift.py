a = []
size= int(input("Enter The Size Of List: "))
for i in range(size):
    val= int(input("Enter the list of items:"))
    a.append(val)
print("Original list is: ",a)
last_element= a[size-1]
for i in range(size-2,-1,-1):
    a[i+1]=a[i]
a[0]=last_element
print("Modified List is: ",a)    
