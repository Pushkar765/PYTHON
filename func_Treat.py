print("Welcome to the 'Data Analyzer and Transformer' Program :) ")

Record = []
li = []


while True:
    
    print("Enter 1 for Input data.")
    print("Enter 2 for Display data summary.")
    print("Enter 3 for Calculate the factorial.")
    print("Enter 4 for Filter data by threshold.")
    print("Enter 5 for Sort data.")
    print("Enter 6 for Display Dataset static.")
    print("Enter 0 for Exit the programe.")

    Choice = int(input("\n Enter your choice : "))

    if Choice == 1:

        Num = int(input("Enter the number of element : "))

        for i in range(Num):
            val = int(input("Enter the number for list : "))
            li.append(val)
        print(li)

        print("\n Data stored successfully :) \n")

    elif Choice == 2:
        
        Sum = sum(li)
        Count = len(li)
        Avg = 0

        def datasummary():
            '''This is function of Data_Summary.'''
            print("Total elelments in list :")
            print(len(li))
            print()
            print("Minimum value of list :")
            print(min(li))
            print()
            print("Maximum value of list :")
            print(max(li))
            print()
            print("Sum of list's All value :")
            print(sum(li))
            print()
            print("Average value of list :")
            if Count > 0:
                global Avg
                Avg = Sum/Count
                
                print(Avg)
            else:
                print("We can't calculate the Average of empty list.")
            
        datasummary()
        print(datasummary.__doc__)

    elif Choice == 3:

        def fact(a):
            if a<1:
                return print("Number is inavalid.")
    
            if a==1:
                return 1

            return a*fact(a-1)

        num = int(input("Enter the number for calculate factorial : "))
        result = fact(num)
        print(result)

    elif Choice == 4:

        New_li = list(filter(lambda x: x %2 == 0,li))
        print(New_li)

    elif Choice == 5:

        print("Choose 1 for the Ascending Oreder.")
        print("Choose 2 for the Descending Order.")
        print()
        Ch = int(input("Enter your choice here : "))
        
        if Ch == 1:
            li.sort()
            print(li)
            print()
        elif Ch == 2:
            li.sort(reverse=True)
            print(li)
            print()
        else:
            print("Your entered choice is invalid :(")

    elif Choice == 6:
        print("Data set static is similiar like Data summary.")
        print()
        print(f"- Total elements in list : {len(li)}")
        print()
        print(f"- Minimum value in list : {min(li)}")
        print()
        print(f"- MAximum value in list : {max(li)}")
        print()
        print(f"- Sum of all values in list : {sum(li)}")
        print()
        print(f"- Average value in list : {Avg}")
        print()

    elif Choice == 0:
        print("\n thanks for visiting our 'Data Analyzer and Transformer' Program :) ")
        break

    else:
        print("your entered number is invalid :(")

