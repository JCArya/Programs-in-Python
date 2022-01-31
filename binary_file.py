# Program in Write, Read and Search Element in Binary File..
import pickle
record= []
def write():
    f= open("data.dat","wb")
    while True:
        rno=int(input("Enter Roll Number:"))
        name=input("Enter Your Name:")
        marks=int(input("Enter Your Marks: "))
        data= [rno,name,marks]
        record.append(data)
        ch=input("Y->Yes\nN->No\nEnter Your Choice: ")
        if ch=='n' or ch=='N':
            break
    pickle.dump(record,f)
    f.close()
def read():
    f=open("data.dat","rb")
    r=pickle.load(f)
    for i in r:
        print(i)
    f.close()
write()
print("Data Written Successfully.....")
read()
print("Data Read Successfully.....")                
