#print('hello world')

# """pushkar jayeshbhai bhatti"""
# print("hii boy")
# print("hello world",end=" ")
# print("yo yo")

#print()

#input()
#print("hello")

#input("enter your name: ")
#print("Yo Yo")

# a=2
# b=34
# print(a+b)
# print(a*b)
# print(a/b)
# print()
# print(a)
# a=45
# print(a)

# a=int(input("enter a num: "))
# b=input("enter a num: ")

# print(type(a))
# print(type(b))

# print(a+int(b))

# print(int(34.9))
# print(int(34.4))
# print(int(True))
# print(int(False))

# print(str(23))
# print(str(23.3))
# print(str(True))
# print(str(False))

# print("your name",222222,"fuck no way",123456789)

# print(float("yo"))
# print(float(2121))
# print(float(21.0003))
# print(float(True))
# print(float(False))

# print(bool(""))
# print(bool(" "))
# print(bool("rahul"))
# print(bool(0))
# print(bool(-9999))
# print(bool(23.3))

#arithmetic operators

# a=4
# b=2
# print(a//b)

# a=2
# b=5
# print(a**b)

# a=5
# b=2
# print(a%b)

#assingment operator

# a=2
# a+=2

# print(a)

# a=2
# a-=2
# print(a)

# a=2
# a*=2
# print(a)

# a=10
# a/=5
# print(a)

# a=5
# a%=2
# print(a)

# a=5
# a//=2
# print(a)

# a=5
# a**=2
# print(a)

# a="Pushkar bhatti"
# b=10
# c=3.25461
# d=True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#if statement

# if 10>2:
#     print("Yes this is true")

#if and else statement

# if 10<=13:
#     print("Yes this is true")
# else:
#     print("No this is false")

#ladder statement

# choice=int(input("choose 1 To 5 for free food : "))

# if choice==1:
#     print("You ordered pizza.")
# elif choice==2:
#     print("You ordered burger.")
# elif choice==3:
#     print("You ordered sandwich.")
# elif choice==4:
#     print("You ordered garlic bread.")
# elif choice==5:
#     print("You ordered coke.")
# else:
#     print("The number you clicked is not valid.")

# Num=int(input("Enter a number and check it's odd or even: "))

# if Num%2:
#     print("Your given  number is odd. :)")
# else:
#     print("Your given number is  even. :)")

# Age=int(input("Enter your age here: "))

# if Age<=12:
#     print("You're a child.")
# elif Age<=18:
#     print("You're a teenager.")
# elif Age<=35:
#     print("You're adult.")
# else:
#     print("You're senior citizen.")

# A=int(input("Enter first number: "))
# B=int(input("Enter second number: "))

# if A<B:
#     print("Your entered number is less than Second number.")
# elif A>B:
#     print("Your entered number is greater than Second number.")
# elif A==B:
#     print("Your entered number is both are same.")

# Mark=int(input("Enter your marks here: "))

# if Mark>=90:
#     print("A")
# elif Mark>=75:
#     print("B")
# elif Mark>=50:
#     print("C")
# elif Mark>=33:
#     print("D")
# else:
#     print("Fail")

# mark = int(input("Enter your marks: "))
# grade = ""

# if mark>=90:
#     grade="A"
# elif mark>=75:
#     grade="B"
# elif mark>=50:
#     grade="C"
# elif mark>=33:
#     grade="d"
# else:
#     grade="F"

# if grade=="A":
#     print("You're good in your work.")
#     print("You got A.")
# elif grade=="B":
#     print("You're excellent in your work.")
#     print("You got B.")
# elif grade=="C":
#     print("You're well in your work.")
#     print("You got C.")
# elif grade=="D":
#     print("Your performance is not well  but you're pass.")
#     print("You got D.")
# else:
#     print("You failed led.")
#     print("You got F.")

#nested statement

# print("Enter 1 to order Fast-food.")
# print("Enter 2 to Cold-Drink.")
# print("Enter 3 to order Dessert.")

# choice = int(input("Enter your choice: "))

# if choice==1:
#     print("Enter 1 to order Pizza.")
#     print("Enter 2 to order burger.")

#     ch = int(input("Enter your choice: "))

#     if ch==1:
#         print("Youu ordered a Pizza.")
#     elif ch==2:
#         print("You ordered burger.")
#     else:
#         print("Invalid.")

