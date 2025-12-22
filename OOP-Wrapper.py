print("         Welcome to our new program :)        ")
print("Employee Managament System.")
print()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getData(self):
        print(f"Name : {self.name}   Age : {self.age}")

class Employee:
    def __init__(self,name,age,empId,salary):
        self.name = name
        self.age = age
        self.empId = empId
        self.salary = salary

    def getData(self):
        print(f"Name : {self.name}   Age : {self.age}   empId : {self.empId}    salary : {self.salary}")

class Manager(Employee):
    def __init__(self,name,age,empId,salary,department):
        super().__init__(name,age,empId,salary)
        self.department = department

    def getData(self):
        print(f"Name : {self.name}   Age : {self.age}   empId : {self.empId}    salary : {self.salary}  Department : {self.department}")


per = []
emp = []
man = []

while True:
    print("\n Enter 1 to  create a Person")
    print("\n Enter 2 to  create an Employee")
    print("\n Enter 3 to  create a Manager")
    print("\n Enter 4 to  show details.")
    print("\n Enter 0 to  exit.")

    Choice = int(input("Enter your choice here : "))

    if Choice == 1 :
        name = input("Enter Person name : ")
        age = int(input("Enter Person age : "))
        
        obj = Person(name,age)
        per.append(obj)

        print("\n Person added successfully :)!\n")

    elif Choice == 2 :
        name = input("Enter Employee name : ")
        age = int(input("Enter Employee age : "))
        empId = input("Enter employee empId(eg:-E1,E2) : ")
        salary = int(input("Enter Employee salary : "))
        
        obj = Employee(name,age,empId,salary)
        emp.append(obj)
        
        print("\n Employee added successfully :)\n")

    elif Choice == 3:
        name = input("Enter Manager name : ")
        age = int(input("Enter manager age : "))
        empId = input("Enter manager (eg:-M1,M2) : ")
        salary = int(input("Enter manager salary : "))
        department = input("Enter manager's department(eg:-Hr,Sales) : ")

        obj = Manager(name,age,empId,salary,department)
        man.append(obj)

        print("Manager addedd successfully :)")             


    elif Choice == 4:
        while True:

            print("Enter 1 to watch Person's details.")
            print("Enter 2 to watch Employee's details.")
            print("Enter 3 to watch Manager's details.")
            print("Enter 0 to Exit from this details.")

            Ch = int(input("Choose option given above : "))
            
            # obj1 = Employee()
            # obj2 = Manager()

            if Ch == 1:
                obj = Person(name,age)
                print(obj.getData())

            elif Ch == 2:
                obj1 = Employee(name,age,empId,salary)
                print(obj1.getData())

            elif Ch == 3:
                obj2 = Manager(name,age,empId,salary,department)
                print(obj2.getData())

            elif Ch == 0:
                print("Go back to main menu.")
                break

            else:
                print("You entered Invalid choice :(")

    elif Choice == 0:
        print("\n Thanks for visiting our 'Employee Managament' Programme :) ")
        break

    else:
        print("Your entered choice is invalid :(")

