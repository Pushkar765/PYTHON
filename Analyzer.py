print("Welcome to our new project Analyzer :)")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print()

import numpy as np
First_Ar = None
Second_Ar = None
list1 = []
Third_Ar = None

class Analyzer:

    def __init__(self):
        self.name = None
        self.First_Ar = None
        self.Second_Ar = None
        self.Third_Ar = None

    def Crt_Array(self):

        while True:

            print()
            print("Enter 1 to Create 1D Array.")
            print("Enter 2 to Create 2D Array.")
            print("Enter 0 to Go-Back to Main-Menu.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            Choice = int(input("Enter your Choice here : "))

            if Choice == 1:

                Elements = input("Enter the Elements for the separated by ',' : ").split(",")
                Nums = [int(x) for x in Elements]
                print(Nums)

            elif Choice == 2:

                Row = int(input("Enter the number of rows : "))
                Column = int(input("Enter the number of Column : "))
                Mult = Row * Column
                Elements = input(f"""Enter the {Mult} Elements for Array sparated by ',' : """).split(",")
                Length = len(Elements)
                print(Length)
                list1.append(Length)

                if Length == Mult:

                    Nums = [int(x) for x in Elements]
                    num = np.array(Nums)
                    Two_d_Array = num.reshape(Row,Column)
                    self.First_Ar = Two_d_Array

                    print(self.First_Ar)
                else:
                    print("You entered more or less elements which you given above.")

            elif Choice == 0:
                print("You're Going-Back to Main-Menu.")
                break

            else:
                print("You entered Invalid choice of Create Numpy Array :(")


    def Perform_Mathematical_Ops(self):
        
        while True:

            print()
            print(self.First_Ar)
            print()
            print("Now,Enter the second array to do Any Mathematical Operation with first array (same-size of array as you wrote above.)")
            print()

            Row = int(input("Enter the number of rows : "))
            Column = int(input("Enter the number of Column : "))
            Mult = Row * Column
            Elements = input(f"""Enter the {Mult} Elements for Array separated by ',' : """).split(",")

            if len(Elements) == Mult:

                Nums = [int(x) for x in Elements]
                num = np.array(Nums)
                self.Second_Ar = num.reshape(Row,Column)

                print(self.Second_Ar)
            else:
                print("You entered more or less elements which you given above.")

            while True:
                print()
                print("Enter 1 to Perform a Addition of Array.")
                print("Enter 2 to Perform a Subtraction of Array.")
                print("Enter 3 to Perform a Multiplication of Array.")
                print("Enter 4 to Perform a Division of Array.")
                print("Enter 0 to Go-Back to Main-Menu.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                Choice = int(input("Enter your Choice here : "))

                if Choice == 1:
                    
                    Total = np.add(self.First_Ar,self.Second_Ar)
                    print(f"""Total of Array : \n {Total}""")

                elif Choice == 2:
                    
                    Subtraction = self.First_Ar - self.Second_Ar
                    print(f"""Subtraction of Array: \n {Subtraction}""")

                elif Choice == 3:
                    
                    Multiplication = self.First_Ar * self.Second_Ar
                    print(f"""Multiplication of array : \n {Multiplication}""")

                elif Choice == 4:
                    
                    Division = self.First_Ar / self.Second_Ar
                    print(f"""Division of Array : \n {Division}""")

                elif Choice == 0:
                    print("You're Going-Back to Main-Menu.")
                    break

                else:
                    print("You entered Invalid choice of Mathematical Operations :(")
                    print()

            break

    def Comb_Split_Ops(self):

        while True:

            print()
            print("Enter 1 to Combine array.")
            print("Enter 2 to Split array.")
            print("Enter 0 to Go-Back to Main-Menu.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            Choice = int(input("Enter your Choice here : "))

            if Choice == 1:

                print()
                print("Now,Enter the Third array to Combine with first array.")
                print("Note: Number of Columns must be same. Rows can be anything")
                print()

                
                Row = int(input("Enter the number of rows : "))
                Column = int(input("Enter the number of Column : "))
                Mult = Row * Column
                Elements = input(f"""Enter the {Mult} Elements for Array separated by ',' : """).split(",")

                if len(Elements) == Mult:

                    Nums = [int(x) for x in Elements]
                    num = np.array(Nums)
                    self.Third_Ar = num.reshape(Row,Column)

                    print(self.Third_Ar)
                    print()
                else:
                    print("You entered more or less elements which you given above.")

                while True:

                    print("Enter 1 to create Array Horizontally.")
                    print("Enter 2 to create Array Vertically.")
                    print("Enter 0 to G-Back to the Combine Or Split Array Menu.")
                    print()
                    
                    In_Choice = int(input("Enter your Choice here : "))

                    if In_Choice == 1:
                        
                        print()
                        self.Combine = np.hstack((self.First_Ar,self.Third_Ar))
                        print(f"""Your horizontally Combined Array : \n {self.Combine}""")
                        print()

                    elif In_Choice == 2:

                        print()
                        self.Combine = np.vstack((self.First_Ar,self.Third_Ar))
                        print(f"""Your vertically Combined Array : \n {self.Combine}""")
                        print()

                    elif In_Choice == 0:

                        print("Now you're Going-Back to Combine Or Split Array.")
                        break

                    else: 
                        print("Your entered choice is Invalid :(")
                        

            elif Choice == 2:
            
                print()
                Parts = int(input("Enter Digit you want to Create how many parts of array : "))
                Split = np.split(self.First_Ar,Parts)
                Vertical_array = np.vstack(Split)
                Horizontal_array = np.hstack(Split)
                print(f"""Splited Array : \n {Split}""")
                print()

                print("Combined array in vertical.")
                print(f"""Vertical Array : \n {Vertical_array}""")
                print()

                print("Combined array in horizontal.")
                print(f"""Horizontal Array : \n {Horizontal_array}""")
                print()

            elif Choice == 0:

                print("Now you're Going-Back to Main-Menu.")
                break

            else:

                print("You entered Invalid choice of Combine OR split Operations :(")

    def Srch_Srt_Fltr(self):

        while True:

            print()
            print("Enter 1 to Search any digit of array.")
            print("Enter 2 to Sort the array.")
            print("Enter 3 to filter the array.")
            print("Enter 0 to Go-Back to Main-Menu.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            Choice = int(input("Enter your Choice here : "))

            if Choice == 1:

                Digit = int(input("Enter the Digit which you want to search(Enter valid digit which was already in your created array) : "))
                Srch = np.where(self.First_Ar == Digit)
                print(f"Searched value : \n {Srch}")

            elif Choice == 2:
                
                print("Enter 1 to Sort Row-Wise.")
                print("Enter 2 to Sort Column-Wise.")
                print("Enter 0 to Go to the Search,Sort & Filter Array.")

                Choose = int(input("Choose your Option here : "))

                if Choose == 1:

                    Sort = np.sort(self.First_Ar,axis=1)
                    print(f"Sorted value : \n {Sort}")

                elif Choose == 2:

                    Sort = np.sort(self.First_Ar,axis=0)
                    print(f"Sorted value : \n {Sort}")

                elif Choose == 0:

                    print("You're Going-Back to Search,Sort & Filter Menu.")
                    break

            elif Choice == 3:

                digit = int(input("Enter the digit you want to check the array is greater than or not : "))
                Filtered = self.First_Ar[self.First_Ar > digit]
                print(f"Your Filtered value : \n {Filtered}")

            elif Choice == 0:

                print("Now you're Going-Back to Main-Menu.")
                break

            else:

                print("You entered Invalid choice of Search,Sort & Filter Operations :(")

    def Aggre_Stat_Ops(self):

        while True:

            print()
            print("Enter 1 to find Sum of array.")
            print("Enter 2 to find Mean of array.")
            print("Enter 3 to find Median of array.")
            print("Enter 4 to find Standard-deviation of array.")
            print("Enter 5 to find Variance of array.")
            print("Enter 6 to find Minimum value of array.")
            print("Enter 7 to find Maximum value of array.")
            print("Enter 0 to Go-Back to Main-Menu.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            Choice = int(input("Enter your Choice here : "))

            if Choice == 1:

                Sum = np.sum(self.First_Ar)
                print()
                print(f"Sum of Array : {Sum}")

            elif Choice == 2:

                Mean = np.mean(self.First_Ar)
                print()
                print(f"Mean of Array : {Mean}")

            elif Choice == 3:

                Median = np.median(self.First_Ar)
                print()
                print(f"Median of Array : {Median}")

            elif Choice == 4:

                Std_Dev = np.std(self.First_Ar)
                print()
                print(f"Standard-Deviation of Array : {Std_Dev}")

            elif Choice == 5:

                Variance = np.var(self.First_Ar)
                print()
                print(f"Variance of Array : {Variance}")

            elif Choice == 6:

                Minimum = np.min(self.First_Ar)
                print()
                print(f"Minimum of Array : {Minimum}")

            elif Choice == 7:

                Maximum = np.max(self.First_Ar)
                print()
                print(f"Maximuum of Array : {Maximum}")

            elif Choice == 0:

                print()
                print("Now you're Going-back to Main_menu.")
                break

            else:

                print("You entered Choice of Aggregates & Statistical operations.")




A_File = Analyzer()
while True:

    print()
    print("Enter 1 to Create Numpy Array.")
    print("Enter 2 to Perform Mathematical Operations on Array.")
    print("Enter 3 to Combine Or Split Array.")
    print("Enter 4 to Search,Sort and Filter Array.")
    print("Enter 5 to Compute Aggregates Or Statistics.")
    print("Enter 0 to exit the programme.")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^")

    Operations = int(input("Enter your choice here : "))

    if Operations == 1:

        A_File.Crt_Array()

    elif Operations == 2:

        A_File.Perform_Mathematical_Ops()

    elif Operations == 3:

        A_File.Comb_Split_Ops()

    elif Operations == 4:

        A_File.Srch_Srt_Fltr()

    elif Operations == 5:

        A_File.Aggre_Stat_Ops()

    elif Operations == 0:

        print("Thanks for visiting our Programme Analyzer :)")
        break

    else:

        print("You're entered Invalid choice of Operations :( ")

