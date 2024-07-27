from openpyxl import load_workbook
import os

files = os.listdir()
# print(files)
filtered_files = []

for f in files:
    if f.split('.')[-1] == 'xlsx' and len(f.split('.')[0].split('-')) >= 2:
        filtered_files.append(f)

print(filtered_files)

## loop ยอดจากไฟล์ทั้งหมด

sales_list = []

for ft in filtered_files:
    excelfile = load_workbook(filename=ft)
    sheet = excelfile.active 
    sales = sheet['A2'].value
    sales_list.append(sales)

summary = sum(sales_list)
print('ยอดขายทั้งหมดวันนี้: {:,.2f} บาท'.format(summary))
print(f'ยอดขายทั้งหมดวันนี้: {summary:,.2f} บาท')



