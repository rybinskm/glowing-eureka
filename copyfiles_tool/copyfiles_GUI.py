# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import pathlib
import shutil
from tkinter import *
from datetime import datetime

def copy():
    source_path = srcpath.get()
    target_path = trgtpath.get()
    logging = varLog.get()

    if len(fn.get()) == 0:
        file_name = ('')
    else:
        file_name = fn.get()

    if len(ft.get()) == 0:
        file_type = ('*')
    else:
        file_type = ft.get()

    ### creating log
    if logging == 1:
        print(f'Logging enabled.')
        date = datetime.now()
        log = date.strftime("%d-%m-%Y_%H%M%S")
        log_file = open(f"{target_path}\Logfile_{log}.txt", "w+")

    files_list = []
    ext = (f'*.{file_type}')

    # getting amount of files to copy
    for file in pathlib.Path(source_path).glob(f'{ext}'):
        if file_name:
            if file_name in str(file):
                files_list.append(file)
        else:
            files_list.append(file)
    files_amount = len(files_list)
    file_order = 0

    if files_amount != 0:
        print(f'Source path: {source_path}')
        print(f'Target path: {target_path}')
        print(f'Files to copy: {files_amount}')
        print('Start of copying.')
        if logging == 1:
            log_file.write(f'Source path: {source_path}\n')
            log_file.write(f'Target path: {target_path}\n')
            log_file.write(f'Files to copy: {files_amount}\n')
            log_file.write('Start of copying.\n')
        for file in files_list:
            if file_name:
                if file_name in str(file):
                    f = str(file).split('\\')[-1]
                    shutil.copy(file, target_path)
                    file_order += 1
                    print(f'"{f}" copied. [{file_order}/{files_amount}]')
                    if logging == 1:
                        log_file.write(f'"{f}" was copied. [{file_order}/{files_amount}]\n')
            else:
                f = str(file).split('\\')[-1]
                shutil.copy(file, target_path)
                file_order += 1
                print(f'"{f}" copied. [{file_order}/{files_amount}]')
                if logging == 1:
                    log_file.write(f'"{f}" was copied. [{file_order}/{files_amount}]\n')
        print(f'{len(files_list)} files were copied.')
        if logging == 1:
            log_file.write(f'{len(files_list)} files were copied.')
            log_file.close()
    else:
        if file_name:
            print(f'There is no file with name "{file_name}" for extension "{file_type}".')
        else:
            print(f'There is no file with extension "{file_type}" (blank field is equal all files extensions).')

'''
        print(f'Logfile_{log} created.')
        log_file = open(f"{source_path}\Logfile_{log}.txt", "w")

        print(f'Source path: {source_path}')
        log_file.write(f'Source path: {source_path}\n')
        print(f'Target path: {target_path}')
        log_file.write(f'Target path: {target_path}\n')
        print(f'Files to copy: {files_amount}')
        log_file.write(f'Files to copy: {files_amount}\n')
        print('Start of copying.')
        log_file.write('Start of copying.\n')
        for file in files_list:
            if file_name:
                if file_name in str(file):
                    f = str(file).split('\\')[-1]
                    shutil.copy(file, target_path)
                    file_order += 1
                    print(f'"{f}" copied. [{file_order}/{files_amount}]')
                    log_file.write(f'"{f}" was copied. [{file_order}/{files_amount}]\n')
            else:
                f = str(file).split('\\')[-1]
                shutil.copy(file, target_path)
                file_order += 1
                print(f'"{f}" copied. [{file_order}/{files_amount}]')
                log_file.write(f'"{f}" was copied. [{file_order}/{files_amount}]\n')
        print(f'{len(files_list)} files was copied.')
        log_file.write(f'{len(files_list)} files were copied.')
        log_file.close()
        
        if file_name is True and file_type is True:
            print(f'There is no file with name "{file_name}" for extension "{file_type}".')
        elif file_name is True and file_type is False:
            print(f'There is no file with extension "{file_type}" (blank field is equal all files extensions).')
        elif file_name is False and file_type is False:
            print(f'There is no file with name "{file_name}".')
        elif file_name is False and file_type is True:
            print(f'There is no file with extension "{file_type}".')

'''

# GUI construction
window = Tk()
window.geometry('450x225')
window.title('Copying tool')

label1 = Label(window, text="Source path:", justify=CENTER)
label1.pack(side='top')
source_path = StringVar()
srcpath = Entry(window, width=70, textvariable=source_path, justify=CENTER)
srcpath.pack(side='top')

label2 = Label(window, text="Target path:", justify=CENTER)
label2.pack(side='top')
target_path = StringVar()
trgtpath = Entry(window, width=70, textvariable=target_path, justify=CENTER)
trgtpath.pack(side='top')

label3 = Label(window, text="Files name:", justify=CENTER)
label3.pack(side='top')
file_name = StringVar()
fn = Entry(window, width=20, textvariable=file_name, justify=CENTER)
fn.pack(side='top')

label4 = Label(window, text="Files type:", justify=CENTER)
label4.pack(side='top')
file_type = StringVar()
ft = Entry(window, width=20, textvariable=file_type, justify=CENTER)
ft.pack(side='top')

genBut = Button(window, text='Copy', command=copy)
genBut.pack(side='bottom')

varLog = IntVar()
chkLog = Checkbutton(window, text='External log file', var=varLog)
chkLog.pack(side='bottom')

source_path.set(r"C:\folder1")
target_path.set(r"F:\folder2")
file_type.set("jpg")
varLog.set(1)

mainloop()
