from os.path import *
from tkinter import *
import tkinter.ttk as ttk

def show():
    o = open(acc_file, 'r')
    acc1 = choice.get()
    for line in o:
        acc2 = (line.split(';')[0])
        if acc1 == acc2:
            login = (line.split(';')[1])
            password = (line.split(';')[2])
            text1.delete(1.0, 50.0)
            text1.insert(1.0, login)
            text2.delete(1.0, 50.0)
            text2.insert(1.0, password)

acc_file = relpath(r'G:\PycharmProjects\untitled\source\files\accounts.txt')
o = open(acc_file, 'r')

top = Tk()
top.title("Accounts")
top.geometry('220x150')

labelTop = Label(text='Choose application: ')
labelTop.grid(column=0, row=0)
choice = ttk.Combobox(top, state='readonly', values=['Battle.net',
                                                     'CD-Action',
                                                     'Epic Games',
                                                     'GOG',
                                                     'Humble Bundle',
                                                     'Nintendo',
                                                     'Origin',
                                                     'Playstation Network',
                                                     'Steam',
                                                     'Uplay'])

choice.grid(column=0, row=1)
choice.current(0)
label1 = Label(text='Login: ')
text1 = Text(height=1, width=26)
label2 = Label(text='Password: ')
text2 = Text(height=1, width=26)

label1.grid(column=0, row=2)
text1.grid(column=0, row=3)
label2.grid(column=0, row=4)
text2.grid(column=0, row=5)

button1 = Button(text='Show', command=show)
button1.grid(column=0, row=6)

top.mainloop()
