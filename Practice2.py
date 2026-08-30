# print("===============")
# print("Welcome to Interactive Personal Data-Collector 😊")
# print("===============")


# Name = input("Enter your name here : ")
# Age = int(input("Enter your age here : "))
# Height = input("Enter your Height here : ")
# Weight = float(input("Enter your Weight here : "))
# Hobby = input("Enter your Hobby here : ")
# Frt_Nbr = int(input("Enter your Favourite-Number here : "))
# print()

# print("Thanks to you, to Share us your personal Information 😊")
# print("~~~~~~~~~~~~~~~~~~~~~~~~")

# print("And here is the Information we collected from you 😊")
# print("--------------")
# print("--------------")

# print(f"Name : {Name} , Entered Name's DataType : {type(Name)} , And your Name's Memory Address : {id(Name)}.")
# print()
# print(f"Age : {Age} , Entered Age's DataType : {type(Age)} , And your Age's Memory Address : {id(Age)}.")
# print()
# print(f"Height : {Height} , Entered Height's DataType : {type(Height)} , And your Height's Memory Address : {id(Height)}.")
# print()
# print(f"Weight : {Weight} , Entered Weight's DataType : {type(Weight)} , And your Weight's Memory Address : {id(Weight)}.")
# print()
# print(f"Hobby : {Hobby} , Entered Hobby's DataType : {type(Hobby)} , And your Hobby's Memory Address : {id(Hobby)}.")
# print()
# print(f"Favourite-Number : {Frt_Nbr} , Entered Favourite-Number's DataType : {type(Frt_Nbr)} , And your Favourite-Number's Memory Address : {id(Frt_Nbr)}.")
# print()

# BirthYear = 2025 - Age

# print(f"We find out your Birth-Year from your Age : {BirthYear}.")
# print()
# print("===============")
# print("I'm Glad you helped us to Test our Project 🤗")
# print("===============")


# print("===============")
# print("Welcome to our new project Logic-Box 😊")
# print("===============")
# sum = 0

# while True:

#     print("Enter 1 to create Pattern.")
#     print("Enter 2 to Analyze the numbers it's odd OR it's even.")
#     print("Enter 0 to exit the program.")
#     print()

#     Choice = int(input("Enter your choice here : "))

#     if Choice == 1:

#         for i in range(6,0,-1):
#             print(" 😎 "*i)
#         print()

#     elif Choice == 2:

#         print()
#         Starting = int(input("Enter the Starting range number : "))
#         Exiting = int(input("Enter the Exiting range number : "))
        
#         print()

#         for i in range(Starting , Exiting+1):

#             if i%2 == 0:
#                 print("This Number is 'Even'.",i)
#             else:
#                 print("This Number is 'Odd'.",i)
#             sum += i
        
#         print()
#         print("Here is your given range's sum : ",sum) 
#         print()


#     elif Choice == 0:

#         print()
#         print("Thanks for visiting OUR project 😊")

#         break

#     else:

#         print("Invalid Choice.")

# print("===============")
# print("Welcome to OUR new project Collection_Manipulator.")
# print("===============")

# Data = []

# while True:

#     print("Enter 1 to Add Student.")
#     print("Enter 2 to View Student.")
#     print("Enter 3 to Delete the Student.")
#     print("Enter 4 to Update Student.")
#     print("Enetr 5 to Display subjects offered by Us.")
#     print("Enter 0 to Exit our Project.")
#     print()

#     Choice = int(input("Enter your Choice here : "))
#     print()

#     if Choice == 1:

#         Stud ={
            
#             "ID" : int(input("Enter Student ID here : ")) ,
#             "Name" : input("Enter your name here : ") ,
#             "Age" : int(input("Enter your Age here : ")) ,
#             "Grade" : input("Enter your Previous Grade here : ") ,
#             "Date-Of-Birth" : input("Enter your Date-Of-Birth(YYYY-MM-DD) : ") ,
#             "Subject" : input("Enter your Subject_Group given by US : ")
#         }

#         Data.append(Stud)
#         print()
#         print("Student's all details Added successfully.")
#         print()

#     elif Choice == 2:

#         St_ID = int(input("Enter Student_ID to view : "))

#         for Student in Data:

#             if St_ID == Student["ID"]:
#                 print(f"ID : {Student["ID"]} , Name : {Student["Name"]} , Age : {Student["Age"]} , Grade : {Student["Grade"]} , DOB : {Student["Date-Of-Birth"]} , Subject_Group : {Student["Subject"]}")   
#             else:
#                 print("Student_ID is invalid.")

#     elif Choice == 3:

#         St_ID = int(input("Enter Student_ID to Delete : "))

#         for Student in Data:

#             if St_ID == Student["ID"]:
#                 Data.remove(Student)
#                 print("Your given Student Id's Student's data deleted succesfully.")

#             else:

#                 print("Student not found in Data.")

#     elif Choice == 4:

#         St_ID = int(input("Enter Student Id to Update : "))

#         for Student in Data:

#             if St_ID == Student["ID"]:

#                 Student["Name"] = input("Enter the Student's Name : ")
#                 Student["Age"] = int(input("Enter the Student's Age : "))
#                 Student["Grade"] = input("Enter the Student's Grade : ")
#                 Student["Dob"] = input("Enter the Student's Date-Of-Birth : ")
#                 Student["Subject"] = input("Enter the Student's Subject : ")

#                 print("Student Updated Successfully ")

#             else:

#                 print("Student not found in Data.")

#     elif Choice == 5:

#         St_ID = int(input("Enter your Student ID to view your Subject group : "))

#         for Student in Data:

#             if St_ID == Student["ID"]:

#                 print(f"Your Subject group is :{Student["Subject"]} ")
            
#             else:

#                 print("Your given ID not available in Data.")
    
#     elif Choice == 0:

#         print("Thanks for Visiting our Project.")
#         break

#     else:

#         print("Your Entered choice is invalid.")



