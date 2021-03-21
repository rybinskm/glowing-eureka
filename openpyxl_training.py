import openpyxl

# wb = doors_export

wb = openpyxl.load_workbook(r'C:\folder1\doors_export.xlsx')
sheet = wb['Arkusz1']
for i in range(0, 2):
    cell_pointer = f'A{i}'
    cell = sheet[f'A{i}'][0].value
    print(f"{cell_pointer}")
    print(f"{cell}")
