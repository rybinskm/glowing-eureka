# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

from tkinter import *
from os.path import *
from random import *

def generate():
    korwinizmy = open('G:\PycharmProjects\korwinizmy.txt', 'a')
    list = []
    ch = chr(122)
    c = 0
    file = open(speech, 'r')
    for line in file:
        x = randint(0, 21)
        i = line.split(';')[x]
        list.append(i)
        for char in line:
            if char.lower() == ch:
                c += 1

    sentence = f"{list[0]} {list[1]} {list[2]} {list[3]} {list[4]} {list[5]}"
    korwinizmy.write(f'{sentence} \n')
    result.set(sentence)
    korwinizmy.close()

speech = relpath(r'G:\PycharmProjects\untitled\source\files\korwin.txt')
o = open(speech, 'r')

window = Tk()
window.geometry('1375x50')
window.title('Korwin speech generator')

result = StringVar()
res = Entry(window, width=225, textvariable=result, justify=CENTER)
res.pack(side='top')

genBut = Button(window, text='Generate', command=generate)
genBut.pack(side='bottom')

window.mainloop()
