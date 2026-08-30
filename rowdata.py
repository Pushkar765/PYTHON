import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# df = pd.read_csv("expenses.csv")

class ExpenseTracker:
    def __init__(self, dataframe):
        self.expenses = dataframe

    def R_Data(self):

        self.expenses = pd.read_csv("expenses.csv")
        print(self.expenses)
        print("DataSet Read Successfully 😊")
        return 

    def add_expense(self, date, amount, category, description):
        new_row = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        self.expenses = pd.concat(
            [self.expenses, pd.DataFrame([new_row])],
            ignore_index=True
        )
    def take_input():
        while True:
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format")

        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    break
            except ValueError:
                print("Invalid amount")

        category = input("Enter category: ")
        description = input("Enter description: ")

        return date, amount, category, description
    
    def analyze_expenses(df):
        total = np.sum(df["Amount"])
        average = np.mean(df["Amount"])
        category_total = df.groupby("Category")["Amount"].sum()

        print("Total Expense:", total)
        print("Average Expense:", average)
        print("Category-wise Expense:")
        print(category_total)

    def filter_by_category(df, category):
        return df[df["Category"] == category]
    
    def bar_chart(df):
        df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Expenses by Category")
        plt.show()

    def line_graph(df):
        df.groupby("Date")["Amount"].sum().plot()
        plt.title("Expense Trend")
        plt.show()

    def pie_chart(df):
        df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.show()

    def histogram(df):
        plt.hist(df["Amount"])
        plt.title("Expense Distribution")
        plt.show()




E_File = ExpenseTracker()

while True:

    print("Enter 1 to Read Expense DataSet.")
    print("Enter 2 to Input any Expense.")
    print("Enter 3 to Cleaning DataSet(🧹).")
    print("Enter 4 to Analysis & Matrics.")
    print("Enter 5 to Filter the DataSet.")
    print("Enter 6 to Visualize the DataSet(📈📉📊).")
    print("Enter 0 to Close the Programme.")

    Choice = int(input("Enter your Choice here : "))

    if Choice == 1:

        print()
        E_File.R_Data()

    elif Choice == 2:

        print()
        E_File.take_input()

    elif Choice == 3:

        print()
        E_File.analyze_expenses()

    elif Choice == 4:

        print()
        E_File.analyze_expenses()

    elif Choice == 5:

        print()
        E_File.filter_by_category()

    elif Choice == 6:

        print()
        E_File.bar_chart()
        E_File.line_graph()
        E_File.pie_chart()
        E_File.histogram()

    elif Choice == 0:
        print("Thanks for visiting My Project 👋")
        break

    else:
        print("You entered Invalid Choice 🥺")