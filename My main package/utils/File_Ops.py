File_Name = 0

def Crt_File():
    global File_Name
    File_Name = input("Enter File name what you want : ")
    file = open(File_Name,"w")
    print("Your file is created.")
    file.close()


def Wrt_File():
    global File_Name
    file = open(File_Name,"w")
    file.write(input("Enter what  you written here : "))
    print("Your Message is printed successfully.")
    file.close()
    
def Read_file():
    global File_Name
    file = open(File_Name,"r")
    Lines = file.readlines()

    for i in Lines:
        print(i)
        file.close()

def Append_File():
    global File_Name
    file = open(File_Name,"a")
    file.write(input("Enter your New message here : "))
    print("Your new message printed successfully :)")
    file.close()