# elif choice==2:
#     print("Enter 1 to order coke.")
#     print("Enter 2 to order fanta.")

#     ch = int(input("Enter your choice: "))

#     if ch==1:
#         print("Youu ordered coke.")
#     elif ch==2:
#         print("You ordered fanta.")
#     else:
#         print("Invalid.")

# elif choice==3:
#     print("Enter 1 to order brownie.")
#     print("Enter 2 to order Ice-cream.")

#     ch = int(input("Enter your choice: "))

#     if ch==1:
#         print("Youu ordered coke.")
#     elif ch==2:
#         print("You ordered fanta.")
#     else:
#         print("Invalid.")

# else:
#     print("Invalid choice.Please enter number between 1 To 3.:)")

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# if a>b:
#     if a>c:
#         print("A is bigger than 'B' and 'c'.")
#     else:
#         print("C is bigger than 'A' and 'B'.")

# else:
#     if b>c:
#         print("B is bigger than 'A' and 'C'.")
#     else:
#         print("C is bigger than 'A' and 'B'.")

#ternary operator 

# num = int(input("Enter a num: "))

# result="Even" if num%2==0 else "odd"

# print(result)

#looping controls 

#for loop

# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(5):
#     print("Hello World")

# num=int(input("Enter a number to print its Table: "))

# for i in range(1,11):
#     print(num,"X",i,"=",i*num)

# start=int(input("Enter number for starting a range to find 'even' and 'odd' numbers: "))
# end=int(input("Enter number for ending a range to find 'even' and 'odd' numbers: "))

# for i in range(start,end+1):

#     if i%2==0:
#         print("Your Entered number ", i ," is even.")
#     else:
#         print("Your entered number ", i ," is odd")

# range in reverse

# for i in range(20,0,-2):
#     print(i)

# while loop

# i=0

# while i<=10:
#     i+=1
#     print(i)

# while True:
#     num=int(input("Enter a number: "))
#     print("Enter 0 to stop: ") 

#     if num==0:
#         break   

# while True:
#     print("Enter 1 to order Fast-food.")
#     print("Enter 2 to Cold-Drink.")
#     print("Enter 3 to order Dessert.")

#     choice = int(input("Enter your choice: "))

#     if choice==1:
#         print("Enter 1 to order Pizza.")
#         print("Enter 2 to order burger.")

#         ch = int(input("Enter your choice: "))

#         if ch==1:
#             print("Youu ordered a Pizza.")
#         elif ch==2:
#             print("You ordered burger.")
#         else:
#             print("Invalid.")

#     elif choice==2:
#         print("Enter 1 to order coke.")
#         print("Enter 2 to order fanta.")

#         ch = int(input("Enter your choice: "))

#         if ch==1:
#             print("Youu ordered coke.")
#         elif ch==2:
#             print("You ordered fanta.")
#         else:
#             print("Invalid.")

#     elif choice==3:
#         print("Enter 1 to order brownie.")
#         print("Enter 2 to order Ice-cream.")

#         ch = int(input("Enter your choice: "))

#         if ch==1:
#             print("Youu ordered coke.")
#         elif ch==2:
#             print("You ordered fanta.")
#         else:
#             print("Invalid.")

#     elif choice==0:
#         print("Exit from menu bar.")
#         break

#     else:
#         print("Invalid choice.Please enter number between 1 To 3.:)")

#nested loop

# while True:

#     print("Enter 1 to print table of any number.")
#     print("Enter 2 to prinnt even and oodd number range.")
#     print("Enter '0' to exit loop.")

#     choice = int(input("Enter your choice: "))

#     if choice==1:
#         num = int(input("Enter number to print table: "))

#         for i in range(1,11):
#             print(num,"X",i,"=",i*num)
            
#     elif choice==2:
#         start = int(input("Enter the starting range: "))
#         exit = int(input("Enter the exit range: "))

#         for i in range(start,exit+1):
            
#             if i%2==0:
#                 print("The num",i,"is even.")
#             else:
#                 print("The num",i,"is odd.")

#     elif choice==0:
#         print("Visit again.")
#         break

#     else:
#         print("Invalid choice.")

#patterns 

#square matrix  of 5*5

# for i in range (5):
#     print("* * * * *")

# for  i  in range(5):
#     print(" * "*5)

