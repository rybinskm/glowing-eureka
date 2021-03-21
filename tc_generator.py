# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import xlrd

workbook = xlrd.open_workbook(r"C:\Users\Rybston\Desktop\TC\skr.xlsx")  # workbook pointer
worksheet = workbook.sheet_by_name('Arkusz1')  # sheet pointer

# for i in range(4):  # rows
# for j in range(3):  # columns
# print(worksheet.cell_value(i, j))

for i in range(4):  # excel rows value
    tc = (worksheet.cell_value(i, 0))  # data from excel
    head = (worksheet.cell_value(i, 1))  # data from excel
    desc = (worksheet.cell_value(i, 2))  # data from excel
    file_def = open(r"C:\Users\Rybston\Desktop\TC\TC_XX.txt", 'r')  # def as default file for generator
    file_new = open(rf"C:\Users\Rybston\Desktop\TC\TC_{tc}.txt", 'w+')  # new file with changed lines
    for j in range(100):  # maximum lines value
        line = file_def.readline()  # reading line by line from default file
        line = line.replace("{id}", f"{tc}")  # replace for 1st finding
        line = line.replace("{head}", f"{head}")  # replace for 2nd finding
        line = line.replace("{desc}", f"{desc}")  # replace for 3rd finding
        file_new.writelines(line)  # write line to new file
    file_new.close()  # close new file for next iteration
    file_def.close()  # close default file for next iteration


def tc_gen(val):
    for i in range(val):  # excel rows value
        head = f"HEAD #{i}"
        desc = f"DESCRIPTION #{i}"
        file_def = open(r"C:\Users\Rybston\Desktop\TC\TC_XX.txt", 'r')  # def as default file for generator
        file_new = open(rf"C:\Users\Rybston\Desktop\TC\TC_{i}.txt", 'w+')  # new file with changed lines
        for j in range(100):  # maximum lines value
            line = file_def.readline()  # reading line by line from default file
            line = line.replace("{id}", f"{i}")  # replace for 1st finding
            line = line.replace("{head}", f"{head}")  # replace for 2nd finding
            line = line.replace("{desc}", f"{desc}")  # replace for 3rd finding
            file_new.writelines(line)  # write line to new file
        file_new.close()  # close new file for next iteration
        file_def.close()  # close default file for next iteration
