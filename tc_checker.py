# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import pathlib
import xlrd

files_list = []

for py_file in pathlib.Path('G:\PycharmProjects').glob('*.py'):
    py = open(f'{py_file}', 'r')
    files_list.append(py_file)
    print(f"{py_file} opened.")
    for line in py:
        print(f'{line}')
    py.close()
print(f'{files_list}')

# workbook = xlrd.open_workbook(r"C:\Users\RYBINSKM\Desktop\check\cc_req.xlsx")  # workbook pointer
# worksheet = workbook.sheet_by_name('Sheet1')  # sheet pointer
#
# export_file = open(rf"C:\Users\RYBINSKM\Desktop\check\req_cov.txt", 'w+')
# checked_reqs = []
# for py_file in pathlib.Path('C:\FCA_332_S-CAM48\TESTUS\tests_implementation\test_cases\FCA_332\CameraCalibration\develop').glob('*.py'):
#     tc = open(rf"{py_file}", 'r')
#     print(f"{py_file}")
#     export_file.write(f"{py_file} \n")
#     for line in tc:  # lines in TC values
#         for j in range(1, 171):  # lines in excel
#             id_req = (worksheet.cell_value(j, 0))  # data from excel, second parameter is a column number
#             cal_type = (worksheet.cell_value(j, 3))
#             req_status = (worksheet.cell_value(j, 4))
#             if (id_req in line) and (id_req not in checked_reqs):
#                 print(f"{id_req}; {req_status}; {cal_type}")
#                 export_file.write(f"{id_req}; {req_status}; {cal_type} \n")
#                 checked_reqs.append(id_req)
#     tc.close()
# export_file.close()