#side triangle

# for i in range(1,6):
#     print(" * "*i)

#reverse side triangle

# for i in range(6,0,-1):
#     print(" * "*i)

# for i in range(6):
#     print(" * "*i)

#numbers matrix

# for i in range(5):
#     print(str(i)*5)

# for i in range(1,6):
#     print(str(i)*i)

#nested number matrix

# for i in range(1,6):
#     for j in range(1,6):
#         print(" * ",end=" ")
#     print()
    
#nested pattern

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(str(j),end=" ")
#     print()

#string formatting

# A = 18

# print("My age is ",A)

#.formatting

# A = 18
# B = "Rajkot"

# print("My age is {} and i'm from {}.".format(A,B))

#f string

# print(f"My age is {A} and i'm from {B}.")

# with %modulo operator

# Name = "Pushkar"
# Age = 18

# Foarmatted_String = "My name  is %s and i'm %d years old." %(Name,Age)

# print(Foarmatted_String)

# you just used %s,%d it is formatting words of modulo %s = string,%d = integer,%f = float and

#string manipulating
#1.Double quotes

# I = '''This is multi-line string
#         y
#         e
#         a
#         h'''

# print(I)

#2.String concantation

# First_name = "Pushkar"
# Last_name = "Bhatti"
# Full_name = First_name+" "+Last_name

# print(Full_name)

#3.Indexing

# name = "Pushkar"

# print(name[0])

#4.Slicing

# Name = "Pushkar"

# print(Name[0:4])  

#5.Index with steps

# name = "Pushkar J. Bhatti"

# print(name[0:4:2])

#In above example starting with 0 ending with 4 and take step of 2

#6. Negative indexing

# name = "Pushkar j. bhatti"

# print(name[-1])
# print(name[-17:-10])

#7.Omitting Indices

# name = "Pushkar j. bhatti"

# print(name[:])
# print(name[::])
# print(name[0::])
# print(name[::1])
# print(name[0::1])
# print(name[0:len(name):1])

#collection data-types
#list
#tuple
#set
#Dict
#string

#---------------------list------------------------#

# L = [23,54,"Apple"]

#--------------------tuple------------------------#

# T = (34,54,"Banana")

#--------------------set-------------------------#

# S = {"Pushkar","Pushkar","Don","Glitch"}

#-------------------Dict------------------------#

# D = {
#     "Name":"Pushkar",
#     "Age":"18",
#     "Married":"Stay-Single"
# }

#------------------string-----------------------#

# STR = ("Fuck youuuuuu")


# print(L)
# print(T)
# print(S)
# print(D)
# print(STR)

#example of difference between set and dict

# A = {}

# print(type(A))

# A = []
# B = ()
# C = {""}
# D = {}


# print(type(A))
# print(type(B))
# print(type(C))
# print(type(D))

#string to list

#first common example

# str = "Rahul is a boy."

# for i in str:
#     print(i)


# print(list(str))

# Ls = str.split()
# print(Ls)

# SS = " ".join(Ls)
# print(SS)


#methods of list


# l = [1,1,1,2,3,4]
# print(l)

# l.append(5)
# print(l)

# l.extend([6,7,8,9])
# print(l)

# l.insert(10,10)
# print(l)

# l.remove(3)
# print(l)

# l.pop()
# print(l)

# l.pop(2)
# print(l)

# l.count(1)
# print(l)

# l = [50,40,60,40]
# print(l.count(40))

# l.sort()
# print(l)

# l.reverse()
# print(l)



#Metods of Tuple

# t = (1,2,3,4,5,1,2)
# del t
# print(t)

#count
# print(t.count(1))

# t = ("Apple","Banana","Grapes")
# print(t.index("Apple"))



#Methods of set

# S = {1,2,3,4,5,3}
# print(S)

# S.add(6)
# print(S)

# S.remove(1)
# print(S)

# S.pop()
# print(S.pop())

# set1 = {1,2,3}
# set2 = {4,5,6}
# print(set1.union(set2))



#Methods of dict

# dt = {
#     "Name":"Pushkar J. Bhatti",
#     "Age":"18",
#     "Subject":["Hindi,gujarati"],
#     "Married":False
# }

# print(D)

# for i in dt:
#     print(i)

# for key,value in dt.items():
#     print(f"{key},{value}")

