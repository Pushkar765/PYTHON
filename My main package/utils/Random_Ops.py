import random

Li = []

def Ran_num():

    Start = int(input("Enter the number/value Which numbers you want : "))
    End = int(input("Enter the number/value Which you go far : "))

    print(random.randint(Start,End))

def Ran_List():

    List = input("Enter names you want to make list : ")

    Li.append(List)

    print(Li)

def Ran_pass():

    digit = ["0","1","2","3","4","5","6","7","8","9"]
    Symbol = ["@","#","$"]
    Space = ["__"]

    pw_1 = random.choice(Symbol)
    pw_2 = random.choice(Space)
    pw_3 = random.choice(digit)
    pw_4 = random.choice(digit)
    pw_5 = random.choice(digit)
    pw_6 = random.choice(digit)
    pw_7 = random.choice(digit)
    pw_8 = random.choice(digit)
    pw_9 = random.choice(digit)
    pw_10 = random.choice(digit)

    M_Pass = pw_1 + pw_2 + pw_3 + pw_4 + pw_5 + pw_6 + pw_7 + pw_8 + pw_9 + pw_10 + pw_2 + pw_1

    print(M_Pass)

def Ran_OTP():

    print(random.randint(100000,999999))

