import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


print("`````Welcome to Our New Project Visulizer`````:)")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")

class Visualizer:


    def __init__(self):
        self.name = None
        self.df = None
        self.plots = False
        self.figs = None

    """Load Data Functions."""

    def Load_data(self):

        self.name = input("Enter the DataSet file name you want to Load(Only CSV_file) : ")
        try:
            self.df = sns.load_dataset(self.name)
            print("Data loaded Successfully.")
            return self.df
            
        except FileNotFoundError:
            print("Your entered file name is Invalid.")

    """Explore Data Functions."""

    def F_5_rows(self):
        
        F_5_r = self.df.head()
        print(F_5_r)

    def L_5_rows(self):
        
        L_5_r = self.df.tail()
        print(L_5_r)

    def D_Types(self):
        
        D_Types = self.df.dtypes
        print(D_Types)

    def Basic_Info(self):
        
        Basic_Inf = self.df.info()
        print(Basic_Inf)

    """DataFrame operations"""

    def Select_Cols(self):

        Cols = input("Enter the column name which you want to show : ")

        if Cols in self.df.columns:

            print(self.df[Cols])
        else:

            print("Your entered column name is not in DataFrame.")

    def Sample_Vals(self):

        Samp = self.df.sample(10)
        print(Samp)

    def Sort_Vals(self):

        Cols = input("Enter the column name which you want to sort : ")

        if Cols in self.df.columns:

            print(self.df.sort_values(by = Cols, ascending = True))

        else:

            print("Your entered column name is not in DataFrame.")        


    """Handle Missing Data"""

    def Rows_M_Vals(self):

        Missing_R_Vals = self.df.isna().sum()
        print(Missing_R_Vals)

    def Fill_M_vals(self):

        Miss_V_C_name = input("Enter the column name you want to fill : ")
        
        if Miss_V_C_name not in self.df.columns:
            print(f"{Miss_V_C_name} not Exist :(")

        if self.df[Miss_V_C_name].dtype :
            self.df[Miss_V_C_name].fillna(self.df[Miss_V_C_name].mean(), inplace = True)
            print("Missing values are successfully filled with mean.")
        else:
            print("Mean can be fill on numeric values not in objects.")

    def Drop_R_M_Vals(self):

        self.df.dropna(inplace = True)
        print("Rows missing values are Droped Successfully.")

    def R_Miss_Vals(self):
        col = input("Enter column name : ")

        if col not in self.df.columns:
            print("Column does not exist.")
            return

        value = input("Enter value to replace missing data with : ")

        if pd.api.types.is_numeric_dtype(self.df[col]):
            value = float(value)

        self.df[col].fillna(value, inplace=True)
        print("Missing values replaced successfully.")

    """Describe DataSet Statistics."""

    def Describe_Data(self):

        if self.df is None:
            print("First load the DataSet for the run thiis Operation.")
        else:
            print(self.df.describe())

    """Data Visualization"""

    def Bar_Plot(self):
        x = input("Enter X-axis column name : ")
        y = input("Enter Y-axis column name : ")
        Title = input("Enter the Title for Bar-Chart : ")

        if x in self.df.columns and y in self.df.columns:
            
            data = self.df.groupby(x)[y].sum()
            self.figs = plt.figure(figsize = (10,6))
            plt.bar(data.index,data.values, color = ["pink","lightblue"], alpha = 0.5, label = y)
            plt.title(Title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend(loc = "best")
            plt.tight_layout()
            plt.show()

            self.plots = True

        else:
            print(f"{x} and {y} columns are not fouund in Data.")

    def Line_Plot(self):

        x = input("Enter X-axis column name : ")
        y = input("Enter Y-axis column name : ")
        Title = input("Enter the Title for Line-Chart : ")

        if x in self.df.columns and y in self.df.columns:

            data = self.df.groupby(x)[y].sum()
            self.figs = plt.figure(figsize = (10,10))
            plt.plot(data.index,data.values, color = "pink", marksize = 7, marker = "o", markerfacecolor = "lightblue", label = y)
            plt.title(Title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend(loc = "best")
            plt.tight_layout()
            plt.show()

            self.plots = True

        else:
            print(f"{x} and {y} columns are not found in your Data.")

    def Scatter_Plot(self):

        x = input("Enter X-axis column name : ")
        y = input("Enter y-axis column name : ")
        Title = input("Enter the Title for Scatter-Chart : ")

        if x in self.df.columns and y in self.df.columns:

            data = self.df.groupby(x)[y].sum()
            self.figs = plt.figure(figsize = (10,10))
            plt.scatter(data.index,data.values, color = "pink", edgecolors = "lightblue" ,s = 100, label = y)
            plt.title(Title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend(loc = "best")
            plt.tight_layout()
            plt.show()

            self.plots = True

        else:
            print(f"{x} and {y} columns are not found in your Data.")

    def Pie_Plot(self):

        Col_Name = input("Enter Y-axis column name : ")
        Title = input("Enter the Title for Pie-Chart : ")
        counts = self.df[Col_Name].value_counts()

        if Col_Name in self.df.columns:
            
            self.figs = plt.figure(figsize = (10,10))
            plt.pie(
                counts,
                labels = counts.index, 
                startangle = 90,
                autopct = "%.2f%%",
                colors = ["pink","lightblue","purple"],
                shadow = True,
                label = Col_Name
                )
            plt.title(Title)
            plt.legend(Title = Col_Name,loc = "best")
            plt.tight_layout()
            plt.show()

            self.plots = True

        else:
            print(f"{Col_Name} columns are not found in your Data.")

    """Save the Data Visualization"""

    def Save_Plot(self):

       if self.figs is None:
           print("You didn't create Chart yet.")
           print("So,Please create a any chart which are given in 6th choice.")
           return

       try:
            
            F_Name = input("Enter file name (eg.Chart.png) : ")
            self.figs.savefig(F_Name)
            plt.close()
            self.figs = None
            print("Your Chart is successfully saved.")

       except Exception as  Mistakeinchart:
           
            print("Some mistakes in your chart.")
            print(Mistakeinchart)



V_File  = Visualizer()

while True:

    print()
    print("Enter 1 to Load Dataset.")
    print("Enter 2 to Explore Data.")
    print("Enter 3 to Perform DataFrame Operations.")
    print("Enter 4 to Handle Missing Data.")
    print("Enter 5 to Generate Descriptive Statistics.")
    print("Enter 6 to Data Visualization.")
    print("Enter 7 to Save Visualiztion.")
    print("Enter 0 to Exit The Programme.")
    print("~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|")

    Choice = int(input("Enter your Choice here : "))

    if Choice == 1:

        V_File.Load_data()

    elif Choice == 2:

        while True:
            print()
            print("Enter 1 to Display First 5 Rows.")
            print("Enter 2 to Display Last 5 Rows.")
            print("Enter 3 to Display Column Names.")
            print("Enter 4 to Display Data-types.")
            print("Enter 5 to Display Basic Information.")
            print("Enter 0 to Go-Back to Main-Menu.")
            print(":-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")

            choice = int(input("Enter your choice here : "))

            if choice == 1:

                print()
                V_File.F_5_rows()

            elif choice == 2:

                print()
                V_File.L_5_rows()

            elif choice == 3:
                pass

            elif choice == 4:

                print()
                V_File.D_Types()
                
            elif choice == 5:

                print()
                V_File.Basic_Info()
                
            elif choice == 0:

                print()
                print("Now you're Going-Back to Main-Menu.")
                break

            else:
                print("You entered Invalid choice of Explore Data Option :(")

    elif Choice == 3:

        while True:

            print()
            print("Enter 1 to Show Columns.")
            print("Enter 2 to Show Sample values of DataFrame.")
            print("Enter 3 to Sort values of DataFrame.")
            print("Enter 0 to Go-Back to Main-Menu.")

            choice = int(input("Enter your choice here : "))

            if choice == 1:

                print()
                V_File.Select_Cols()

            elif choice == 2:

                print()
                V_File.Sample_Vals()

            elif choice == 3:

                print()
                V_File.Sort_Vals()

            elif choice == 0:

                print("You're Going-Back to Main-Menu.")
                break

            else:

                print("You entered Invalid choice of DataFrame Operations.")

    elif Choice == 4:

        while True:
            print()
            print("Enter 1 to Display rows with missing values.")
            print("Enter 2 to Fill missing values with mean.")
            print("Enter 3 to Drop rows with missing values.")
            print("Enter 4 to Replace missing values with a specific values.")
            print("Enter 0 to Go-Back to Main-Menu.")

            choice = int(input("Enter your choice here : "))

            if choice == 1:

                print()
                V_File.Rows_M_Vals()

            elif choice == 2:

                print()
                V_File.Fill_M_vals()

            elif choice == 3:

                print()
                V_File.Drop_R_M_Vals()

            elif choice == 4:
                pass
            elif choice == 0:

                print()
                print("Now you're Going-Back to Main-Menu.")
                break
            else:
                print("You entered Invalid choice of Handle Missing Data Option :(")

    elif Choice == 5:

        print()
        V_File.Describe_Data()

    elif Choice == 6:

        print()
        print("Enter 1 to Bar plot.")
        print("Enter 2 to Line plot.")
        print("Enter 3 to Scatter plot.")
        print("Enter 4 to Pie chart.")
        print("Enter 0 to Go-Back to Main-Menu.")

        choice = int(input("Enter your choice here : "))

        if choice == 1:
            
            print()
            V_File.Bar_Plot()

        elif choice == 2:

            print()
            V_File.Line_Plot()

        elif choice == 3:

            print()
            V_File.Scatter_Plot()
            
        elif choice == 4:

            print()
            V_File.Pie_Plot()

        elif choice == 0:

            print()
            print("Now you're Going-Back to Main-Menu.")
            break
            
        else:
            print("You entered Invalid choice of Data Visualization Option :(")

    elif Choice == 7:

        print()
        V_File.Save_Plot()

    elif Choice == 0:
        print()
        print("Thanks for visiting Our Programme Visualizer :)")
        break

    else:
        print("You're entered Invalid Choice :( ")