from songline import Sendline


def sawatdee():
    print('สวัสดีจ้าาาา')
    print('สวัสดีจ้าาาา')
    print('สวัสดีจ้าาาา')
    print('สวัสดีจ้าาาา')
    print('สวัสดีจ้าาาา')

def hello(friend):
    print('เฮลโหล{}ฮาวอาร์ยู'.format(friend))

# sawatdee()
# hello('จอห์น')

def send_message_line(text):
    token = 'r1lmj6fhzyzAEy4JYAzjACQ6Qfn64RNsDUTzTUPD1EX'
    messenger = Sendline(token)
    messenger.sendtext(text)



# token = 'r1lmj6fhzyzAEy4JYAzjACQ6Qfn64RNsDUTzTUPD1EX' # ใครสร้างบ็อทตัวนี้ อยู่ในกลุ่มไหน? ชื่อบ็อทชื่อ?
# messenger = Sendline(token)
# messenger.sendtext('สวัสจ้าาาา ลุงกำลังจะส่งยอดให้')
# messenger.sticker(229,3,'กำลังรีบไปขายของจ้าาา')
# messenger.sendimage('https://i.pinimg.com/736x/5c/f8/0d/5cf80d9dfaf553f9d11ac3ccbdf02a33.jpg')