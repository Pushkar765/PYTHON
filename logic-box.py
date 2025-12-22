print("Welcome to our new project GUYS."," :) ")
print()

print("Project's name is logic-box.")
print()

while True:

    print("Select one option of the options given below:")
    print()

    print("1.When you want to create pattern","So,","Choose this option.")
    print("2.When you want to check numbers even and odd","So,","Choose this option.")
    print("0.When you want to exit from this program","So,","Choose this option.")
    print()

    choice = int(input("Enter your choice here: "))

    if choice==1:
       for i in range(1,6):
        for j in range(1,i+1):
            print(str(j),end=" ")
        print()

    elif choice==2:
       
       start = int(input("Enter the starting range of numbers Which you want to check 'even' and 'odd': "))
       exit = int(input("Enter the exiting range of numbers Which you want to check 'even' and 'odd': "))
       sum = 0

       for i in range(start,exit+1):
          
        if i%2==0:
            print("The num is 'even'.",i)
        else:
            print("The num is 'odd'.",i)

        sum += i
        print("Here's your sum of numbers: ",sum)

    elif choice==0:
       print("Thanks for visit our program.")
       print(":)")

       break

    else:
       print("Invalid choice.")
   
