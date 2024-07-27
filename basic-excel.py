from openpyxl import Workbook

excelfile = Workbook()
sheet = excelfile.active

sheet['A1'] = 'ยอดขาย'
sheet['A2'] = 5000

sheet['B1'] = 'ค่าคอมฯ'
sheet['B2'] = '=A2*0.1'


excelfile.save('sales.xlsx')
