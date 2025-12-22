import math

def Calculate_Fact():

    Num = int(input("Enter the number you want a factorial : "))

    print(math.factorial(Num))

def Compound_Intrest():

    Principal_Amount = float(input("Enter the number principal amount : "))
    Rate_Intrest = float(input("Enter the annual intrest rate : "))
    Time = float(input("Enter the Time in years : "))
    Number = float(input("Enter the number of times intrest compounded in years : "))

    R = Rate_Intrest/100

    intrest = Principal_Amount * (1+R/Number) ** (Number*Time)
    C_I = intrest - Principal_Amount

    print(f"\n Final Amount : {intrest}")
    print(f"\n Final Amount : {C_I}")