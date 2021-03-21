import xlrd
import os

workbook = xlrd.open_workbook(r'C:\Users\Rybston\Downloads\sheet.xlsx')
worksheet = workbook.sheet_by_name('Arkusz1')

# for i in range(10):
#     for j in range(10):
#         for worksheet.cell_type(i, j):
#             if 'monitor' in worksheet.cell(i, j).value:
#                 print(worksheet.cell(i, j).value)

for i in range(16):
    for j in range(3):
        cell = worksheet.cell_value(i, j)
        if 'Screen:' in cell:
            print(f"Screen: {int(worksheet.cell_value(i, j+1))}")
        else:
            print(f'Not detected, row {i} column {j}')

print(worksheet.cell_value(5, 2))

# for i in range(5):
#     # for j in range(5):
#     j = 1
#     cell_val = worksheet.cell(i, j).value
#     cell_type = worksheet.cell_type(i, j)
#     if cell_type != xlrd.XL_CELL_EMPTY
#         print(cell_val)
#     else:
#         print('x')
        # if 'Screen:' in worksheet.cell_value(i, j):
        #     print(f'{i} {j}')
    # print(cell_val)
