from electronic_source import *
from tkinter import *

def add_res(value):
    res_array.append(value)
    return res_array

def curr(entrance_voltage, res_):
    sum = sum(res_array)
    i = entrance_voltage/res_array
    return i

window = Tk()

label1 = Label(text='R: ')
text1 = Text(height=1, width=26)
label2 = Label(text='U: ')
text2 = Text(height=1, width=26)

label1.grid(column=0, row=2)
text1.grid(column=0, row=3)
label2.grid(column=0, row=4)
text2.grid(column=0, row=5)

button1 = Button(text='Add resistance', command=add_res)
button1.grid(column=0, row=6)

button1 = Button(text='Calculate', command=curr)
button1.grid(column=0, row=7)

print(f"Entrance voltage: {u} [V]")
print(f"Resistance: {r} [ohm]")
i = u/r
print(f"Current: {i} [A]")

window.mainloop()