# print(D.keys())

# print(D.values())

# print(D.items())
# D2 = {
#     "Lang-Known":"Eng,Guj,Hin,Sans",
#     "Country":"India"
# }

# D.update(D2)
# print(D)

# D.pop("Name")
# print(D)


#List of dict

# Ls = [{"id":1,"Name":"Pushkar"}]

# print(Ls[0]["Name"])

# for i in Ls:
#     print(f"Name:{i["Name"]}")
#     for key,value in i.items():
#         print(f"{key}:-{value}")


#Real CRUD operation

# Record = []

# while True:
    
#     print("\n Welcome to Our New Programme. \n")


#     print("Enter 1 to add Student.")
#     print("Enter 2 to view Student.")
#     print("Enter 3 to Delete Student.")
#     print("Enter 4 to Update Student.")
#     print("Enter 0 to 'Exit'.")

#     Choice = int(input("Enter your choice: "))

#     if Choice==1:
#         st = {
#             "Id":int(input("Enter student Id : ")),
#             "Name":input("Enter your Name : "),
#             "Age":int(input("Enter students Age : "))
#         }

#         Record.append(st)
#         print("\n Student added successfully. \n")

#     elif Choice==2:
#         stid = int(input("Enter student id to View : "))
#         for student in Record:
#             if stid==student["Id"]:
#                 print(f"Id:{student["Id"]},Name:{student["Name"]},Age:{student["Age"]}")
#             else:
#                 print("Student Id is invalid.")

#     elif Choice==3:
#         stid = int(input("Enter student Id to Delete : "))
#         for student in Record:
#             if stid==student["Id"]:
#                 Record.remove(student)
#                 print("Your given Id's student is Deleted successfully.")
#             else:
#                 print("Student not found in Record.")

#     elif Choice==4:
#         stid = int(input("Enter Studnet Id to Update : "))
#         for student in Record:
#             if stid==student["Id"]:
#                 student["Name"] = input("Enter student name : ")
#                 student["Age"] = int(input("Enter student Age."))
#                 print("Student updated successfully. :)")
#             else:
#                 print("Student not found in Record.")

#     elif Choice==0:
#         print("Thanks for visiting our new programme. :)")
#         break

#     else:
#         print("Your entered number choce is invalid.")



#Types of function

#1) Built in function
#2) User defined function

#2) User defied function(UDF)

#There are 4 types of write udf
#1.Without parameter and without return
#2.With parameter and without return
#3.With parameter and with return
#4.With parameter and without return

#1.Without parameter and without return
# def yo():
#     print("Pushkar J. Bhatti")

# yo()


#2.With parameter and without return
# def add(a,b):
#     print(a-b)

# add(99999999999999999999999999999999999,1000000000000000000000000000000000000)


#3.With parameter and with return

# def mult(a,b,c):
#     print(a+b*c)

# mult(5,2,10)


#4.Without parameter and without return

#-------this type of UDF is usedd in rare case-------#


#Type of function arguements
#There are four types of arguements

#1)Positional arg.
#2)Default arg.
#4)Keyword arg.
#5)Variable-length arg.

#1.Positional Arguement

# def add(a,b,c):
#     print(a+b+c)

# add(5,6,7)


#2.Default arguement

# def add(a,b):
#     print(a+b)

# add(55,45)


#3.key-word arguement

# def self(name,age):
#     print(f"Name is {name} and Age is {age}")

# self(name = "pushkar",age = 18)

#4.Variable-length arguement
#2 types of  var.len arg
#1st is args(Tuple)
#2nd is kwargs(Dict)

#1st is args

# def a(*args):
#     print(sum(args))

# a(1,2,3,4,5,6,7,8,9)

#2nd is kwargs 

# def yo(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}-{value}")

# yo (name = "PJ",age = 12)

#---------Document String---------#

# def add(a,b):
#     '''This is sum of A+b.'''
#     print(a+b)

# print(add.__doc__)


#Recursion
# a = int(input('Enter the A'))
# def fact(a):
#     if a<1:
#         return print("Number is inavalid.")
    
#     if a==1:
#         return 1

#     return a*fact(a-1)

# num = int(input("Enter number : "))
# result = fact(num)
# print(result)

#Lambda/Anonymous 

# add = lambda x,y:x+y
# print(add(2,2))

