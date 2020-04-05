import pandas
# from tkinter import *
# from tkinter import ttk


"""
Set up the code to have different data display based on whichever planet is selected

"""
#=============Getting solar system data================#

df = pandas.read_csv("solar_system.csv" )
df.set_index("name" , inplace=True)
df.head()
# print(df)
state = True
def select_planet(planet):
    state = df.loc[planet]
    return state

select_planet("Sun")



