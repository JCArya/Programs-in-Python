def push(a,val):
    a.append(val)
    print("Insertion successfully....")

def pop(a):
    x=a.pop()
    print("Popped Item=",x)
    print("Pop successfully...")

def peek(a):
    index=len(a)-1
    print("Peek Element:= ",a[index])

def display(a):
    print("Stack Elements are: ")
    for i in range(len(a)-1,-1,-1):
        print(a[i])

a = []
while True:
    choice=int(input("1->Push Element:\n2->Pop Element:\n3->Peek Element:\n4->Diaplay Element:\n5->Exit:\nEnter your choice: "))
    if choice==1:
        val=int(input("Enter number to push: "))
        push(a,val)
    elif choice==2:
        if len(a)==0:
            print("Stack Underflow:")
        else:
            pop(a)
    elif choice==3:
        if len(a)==0:
            print("Stack Underflow:")
        else:
            peek(a)
    elif choice==4:
        if len(a)==0:
            print("Stack underflow:")
        else:
            display(a)
    else:
        break                                        