#Global key-word

#1st example of global keyword
# x = 50

# def grd():
#     x = 55
#     print(x)

# print(x)
# grd()

#2nd example of global keyword

# x = int(input("Enter the number : "))

# def grd():
#     global x
#     x = x+0
#     print(x)

# grd()

#Returning multiple values from a function
#1) using tuple

# def val():
#     return 1,2,3,4,5

# new = val()
# print(new)

#2)using lists

# def val():
#     return [1,2,3,4,5]

# new = val()
# print(new)

#3)using dictionaries

# def val():
#     return {"name":"pushkar","age":100,"city":"rajkot"}

# new = val()
# print(new)

#4)using multiple return variables

# def val():
#     return 5,10,15,20,25

# a,b,c,d,e = val()
# print(a,b)



#Nested functions.

# def outer_function():
#     def inner_function():
#         #inner's logic
#         print("Hello guys,i'm the og.")

#     inner_function()

# outer_function()

#Nested with variables

# def groot(name):
#     def msg():

#         return f"hy guys,I'm {name},Babita's hubby. :)"
    
#     return msg()

# print(groot("iyer"))

#using return nested function

# def og(fact):
#     def yo(num):

#         return num*fact

#     return yo

# Dub = og(2)
# print(Dub(135))

# def login(username,passsword):
#     def validate():
#         return username == "admin",passsword == "9898"
    
#     if validate():
#         return "login successful"
#     else:
#         return "Invalid candidate"
    
# print(login("admin","9898"))

#----------Array and it's functions-----------
#1)1st type of array is one-dimensional

# Ar = [4,5,6]

# print(Ar[2])
#.
#.
#.
#2)2nd type of array is two-dimensional

# Arr = [
#     [1,2,3],#row 0 with col 0,1,2
#     [4,5,6],#row 1 with col 0,1,2
#     [7,8,9] #row 2 with col 0,1,2
# ]

# print(Arr[2][2])
#.
#.
#.
#3)3rd type of array is 

# Arrr = [
#     [
#         [1,2,3],
#         [1,2,3],
#         [1,2,3]
#     ],
#     [
#         [4,5,6],
#         [4,5,6],
#         [4,5,6]
#     ],
#     [
#         [7,8,9],
#         [7,8,9],
#         [7,8,9]
#     ]
# ]

# print(Arrr)
#.
#.
#.

#min max sum sort sorted filter (list)
#min

# li = [1,25,30,1,5]

# print(min(li))
# print(max(li))
# print(sum(li))
# print(sorted(li))
# nli = sorted(li)
# print(nli)
#sort for ascending order
# li.sort()
# print(li)
#sort for decending order
# li.sort(reverse=True)
# print(li)

#min max sum sort sorted filter for (tuple)

# li = (50,8,7,47,51,62,4)

# print(min(li))
# print(max(li))
# print(sum(li))
# print(sorted(li))
# nli = sorted(li)
# print(nli)
#sort is not for tuple 

#filter on list

# li = [34,65,2,3]
# nl = list(filter(lambda x: x%2==0,li))
# print(nl)

# Num = int(input("Enter the element number  : "))

# li = []

# for i in range(Num):
#     val = int(input("Enter the number : "))

#     li.append(val)
# print(li)


#Class brand

# class Car:
#     Brand = None
#     Model = None

#     def grd(self):
#         print("Hello")

# obj = Car()
# obj2 = Car()
# obj3 = Car()

# obj.Brand = "Bugatti"
# obj2.Brand = "Lamborghinim"
# obj3.Brand = "BMW"


# obj.Model = "Tourbillion"
# obj2.Model = "Urus"
# obj3.Model = "M3" 

# print(obj.Brand)
# print(obj.Model)

# print(obj2.Brand)
# print(obj2.Model)

# print(obj3.Brand)
# print(obj3.Model)


# class Laptop:
#     Brand = None
#     Model = None
#     Version = None


# obj = Laptop()
# obj2 = Laptop()
# obj3 = Laptop()

# obj.Model = "Asus"
# obj2.Model = "Lenovo"
# obj3.Model = "Asus"

# obj.Brand = "Strix"
# obj2.Brand = "Loq"
# obj3.Brand = "Tuff"

# obj.Version = "G-16"
# obj2.Version = "Essential"
# obj3.Version = "A-15"

