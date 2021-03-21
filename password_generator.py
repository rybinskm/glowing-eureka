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
def gen():
    length = int(varLen.get())
    letters = varLet.get()
    numbers = varNum.get()
    signs = varSig.get()
    st = ''
    try:
        for i in range(length):
            rd = (randint(1, 4))
            if rd == 1:
                z = chr(randint(97, 122))
            if rd == 2:
                if letters == 1:
                    z = chr(randint(65, 90))
                else:
                    z = chr(randint(97, 122))
            elif rd == 3:
                if numbers == 1:
                    z = chr(randint(48, 57))
                else:
                    z = chr(randint(97, 122))
            elif rd == 4:
                if signs == 1:
                    z = chr(randint(35, 47))
                else:
                    z = chr(randint(97, 122))
            st = st + z
    except:
        i <= 0
    result.set(st)

window = Tk()
window.geometry('550x100')
window.title('Password Generator')

lenlabel = Label(None, text='Length:')
lenlabel.grid(column=0, row=0)

varLen = IntVar()
len = Entry(window, width=5, textvariable=varLen)
len.grid(column=1, row=0)
varLen.set('8')
s = int(varLen.get())

varLet = IntVar()
chkLet = Checkbutton(window, text='Capital letters', var=varLet)
chkLet.grid(column=0, row=1)
a = varLet.get()

varNum = IntVar()
chkNum = Checkbutton(window, text='Numbers', var=varNum)
chkNum.grid(column=1, row=1)
b = varNum.get()

varSig = IntVar()
chkSig = Checkbutton(window, text='Special signs', var=varSig)
chkSig.grid(column=2, row=1)
c = varSig.get()

genBut = Button(window, text='Generate', command=gen)
genBut.grid(column=1, row=2)

result = StringVar()
res = Entry(window, width=50, textvariable=result, justify=CENTER)
res.grid(column=1, row=4)

mainloop()