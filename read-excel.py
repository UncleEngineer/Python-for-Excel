from openpyxl import load_workbook

sales_list = []

for i in range(1,11):
    name = 'sales-{}.xlsx'.format(i)
    excelfile = load_workbook(filename=name)
    sheet = excelfile.active

    sales = sheet['A2'].value
    sales_list.append(sales)

print(sales_list)
print(sum(sales_list))