# print(obj.Model,obj.Brand,obj.Version)
# print(obj2.Model,obj2.Brand,obj2.Version)
# print(obj3.Model,obj3.Brand,obj3.Version)

#Encapsulation 

# class Person:
#     __name : None
#     __age : None
#     __city : None

#     def setData(self,name,age,city):
#         self.__name = name
#         self.__age = age
#         self.__city = city

#     def getData(self):
#         print(f"name : {self.__name}, Age : {self.__age}, city : {self.__city}.")

# One = Person()
# Two = Person()

# One.setData("pj",23,"rajkot")
# One.getData()

# Two.setData("hb",25,"kagdadi")
# Two.getData()

#Constructor And De-constructor

# class Car:
#     def __init__(self):
#         print("Hello this is constructor.")

#     def grd(self):
#         print("hello")

#     def __del__(self):
#         print("The work is over.")

# obj = Car()


# class Car:
    # name = None

#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def grd(self):
#         print(f"hello {self.name} {self.age} {self.city}")

#     def __del__(self):
#         print("The work is over.")

# obj = Car("pj",100,"Miami")

# obj.grd()


#inheritance
 

#single level inharitance

# class Parent:
#     name = "Randva"
#     def grd(self):
#         print("Hello from parents.")

# class Child(Parent):
#     def grdch(self):
#         print("Hello from child.")

# obj = Child()

# print(obj.name)
# obj.grdch()
# obj.grd()

#Multiple inheritance

# class Parent:
#     name = "brad pitt"
#     def grd(self):
#         print("Helo from guru ghantal.")

# class Parent2:
#     name = "angelina jollie"
#     def grdch(self):
#         print("Hello from baba jio.")

# class Child(Parent,Parent2):
#     def grdyo(self):
#         print("Multiple inharitance.")

# obj = Child()

# print(obj.grd())
# print(obj.grdch())
# print(obj.grdyo())

#multilevel inheritance

# class Gp:
#     name = "Raj k"
#     def grd(self):
#         return "Hello from gps."
    
# class P(Gp):
#     name = "rishi k"
#     def grr(self):
#         return "Hello from."
    
# class Child(P):
#     def gru(self):
#         return "Hey wassup du."
    
# obj = Child()

# print(obj.grd())
# print(obj.grr())
# print(obj.gru())

# Hierarchical inheritance

# class Parents:
#     name = "lingesan"
#     def gnd(self):
#         return "YO yo........"
    
# class Child1(Parents):
#     def g(self):
#         return "YO yo........"
    
# class Child2(Parents):
#     def rnd(self):
#         return "YO yo........"
    
# obj1 = Child1()
# obj2 = Child2()

# print(obj1.g())
# print(obj2.rnd())

# class Employee:
#     def __init__(self,name,salary,age):
#         self.name = name
#         self.salary = salary
#         self.age = age

#     def getInfo(self):
#         print(f"name : {self.name}, salary : {self.salary}, age : {self.age}")

# class Manager(Employee):
#     def __init__(self,name,salary,age,department):
#         super().__init__(name,salary,age)
#         self.department = department

#     def getInfo(self):
#         print(f"Name : {self.name}, salary : {self.salary}, Age : {self.age}, Depatment : {self.department}")

# emp = Employee("Rahul",4000000, 50)
# man = Manager("saand",70000000,100,"finance")

# emp.getInfo()
# man.getInfo()


#           file handling           #
#There are four steps of file handling
# 1st is "r" r means read
# 2nd is "w" w means write
# 3rd is "a" a means append
# 4th is "x" x means create
# 
#
#1st is read 

# file = open("FB.py","r")

# line = file.readline()
# lines = file.readlines()

# print(line)
# print(lines)

# for li in lines:
#     print(li)
#     file.close()


#2nd  is create

# file = open("demo.txt","x")
# print("Yoyr file is created :)")
# file.close()


#3rd is write

# file = open("demo.txt","w")
# file.write("")
# print("Your msg printed successfully :)")
# file.close()


#4th is append

# file = open("demo.txt","a")
# file.write("\n What ohhh heellll nahhh.")
# print("Your extra msg is printed :)")
# file.close()

#an extra for the knoowledge
#with statement

# with open("demo.txt","r") as file:
#     content = file.read()
#     print(content)


