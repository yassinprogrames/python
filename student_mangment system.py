import json
try:
    file = open("data_struc.json", "r")
    data = json.load(file)
    file.close()
except:
    data = {}
def save():
    file = open("data_struc.json","w")
    json.dump(data,file)
    file.close()
def add():
    while True:
        new_name = input("what is the student name")
        while True:
            try:
                new_degree=float(input("what is his degree")) 
                break
            except:
                    print("enter an number")    
        if new_name not in data:
            data[new_name] = new_degree
            print("the student added ")
            again = input("will you add again(y/n)")
            if again == "n":
                save()
                break
        else:
            print("the student is already in the data base so if you will want to add a diffrent name pls choose to try again")            
#remove student
def remove():
    while True:
        removed_data = input("what is the name of the student you want to remove ")
        if removed_data in data:
            data.pop(removed_data)
            print("student removed")
            save()
        else:
            print("student is not exist")
        again = input("will you remove again(y/n) ")
        if again == "n":
            break
#update students name part
def up_name():
            updated_name = input("what is the name of the student you want to update")
            new_name = input("what is the new name ")
            if updated_name in data:
                data[new_name] = data.pop(updated_name)
                print("student name updated")
            else:
                print("student is not exist") 
#update students degree part
def up_degree():
            name =input("what is the student name you want to update")
            while True:
                try:
                    updated_degree=float(input("what is his degree")) 
                    break
                except:
                    print("enter an number")    
            if name in data:
                data[name] = updated_degree
                print("student degree updated ")
            else:
                print("student is not exist") 
# the all update function                
def update():
    while True :
        choice =input("do you want to update name or degree(N,D)")
        if choice == "N":
            up_name()
            save()
        elif choice == "D":
            up_degree()
            save()
        again = input("will you add again(y/n)")
        if again == "n":
            break       
#show students
def show():
    is_all =input("do you show the all students data?(y/n)")
    if is_all == "y":
        for key,value in data.items():
            print(key,value)
    elif is_all == "n":
        cont=int(input("do you show specific number"))
        if cont > len(data):
            print("the number of the students in the data base is just",len(data))
            for keys,values in data.items():
                print(keys,values)
        else:
            for i , (keys,values) in enumerate(data.items()):
                print(keys,values)
                if i+1 ==cont:
                    break       
#searsh for the students dgree by name
def searsh_degree_bynm():
    while True:
        searshed_item = input("what is name of the studen you want to know his degree ")
        if searshed_item in data:
            print("the degree is",data[searshed_item])
        else:
            print("student is not exist") 
        again = input("will you add again(y/n)")
        if again == "n":
            break 
# searsh for all names that have this degree
def searsh_name_bydeg():
    while True:
        searshed_degree = float(input("what is the degree of the student you want"))
        if searshed_degree in data.values():
            names = [key for key,value in data.items() if value == searshed_degree]
            for i ,name in enumerate(names):
                print(i+1,name)
        else:
            print("the degree is not exsit")  
        again = input("will you add again(y/n)")
        if again == "n":
            break
# the all searsh function           
def searsh():
    while True:
        choice = int(input("do you want to know the name by its degree or know a student degree by his name(1,2) "))
        if choice ==1:
            searsh_name_bydeg()
        elif choice == 2:
            searsh_degree_bynm()
        else:
            print("this is not a choice")   
        again = input("will you add again(y/n)")
        if again == "n":
            break         
# the avrage function
def avreg():
    total =0
    cont = len(data)
    for  value in data.values():
        total += value
    if cont == 0:
        print("the count is 0")
    else:
        print(total/cont)     
# making the app by the functions
print("__________________welocme to my app_____________________________")
while True:
    print("the current students data is\n",data)
    op = input("what will you want to do from the list:\n"+
    "1-ADD STUDENT\n"+
    "2-REMONE STUDENT\n"+
    "3-update a student information (update name or degree)\n"+
    "4-SHOW THE ALL DATA OR SPECIFIC NUMBER\n"+
    "5-SEARSH IN THE DATA\n"+
    "6-GET THE AVREAGE\n"+
    "7-EXIT\n")
    if op.strip().lower() == "add" :
        add()
        print(data)
    elif op.strip().lower()== "remove":
        remove()
        print(data)
    elif op.strip().lower() == "update":
        update()
        print(data)
    elif op.strip().lower()== "show":
        show()
        print(data)
    elif op.strip().lower()== "searsh":
        searsh()
        print(data)
    elif op.strip().lower()== "avreage":
        avreg()
        print(data)  
    elif op.strip().lower() ==  "exit" :
        print("ok")
        break
    else:
        print("the operation is not exsit")
    is_exit = input("will you exit(y/n)")   
    if is_exit == "y":
        break 