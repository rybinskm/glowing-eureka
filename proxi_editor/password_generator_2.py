from random import *
from tkinter import *

'''
length:
    Int value for length of password.
letters:
    0: Script doesn't include capital letters.
    1: Script includes capital letters.
numbers:
    0: Script doesn't include integers.
    1: Script includes integers.
signs:
    0: Script doesn't include special signs.
    1: Script includes special signs.
'''
def gen():  # function for generating password for definied parameters
    length = int(varLen.get())  # assign value of varLen(Scale widget) to 'length' parameter
    letters = varLet.get()  # assign value of varLet(Checkbox #1 widget) to 'letters' parameter
    numbers = varNum.get()  # assign value of varNum variable(Checkbox #2 widget) to 'numbers' parameter
    signs = varSig.get()  # assign value of varSig variable(Checkbox #3 widget) to 'signs' parameter
    st = ''  # create empty variable for generated password
    for i in range(length):  # loop equals 'length' parameter
        rd = (randint(1, 4))  # draw one of four possible values
        if rd == 1:  # value of 'rd' for lower case
            z = chr(randint(97, 122))  # ASCII values for all lower cases
        if rd == 2:  # value of 'rd' for capiral letters
            if letters == 1:  # if 'letters' from varLet(Checkbox #1 widget) is equal 1
                z = chr(randint(65, 90))  # ASCII value for all capital letters
            else:  # if 'letters' from varLet(Checkbox #1 widget) is equal 0
                z = chr(randint(97, 122))
        elif rd == 3:  # value of 'rd' for numbers
            if numbers == 1:
                z = chr(randint(48, 57))
            else:
                z = chr(randint(97, 122))
        elif rd == 4:  # value of 'rd' for signs
            if signs == 1:
                z = chr(randint(35, 47))
            else:
                z = chr(randint(97, 122))
        st = st + z
    result.set(st)

window = Tk()
window.geometry('305x190')
window.title('Password Generator')
varLen = Scale(label='Length:', orient=HORIZONTAL, from_=1, to=48, length=200)
varLen.grid(column=0, row=0)

varLet = IntVar()
chkLet = Checkbutton(window, text='Capital letters', var=varLet)
chkLet.grid(column=0, row=1)

varNum = IntVar()
chkNum = Checkbutton(window, text='Numbers', var=varNum)
chkNum.grid(column=0, row=2)

varSig = IntVar()
chkSig = Checkbutton(window, text='Special signs', var=varSig)
chkSig.grid(column=0, row=3)

genBut = Button(window, text='Generate', command=gen)
genBut.grid(column=0, row=4)

result = StringVar()
res = Entry(window, width=50, textvariable=result, justify=CENTER)
res.grid(column=0, row=5)

mainloop()