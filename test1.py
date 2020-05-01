import openpyxl
from pprint import pprint as pp

wb = openpyxl.load_workbook("/home/lokesh/Documents/Cable.xlsx")
#print(wb.sheetnames)
sheet = wb['Sheet1']

for row in range(1, sheet.max_row + 1):
    for col in range(1, sheet.max_column + 1):
        while col < sheet.max_column:
            print(sheet.cell(row, col).value, end=' ')
            break
        continue
    print()

