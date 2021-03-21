import pathlib
import os, stat
import shutil
from datetime import datetime

# def copy(source_path, target_path, ext = '*', pat = ''):

### INPUT PARAMETERS ###
source_path = (r'C:\folder1')
target_path = (r'F:\folder2')
file_name = ('w400')
file_type = ('*')

date = datetime.now()
log = date.strftime("%d-%m-%Y_%H%M%S")
# log = 'Logfile'

files_list = []
ext = (f'*.{file_type}')

### getting amount of files to copy
for file in pathlib.Path(source_path).glob(f'{ext}'):
    if file_name:
        if file_name in str(file):
            files_list.append(file)
    else:
        files_list.append(file)
files_amount = len(files_list)
file_order = 0

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
    for file in files_list:
        if file_name:
            if file_name in str(file):
                f = str(file).split('\\')[-1]
                try:
                    shutil.copy(file, target_path)
                    file_order += 1
                    print(f'"{f}" copied. [{file_order}/{files_amount}]')
                    log_file.write(f'"{f}" was copied. [{file_order}/{files_amount}]\n')
                except PermissionError:
                    file_2 = (f'{source_path}\{f}')
                    os.chmod(file_2, stat.S_IWRITE)
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

else:
    if file_type:
        if file_name:
            print(f'#1 There is no file with name "{file_name}" for extension "{file_type}".')
        else:
            print(f'#2 There is no file with extension "{file_type}".')
    else:
        print(f'Verify extension of the file (type "*" for all files).')
