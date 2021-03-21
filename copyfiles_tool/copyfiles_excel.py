# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import pathlib
import shutil
import openpyxl
from datetime import datetime

# def copy(source_path, target_path, ext = '*', pat = ''):

source_path = (r'C:\folder1')
target_path = (r'F:\folder2')
file_name = ()
file_type = ('jpg')

date = datetime.now()
#log = date.strftime("%d-%m-%Y_%H%M%S")
log = 'Logfile'

doors_export = openpyxl.load_workbook(r'C:\folder1\doors_export.xlsx')
files_list = []
ext = (f'*.{file_type}')

### getting files amount to copy
for file in pathlib.Path(source_path).glob(f'{ext}'):
    if file_name:
        if file_name in str(file):
            files_list.append(file)
    else:
        files_list.append(file)
files_amount = len(files_list)
n = 0

if files_amount != 0:
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
    for file in pathlib.Path(source_path).glob(f'{ext}'):
        if file_name:
            if file_name in str(file):
                f = str(file).split('\\')[-1]
                shutil.copy(file, target_path)
                n += 1
                print(f'"{f}" copied. [{n}/{files_amount}]')
                log_file.write(f'"{f}" was copied. [{n}/{files_amount}]\n')
        else:
            f = str(file).split('\\')[-1]
            shutil.copy(file, target_path)
            n += 1
            print(f'"{f}" copied. [{n}/{files_amount}]')
            log_file.write(f'"{f}" was copied. [{n}/{files_amount}]\n')
    print(f'{len(files_list)} files was copied.')
    log_file.write(f'{len(files_list)} files were copied.')
    log_file.close()
else:
    print(f'There is no file with name "{file_name}" for extension "{file_type}".')
