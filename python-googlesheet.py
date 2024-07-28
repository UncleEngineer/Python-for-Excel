# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread

import gspread
from google.oauth2.service_account import Credentials

sc = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file('credentials.json',scopes=sc)
client = gspread.authorize(creds)

sheet_id = '1e9Fg8uQ_tZSv9oEI0HOXL39FUQodRoFERoNC179DK50'

sheet = client.open_by_key(sheet_id)

worksheet = sheet.get_worksheet(0)

result = worksheet.acell('B5').value
result2 = worksheet.cell(1,1).value
# print(result)
# print(result2)


values_list = worksheet.row_values(1)

print(values_list)

column = worksheet.col_values(1)
print(column)
count = len(column)

# worksheet.format('A1:B1', {'textFormat': {'bold': True}})

# worksheet.update_cell(1,1,'สวัสดีจ้าามาจาก Python')
# worksheet.update_acell('B1','สวัสดีจ้าาา Python V2')

