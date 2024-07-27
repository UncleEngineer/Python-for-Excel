from openpyxl import load_workbook
from songline import Sendline
def send_message_line(text):
    token = 'r1lmj6fhzyzAEy4JYAzjACQ6Qfn64RNsDUTzTUPD1EX'
    messenger = Sendline(token)
    messenger.sendtext(text)

sales_list = []

for i in range(1,11):
    name = 'sales-{}.xlsx'.format(i)
    excelfile = load_workbook(filename=name)
    sheet = excelfile.active

    sales = sheet['A2'].value
    sales_list.append(sales)

total = sum(sales_list)
text = 'ยอดขายวันนี้: {:,.2f} บาท'.format(total)
send_message_line(text)

# print(sales_list)
# print(sum(sales_list))