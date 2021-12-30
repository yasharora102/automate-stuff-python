
import openpyxl
import os

for file in os.listdir('.'):
    if file.endswith('.xlsx'):

        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        data = sheet.rows
        file_csv = open("data.csv", "w+")
        for row in data:
            l = list(row)
            for i in range(len(l)):
                if i == len(l) - 1:
                    file_csv.write(str(l[i].value))
                else:
                    file_csv.write(str(l[i].value) + ',')
            file_csv.write('\n')
        file_csv.close()