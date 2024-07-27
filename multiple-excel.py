from openpyxl import Workbook
import random

# บรรทัดต่อไปคือ for loop # คือการคอมเมนท์โค้ด
for i in range(1,21):

    number = random.randint(5000,10000)
    excelfile = Workbook()
    sheet = excelfile.active

    sheet['A1'] = 'ยอดขาย'
    sheet['A2'] = number

    sheet['B1'] = 'ค่าคอมฯ'
    sheet['B2'] = '=A2*0.1'


    excelfile.save('sales-{}.xlsx'.format(i))

