from utils import Datetime_ops
from utils import Math_ops
from utils import Random_Ops
from utils import File_Ops
import uuid

def UUID():
    print(uuid.uuid4())


def Dir_():
    Mod_Name = input("Enter module name : ")

    try:
        Mod_ = __import__(Mod_Name)

        print(f"All module Attributes in {Mod_Name} module.")
        print(dir(Mod_))
    except:
        print("Your entered module name is Invalid.")

print("=====================")
print("Welcome to our new programme 'Multi-Utility Tool-kit'. ")
print("=====================")
print()

if __name__ == "__main__":

    while True:

        print("-Enter 1 to perform DateTime and Time operations.")
        print("-Enter 2 to perform Mathematical operations.")
        print("-Enter 3 to perform Random Data Genrations.")
        print("-Enter 4 to perform Generate Unique Identifiers (UUID).")
        print("-Enter 5 to perform File Operations(Custom Modules).")
        print("-Enter 6 to perform Explore Module Atributes(dir()).")
        print("-Enter 0 to Exit Programme.")
        print("=================")

        Choice = int(input("Enter your Choice Here : "))

        if Choice == 1:
            print("DateTime and Time Operations : ")
            print("=====")

            while True:
                
                print("Enter 1 to Display Current Date Time.")
                print("Enter 2 to Calculate Difference Between two dates/times.")
                print("Enter 3 to Format date into Custom date.")
                print("Enter 4 to Stop-watch.")
                print("Enter 0 to Go back to main menu.")
                print()
                print("= = = = =")
                choice = int(input("Enter your Choice Here : "))
                print("= = = = =")

                if  choice == 1:

                    Datetime_ops.C_datetime()

                elif choice == 2:

                    dt_1 = input("Enter dates : ")
                    dt_2 = input("Enter dates : ")

                    Datetime_ops.Difr_btwn_tim_dt(dt_1,dt_2)

                elif choice == 3:

                    Datetime_ops.format_into_cstm()

                elif choice== 4:

                    Datetime_ops.stop_watch()
                    
                elif choice == 0:
                    print("=================")
                    print("""Thanks for visiting DateTime and Time Operations.
                        Now You're going to main menu.""")
                    print("=================")
                    
                    break

                else:
                    print("Your Entered Choice is Invalid.")
        

        elif Choice == 2:

            while True:

                print("Enter 1 to Calculate factorial.")
                print("Enter 2 to Solve Compound Intrest.")
                print("Enter 0 to Go back to main menu.")
                print("= = = = =")
                choice = int(input("Enter your choice here : "))
                print("= = = = =")

                if choice == 1:
                    
                    Math_ops.Calculate_Fact()

                elif choice == 2:
                    
                    Math_ops.Compound_Intrest()

                elif choice == 0:
                    print("=================")
                    print("""Thanks for visiting Mathematical-Operations,
                        you're going to main menu.""")
                    print("=================")
                    break

                else:
                    print("Your Entered Choice is Invalid.")

        elif Choice == 3:

            while True:

                print("Enter 1 to Generate Random Number.")
                print("Enter 2 to Generate Random List.")
                print("Enter 3 to Generate Random Password.")
                print("Enter 4 to Generate Random OTP.")
                print("Enter 0 to Go back to main menu.")
                print("= = = = =")
                choice = int(input("Enter your choice here : "))
                print("= = = = =")

                if choice == 1:

                    Random_Ops.Ran_num()

                elif choice == 2:

                    Random_Ops.Ran_List()

                elif choice == 3:
                    Random_Ops.Ran_pass()

                elif choice == 4:

                    Random_Ops.Ran_OTP()

                elif choice == 0:
                    print("=================")
                    print("""Thanks for visiting Random Data generation,
                        Now you're going to main menu.""")
                    print("=================")
                    break
                    
                else:
                    print("Your Entered Choice is Invalid.")

        elif Choice == 4:

            UUID()

        elif Choice == 5:

            while True:

                print("Enter 1 to Create a New File.")
                print("Enter 2 to Write to a File.")
                print("Enter 3 to Read a File.")
                print("Enter 4 to Append a File.")
                print("Enter 0 to Go back to main menu.")
                print("= = = = =")
                choice = int(input("Enter your choice here : "))
                print("= = = = =")

                if choice == 1:
                    
                    File_Ops.Crt_File()
                    
                elif choice == 2:
                    
                    File_Ops.Wrt_File()
                    
                elif choice == 3:
                    
                    File_Ops.Read_file()

                elif choice == 4:

                    File_Ops.Append_File()

                elif choice == 0:
                    print("=================")
                    print("""Thanks for visiting Random Data generation,
                        Now you're going to main menu.""")
                    print("=================")
                    break

        elif Choice == 6:

            Dir_()

        elif Choice == 0:
            print("=================")
            print("Thanks for Visiting our programme 'Multi-Utility Tool-kit'.")
            print("")
            break

        else:
            print("Your entered Choice is Invalid :( ")