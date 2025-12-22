import datetime
import time

def C_datetime():

    Now = datetime.datetime.now()
    print(Now)

def Difr_btwn_tim_dt(Date_1,Date_2):
    
    format = "%d/%m/%Y"
    Date_1_ = datetime.datetime.strptime(Date_1,format).date()
    Date_2_ = datetime.datetime.strptime(Date_2,format).date()
    diffrence = abs(Date_2_ - Date_1_)

    print(f"\n The difference between dates you given is : {diffrence} days")

def format_into_cstm():
    
    Now = datetime.datetime.now()
    print(Now)

    cstm_1 = f"{Now.day}/{Now.month}/{Now.year}"
    cstm_2 = f"{Now.month}/{Now.day}/{Now.year}"

    print("Enter 1 to print DD/MM/YYYY format.")
    print("Enter 2 to print MM/DD/YYYY format.")
    print("Enter 0 to exit programme.")
 
    while True:
        

        cstm_dt = int(input("Eneter your choice : "))

        if cstm_dt == 1:
            print(cstm_1)

        elif cstm_dt == 2:
            print(cstm_2)
        elif cstm_dt == 0:
            print("Go back to DateTime and Time function.")
            break
        else:
            print("Your entred number is invalid :(")

def stop_watch():

    print("Enter your stop watch time Clockwise or Anti-Clockwise.")
    print("Enter 1 to stop-watch in Clockwise.")
    print("Enter 2 to stop-watch in Anti-Clockwise.")

    ch = int(input("Enter your choice here : "))

    if ch == 1:
    
        Stp_watch = int(input("Enter the Time you want to start : "))
        Stp_watch_2 = int(input("Enter the Time you want to end : "))
        Stp_watch_3 = int(input("Enter the duration of update in (seconds) : "))

        for i in range(Stp_watch,Stp_watch_2+1,):
            print(i)
            time.sleep(Stp_watch_3)

    elif ch == 2:

        Stp_watch = int(input("Enter the Time you want to start : "))
        Stp_watch_2 = int(input("Enter the Time you want to end : "))
        Stp_watch_3 = int(input("Enter the duration of update in (seconds) : "))

        for i in range(Stp_watch,Stp_watch_2-1,-1):
            print(i)
            time.sleep(Stp_watch_3)

    else:
        print("Your entered choice is Invalid.")

        