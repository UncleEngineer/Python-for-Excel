# read-excel-data.py
from openpyxl import load_workbook

data_excel = load_workbook(filename='data-invoice.xlsx')
sheet_data = data_excel.active

count = len(sheet_data['A'])
print(count)

rows = []

for i in range(2,count+1):
    datalist = []
    for d in sheet_data[i]:
        datalist.append(d.value)
        #print(datalist)
    rows.append(datalist)
        #print('-----')

print(len(rows))

# loop เพื่อสร้างกลุ่ม IV 
rows_dict = {}
for r in rows:
    if r[4] not in rows_dict:
        rows_dict[r[4]] = []

# print(rows_dict)

# loop เพื่อแยก IV แต่ละ transaction
for r in rows:
    rows_dict[r[4]].append(r)

for r in rows_dict['IV-6307021']:
    print(r)




# datalist = [ d.value for d in sheet_data[2]]


