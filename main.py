from tkinter import *
from datetime import date

def calculator():
   result = str(entry.get())
   today = date.today()
   dob_data = result.split("/")
   date1 = int(dob_data[0])
   month = int(dob_data[1])
   year = int(dob_data[2])
   dob = date(year,month,date1)
   number_of_days = (today - dob).days
   age = number_of_days // 365
   label=Label(mats, text="Your age is " + str(age))
   label.pack()


mats = Tk()
mats.geometry("300x200")
mats.title("Age Calculator")
entry = Entry(width=10)
entry.pack()

button = Button(mats, text="Age", command=calculator,)
button.pack()
mats.mainloop()