# excel-template.py

from openpyxl import load_workbook

data_excel = load_workbook(filename='data-invoice.xlsx')
template_excel = load_workbook(filename='template-iv.xlsx')

sheet_data = data_excel.active # data_excel['ใบกำกับภาษี']
sheet_template = template_excel.active # template_excel[0]

print(sheet_data['E2'].value)

number = sheet_data['E2'].value
# แก้ไข cell ใน template
sheet_template['S14'] = number
template_excel.save('result-excel.xlsx')

