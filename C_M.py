Record = []

while True:
    
    print("\n Welcome to Our New Programme. \n")


    print("Enter 1 to add Student.")
    print("Enter 2 to view Student.")
    print("Enter 3 to Delete Student.")
    print("Enter 4 to Update Student.")
    print("Enter 5 to Display Subjects offered.")
    print("Enter 0 to 'Exit'.")

    Choice = int(input("\n Enter your choice: "))

    if Choice==1:
        st = {
            "Id":int(input("Enter student Id : ")),
            "Name":input("Enter your Name : "),
            "Age":int(input("Enter students Age : ")),
            "Grade":input("Enter Your Grade : "),
            "DOB":input("Enter your Date of birth (YYYY-MM-DD) : "),
            "Subject":input("Plaese Enter Your Subjects : ")
        }

        Record.append(st)
        print("\n Student added successfully. \n")

    elif Choice==2:
        stid = int(input("\n Enter student id to View : "))
        for student in Record:
            if stid==student["Id"]:
                print(f"Id:{student["Id"]},Name:{student["Name"]},Age:{student["Age"]},Grade:{student["Grade"]},DOB:{student["DOB"]},Subject:{student["Subject"]}")
            else:
                print("Student Id is invalid.")

    elif Choice==3:
        stid = int(input("\n Enter student Id to Delete : "))
        for student in Record:
            if stid==student["Id"]:
                Record.remove(student)
                print("Your given Id's student is Deleted successfully.")
            else:
                print("Student not found in Record.")

    elif Choice==4:
        stid = int(input("\n Enter Studnet Id to Update : "))
        for student in Record:
            if stid==student["Id"]:
                student["Name"] = input("Enter student name : ")
                student["Age"] = int(input("Enter student Age : "))
                student["Grade"] = input("Enter your grade : ")
                student["DOB"] = input("Enter your Date of birth(YYYY-MM-DD) : ")
                student["Subject"] = input("Enter your subject : ")
                print("Student updated successfully. :)")
            else:
                print("Student not found in Record.")

    elif Choice==5:

        print("\n Enter 1 to view Science.")
        print("Enter 2 to view Maths.")
        print("Enter 3 to view English.")
        print("Enter 4 to view Gujarati.")
        print("Enter 5 to view Hindi.")
        print("Enter 6 to view Sanskrit.")
        print("Enter 0 to view all the Sibjects.")

        Ch = int(input("\n Enter your choice : "))

        if Ch==1:
            print("You choosed Science subject.")
        elif Ch==2:
            print("You choosed Maths subject.")
        elif Ch==3:
            print("You choosed English subject.")
        elif Ch==4:
            print("You choosed Gujarati subject.")
        elif Ch==5:
            print("You choosed Hindi subject.")
        elif Ch==6:
            print("You choosed Sanskrit subject.")
        elif Ch==0:
            print("You choosed All subjects.")
        else:
            print("Your entered choice is invalid.")
        

    elif Choice==0:
        print("\n Thanks for visiting our new programme. :) \n")
        break

    else:
        print("\n Your entered number choce is invalid. \n")