#           Exception handling          #
#there are 7 types of exception handling
#1st is "Type error"
#2nd is "Value error"
#3rd is "Name error"
#4th is "Index error"
#5th is "Key error"
#7th is "File not found error"


#Try...Except

# print("Hello")
# print("Hello")

# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Divsion by 0 is not valid.")

# print("Hello")
# print("Hello")


#Try..Except..Else

# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Can't divide by 0.")
# else:
#     print("Boobsss")


#Try..Except..Finally

# try:
#     print("Hello")
# except TypeError:
#     print("Your division value is invalid.")
# else:
#     print("No Exception")
# finally:
#     print("Boobies")


#Exception

# try:
#     print(10/0)

# except Exception:
#     print("Can't divide by 0.")
# else:
#     print("Boobsss")


#Raise and Assert key-word

# Age = int(input("Enter your age : "))

# if Age<=18:
#     raise ValueError("Invalid value.")


#Assert key-word

# num = int(input("Enter the number : "))

# assert num>=0,"Number must be positive."

# print("Valid number : ",num)


#Custom error

# Age = int(input("Enter your age : "))

# class MyError(Exception):
#     pass

# if Age <=18:
#     raise MyError("Age is not valid.")

# while True:

#     print("""
#         Enter 1 to Add a new entry.
#         Enter 2 to View all entries.
#         Enter 3 to Search for an entry.
#         Enter 4 to Delete all Entries.
#         Enter 0 to exit the program.""")
    
#     Choice = int(input("Enter your choice : "))

#     if Choice == 1:
#         pass

#     elif Choice == 2:
#         pass

#     elif Choice == 3:
#         pass

#     elif Choice == 4:
#         pass

#     elif Choice == 0:
#         print("Thanx for visiting our programme :)")
#         break

#     else:
#         print("Your entered choice is invalid.")

# -----------------Modules-----------------------
#There are 3 types of midules
#1st is Built in modules
#2nd is udf modules
#3rd is third party(external) modules

#1st bult in modules

# import datetime

# now = datetime.datetime.now()
# year = now.year

# print(now)
# print(year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# Custom_Date = f"{now.day}/{now.hour}/{now.minute}/{now.second}"

# print(Custom_Date)

# C_D = datetime.datetime(2025,11,17,17,20)

# print(C_D)
# print(type(C_D))
# print(C_D.month)

# print(C_D.date())
# print(now.time())

#2nd method of custom date

#1)strf time
#2)strp time

#1) strf time

# now = datetime.datetime.now()

# print(now)

# custom = datetime.datetime.strftime(now,"%d/%m/%Y")

# print(custom)

# #2)strp time

# now = datetime.datetime.now()

# print(now)

# date_rev = datetime.datetime.strftime(custom,"%d/%m/%Y")

# print(date_rev)
# print(type(date_rev))

#timedelta

# from datetime import timedelta,datetime

# now = datetime.now()

# print(now - timedelta(days=10))

#Time module

# import time

# print("Hey")

# time.sleep(2)

# print("GTH")

# for i in range(1,11):
#     print(i)
#     time.sleep(1)


#Math modules

# import math

# print(math.sqrt(238))
# print(math.pow(9,3))
# print(math.fabs(-155448858))
# print(math.floor(40.36))
# print(math.ceil(40.36))
# print(math.trunc(24.555))
# print(math.factorial(24))
# print(math.log(20))
# print(math.pi)
# print(math.e)
# print(math.tau)
# print(math.inf)
# print(-math.inf)
# print(math.nan)



# def Dir_():
#     Mod_Name = input("Enter module name : ")

#     try:
#         Mod_ = __import__(Mod_Name)

#         print("All module Attributes in {Mod_name} module.")
#         print(dir(Mod_))
#     except:
#         print("Your entered module name is Invalid.")

# Dir_()

import seaborn as sns 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


class Visualizer:

    def __init__(self):

        self.name = None
        self.data = None

    def Load_data(self):

        try:
            self.data = sns.load_dataset("titanic")
            print("Data loaded Successfully.")
        except FileNotFoundError:
            print("File not found.")

    def F_5_rows(self):

        self.data = pd.DataFrame("titanic")
        F_5_r = self.data.head()
        print(F_5_r)

        


V_File  = Visualizer()

V_File.F_5_rows()