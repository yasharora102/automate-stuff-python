import os,sys
import openpyxl,sys

if len(sys.argv) > 1:
    path = sys.argv[1]
    if path.split('.')[1]=='xlsx':
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        data = sheet.rows
        txt_file = open("data.txt", "w+")

        for row in data:
            l = list(row)
            for i in range(len(l)):
                if i == len(l) - 1:
                    txt_file.write(str(l[i].value))
                else:
                    txt_file.write(str(l[i].value) + ',')
            txt_file.write('\n')
        txt_file.close()