from tkinter import *

def copy():
    source_path = 'r' + "'" + srcpath.get() + "'"
    target_path = 'r' + "'" + trgtpath.get() + "'"
    file_name = "'" + fn.get() + "'"
    file_type = "'" + ft.get() + "'"
    if (len(source_path) == 0 or len(target_path) == 0):
        print("At least one path is missing.")
    else:
        print(f"{source_path}")
        print(f"{target_path}")
        print(f"{file_name}")
        print(f"{file_type}")

window = Tk()
window.geometry('450x200')
window.title('Copying tool')

label1 = Label(window, text="Source path:", justify=CENTER)
label1.pack(side='top')
source_path = StringVar()
srcpath = Entry(window, width=50, textvariable=source_path, justify=CENTER)
srcpath.pack(side='top')

label2 = Label(window, text="Target path:", justify=CENTER)
label2.pack(side='top')
target_path = StringVar()
trgtpath = Entry(window, width=50, textvariable=target_path, justify=CENTER)
trgtpath.pack(side='top')

label3 = Label(window, text="Files name:", justify=CENTER)
label3.pack(side='top')
target_path = StringVar()
fn = Entry(window, width=50, textvariable=target_path, justify=CENTER)
fn.pack(side='top')

label4 = Label(window, text="Files type:", justify=CENTER)
label4.pack(side='top')
target_path = StringVar()
ft = Entry(window, width=50, textvariable=target_path, justify=CENTER)
ft.pack(side='top')

genBut = Button(window, text='Copy', command=copy)
genBut.pack(side='bottom')

mainloop()