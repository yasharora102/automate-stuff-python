import os,sys
import openpyxl,sys

from openpyxl import workbook

if len(sys.argv) > 1:
    path = sys.argv[1]
    row,column = 1,1
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    if path.split('.')[1]=='txt':
        file = open(path)
        read_stuff = file.readlines()
        for i in read_stuff:
            sheet.cell(row=row,column=column).value = i
            row+=1     
        row=1
        column+=1
        file.close()
    workbook.save('file.xlsx')

else:
    print('Error')
    print('Usage: python3 textotxl.py file_name')
    