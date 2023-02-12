from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys

def move_back():
    prof_window.destroy()

with open("username.txt", "r") as f:
    username = f.read()
user_entry = username

def update_profile():
    if  address.get() == '' or email.get() == '' or contact.get() == '' or password.get() == '' or payment_method.get() == '':
        messagebox.showinfo('Taxi Booking System', 'All feild must be filled.')
    else:
        sql= """UPDATE customers set address=%s, email=%s, phone_no=%s, password=%s, payment_method=%s WHERE username=%s"""
        values = (address.get(), email.get(), contact.get(), password.get(), payment_method.get(), user.get() )
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo('Taxi Booking System', 'Your record is updated')
        prof_window.destroy()
        import login

prof_window = Tk()
prof_window.geometry('900x650')
prof_window.title('Taxi booking system')
prof_window.resizable(False, False)

bg_img = ImageTk.PhotoImage(Image.open('img_file/Component 8.png'))
bg_lbl = Label(prof_window, image=bg_img)
bg_lbl.pack()

reg_frame = Frame(prof_window, width=350, height=600, bg='white', highlightbackground='black', highlightthickness=1)
reg_frame.place(x=300, y=20)

profile = ImageTk.PhotoImage(Image.open('img_file/Profile.png'))
lbl1 = Label(reg_frame, image=profile, bg='white')
lbl1.place(x=120, y=5)

#####################______________________________________________________________________

def on_enter(e):
    name=user.get()
    if name=='Type your username':
        user.delete(0, 'end')
    else:
        user.get()


def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Type your username')

username = Label(reg_frame, fg='black', bg='white', text='Username', font=('Helvetica', 11))
username.place(x=50, y=39)

sql = """SELECT username From customers WHERE username=%s"""
values = (user_entry, )
conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
if record!=None:
    print('Your id is', record)
cursor.close()
conn.close()

user = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
user.insert(0, *record)
user.config(state="disable")
user.place(x=70, y=76)

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=98)

user_img = ImageTk.PhotoImage(Image.open('img_file/user_icon_1.png'))
user_img_lbl = Label(reg_frame, image=user_img, bg='white')
user_img_lbl.place(x=50, y=76)

user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# #########################__________________________________________________________________________
def on_Enter(e):
    add=address.get()
    if add=='Type your address':
        address.delete(0, 'end')
    else:
        address.get()


def on_Leave(e):
    add=address.get()
    if add=='':
        address.insert(0, 'Type your address')

address_lbl = Label(reg_frame, fg='black', bg='white', text='Address', font=('Helvetica', 11))
address_lbl.place(x=50, y=112)

sql = """SELECT address From customers WHERE username=%s"""
values = (user_entry, )
conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
if record!=None:
    print('Your id is', record)
cursor.close()
conn.close()

address = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
address.place(x=70, y=150)
address.insert(0, *record)

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=174)

add_img = ImageTk.PhotoImage(Image.open('img_file/addimg.png'))
lbl_add = Label(reg_frame, image=add_img, bg='white')
lbl_add.place(x=50, y=150)

address.bind('<FocusIn>', on_Enter)
address.bind('<FocusOut>', on_Leave)
# #####################################___________________________________________________

def on_click(e):
    add=email.get()
    if add=='Example@gmail.com':
        email.delete(0, 'end')
    else:
        email.get()


def on_unclick(e):
    add=email.get()
    if add=='':
        email.insert(0, 'Example@gmail.com')

email_lbl = Label(reg_frame, fg='black', bg='white', text='Email', font=('Helvetica', 11))
email_lbl.place(x=50, y=193)

sql = """SELECT email From customers WHERE username=%s"""
values = (user_entry, )
try:
    conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                           database='tbs')
    cursor = conn.cursor()
    cursor.execute(sql, values)
    record = cursor.fetchone()
    if record!=None:
        print('Your id is', record)
    cursor.close()
    conn.close()
except:
    print("Error : ", sys.exc_info())

email = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
email.place(x=72, y=230)
email.insert(0, *record)

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=254)

mail_img = ImageTk.PhotoImage(Image.open('img_file/mailimg.png'))
lbl_mail = Label(reg_frame, image=mail_img, bg='white')
lbl_mail.place(x=50, y=230)

email.bind('<FocusIn>', on_click)
email.bind('<FocusOut>', on_unclick)
#
# ##########################################__________________________________________________________________________
#
def on_Click(e):
    add=contact.get()
    if add=='Phone no.':
        contact.delete(0, 'end')
    else:
        contact.get()

def on_Unclick(e):
    add=contact.get()
    if add=='':
        contact.insert(0, 'Phone no.')

phone_lbl = Label(reg_frame, fg='black', bg='white', text='Contact', font=('Helvetica', 11))
phone_lbl.place(x=50, y=275)

sql = """SELECT phone_no From customers WHERE username=%s"""
values = (user_entry, )
conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
if record!=None:
    print('Your id is', record)
cursor.close()
conn.close()

contact = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
contact.place(x=73, y=310)
contact.insert(0, *record)

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=332)

phone_img = ImageTk.PhotoImage(Image.open('img_file/phoneimg.png'))
lbl_phone = Label(reg_frame, image=phone_img, bg='white')
lbl_phone.place(x=50, y=310)

contact.bind('<FocusIn>', on_Click)
contact.bind('<FocusOut>', on_Unclick)

# #####################################################________________________________________________________________
show_icon = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
hide_icon = ImageTk.PhotoImage(Image.open('img_file/passwordEye1.png'))

def onClick(e):
    add=password.get()
    if add=='Type password':
        password.delete(0, 'end')

    else:
        password.get()


def onUnclick(e):
    add=password.get()
    if add=='':
        password.insert(0, 'Type password')

def show_hide_icon():
    if password['show'] == '*':
        security_btn1.config(image=show_icon)
        password.config(show='')

    else:
        security_btn1.config(image=hide_icon)
        password.config(show='*')

password_lbl = Label(reg_frame, fg='black', bg='white', text='Type password', font=('Helvetica', 11))
password_lbl.place(x=50, y=352)

sql = """SELECT password From customers WHERE username=%s"""
values = (user_entry, )
conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
if record!=None:
    print('Your id is', record)
cursor.close()
conn.close()

password = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
password.place(x=72, y=385)
password.insert(0, *record)

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=408)

password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
lbl_password = Label(reg_frame, image=password_img, bg='white')
lbl_password.place(x=50, y=385)

password.bind('<FocusIn>', onClick)
password.bind('<FocusOut>', onUnclick)

security = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn1 = Button(reg_frame, image=security, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn1.place(x=257, y=386)

# #############################################################________________________________________________________

payment_method_img = ImageTk.PhotoImage(Image.open('img_file/wallet.png'))
payment_method_lbl = Label(reg_frame, image=payment_method_img, bg='white')
payment_method_lbl.place(x=50, y=470)

payment_method_lbl = Label(reg_frame, fg='black', bg='white', text='Payment method', font=('Helvetica', 11))
payment_method_lbl.place(x=50, y=445)

sql = """SELECT payment_method From customers WHERE username=%s"""
values = (user_entry, )
conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
if record!=None:
    print('Your id is', record)
cursor.close()
conn.close()

payment_method = ttk.Combobox(reg_frame, values=['Cash', 'E-Banking'], width=25)
payment_method.place(x=105, y=470)
payment_method.insert(0, *record)

update_img = ImageTk.PhotoImage(Image.open('img_file/update1.png'))
update_btn = Button(reg_frame, image=update_img, borderwidth=0, bg='white', cursor='hand2', command=update_profile)
update_btn.place(x=60, y=530)

prof_window.mainloop()