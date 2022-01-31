from ast import While
import csv
def write():
    with open("data.csv","w") as fobj:
        obj=csv.writer(fobj)
        obj.writerow(["Roll","Name","Marks"])
        while True:
            roll=int(input("Enter Roll Number: "))
            name=input("Enter Name: ")
            marks=int(input("Enter Marks:"))
            data=[roll,name.upper(),marks]
            obj.writerow(data)
            choice=int(input("1->More Record\n2->End: Enter your choice:"))
            if choice==2:
                break
def read():
    with open("data.csv","r") as fobj:
        obj=csv.reader(fobj)
        for i in obj:
            print(i)
def search():
    with open("data.csv","r") as fobj:
        obj=csv.reader(fobj)
        next(obj)
        for i in obj:
            if int(i[2])<=90:
                print(i)            
write()
print("Data Written Successfully.....")
read()
print("Data Read Successfully.........")
search()
print("Search Successfully.....")