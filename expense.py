import gspread
from google.oauth2.service_account import Credentials

sc = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file('credentials.json',scopes=sc)
client = gspread.authorize(creds)

sheet_id = '1e9Fg8uQ_tZSv9oEI0HOXL39FUQodRoFERoNC179DK50'

sheet = client.open_by_key(sheet_id)

worksheet = sheet.get_worksheet(0)

#########################################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมบันทึกค่าใช้จ่ายลง Google Sheeet')

FONT1 = ('Angsana New',20)

L = ttk.Label(GUI,text='รายการ',font=FONT1)
L.pack()
v_title = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_title,font=FONT1,width=50)
E1.pack()
# ---------------------
L = ttk.Label(GUI,text='ค่าใช้จ่าย (บาท)',font=FONT1)
L.pack()
v_price = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1,width=30)
E2.pack()

def Save():
    column = worksheet.col_values(1) # column A
    count = len(column) + 1 # count A
    title = v_title.get()
    price = v_price.get()
    worksheet.update_cell(count,1,title)
    worksheet.update_cell(count,2,price)
    #clear 
    v_title.set('')
    v_price.set('')
    Update_data()

B1 = ttk.Button(GUI,text='บันทึก',command=Save)
B1.pack(ipadx=30,ipady=20,pady=20)

v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result,font=FONT1)
result.pack()

def Update_data():
    values_list = worksheet.col_values(2)
    del values_list[0] #clear column
    
    digit_list = [ float(v) for v in values_list]
    total = sum(digit_list)
    text = 'ยอดค่าใช้จ่ายทั้งหมด: {} บาท'.format(total)
    v_result.set(text)

Update_data()
GUI.mainloop()