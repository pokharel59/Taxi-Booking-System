#importing all the required libraries.
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from searchdata import searchmail, drivermail
import mysql.connector
import sys

def login():
# checking if the users have filled all the datas or not.
    if email.get() == 'Type your username' or password.get() == 'Type Password' or con_password.get() == 'Confirm password':
        messagebox.showerror('Error', 'All field must be filled.')

    elif email.get() == '' or password.get() == '' or con_password.get() == '':
        messagebox.showerror('Error', 'All field must be filled.')
# checking if the password and confirm password are equal or not.
    elif password.get() != con_password.get():
         messagebox.showerror('Error', 'Password mismatched!')


    else:
    # retreiving the eail from customers and driver data if the customer and driver exist or not.
        mail = email.get()
        record = searchmail(mail)
        if record == None:
            mail = email.get()
            record = drivermail(mail)
            if record == None:
                messagebox.showinfo('Taxi Booking System', 'user did not match!')
            else:
                # if the users exist thant updating the new password.
                sql = """UPDATE drivers set password=%s WHERE email=%s"""
                values = (password.get(), email.get())
                conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                               database='tbs')
                cursor = conn.cursor()
                cursor.execute(sql, values)
                conn.commit()
                cursor.close()
                conn.close()
                print('Sucessfull!')
                messagebox.showinfo('Taxi Booking System', 'your password has been updated')

        else:
            sql = """UPDATE customers set password=%s WHERE email=%s"""
            values = (password.get(), email.get())
            try:
                conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                               database='tbs')
                cursor = conn.cursor()
                cursor.execute(sql, values)
                conn.commit()
                cursor.close()
                conn.close()
                print('Sucessfull!')
                messagebox.showinfo('Taxi Booking System', 'your password has been updated')
            except:
                print("Error : ", sys.exc_info())
            finally:
                del values, sql

# creating the window for forget password.
window = Tk()
window.geometry('900x500')
window.resizable(False, False)
window.title('Taxi Bookng System')

win_bg = ImageTk.PhotoImage(Image.open('img_file/Component 4.png'))
bg_lbl = Label(window, image=win_bg)
bg_lbl.pack()

frame = Frame(window, width=315, height=435, bg='white')
frame.place(x=300, y=33)

login_img = ImageTk.PhotoImage(Image.open('img_file/Forgot Password !.png'))
login_img_lbl = Label(frame, bg='white', image=login_img)
login_img_lbl.place(x=18, y=12)

############################__________________________________________________________________________________________

def onClick(e):
    user=email.get()
    if user=='Type your email':
        email.delete(0, 'end')
    else:
        email.get()


def onUnclick(e):
    user=email.get()
    if user=='':
        email.insert(0, 'Type your email')

email_lbl = Label(frame, fg='black', bg='white', text='Email', font=('Helvetica', 11))
email_lbl.place(x=50, y=70)

email = Entry(frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
email.place(x=70, y=103)
email.insert(0, 'Type your email')

Frame(frame, width=215, height=2, bg='#969090').place(x=50, y=125)

mail_img = ImageTk.PhotoImage(Image.open('img_file/mailimg.png'))
lbl_mail = Label(frame, image=mail_img, bg='white')
lbl_mail.place(x=50, y=103)

email.bind('<FocusIn>', onClick)
email.bind('<FocusOut>', onUnclick)

 ###########################################_______________________________________________________________

show_icon = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
hide_icon = ImageTk.PhotoImage(Image.open('img_file/passwordEye1.png'))
# creating placeholder using FocusIn, FocusOut event.
def on_Click(e):
    add=password.get()
    if add=='Password':
        password.delete(0, 'end')
    else:
        password.get()


def on_Unclick(e):
    add=password.get()
    if add=='':
        password.insert(0, 'Password')

def show_hide_icon():
    if password['show'] == '*':
        security_btn1.config(image=show_icon)
        password.config(show='')

    else:
        security_btn1.config(image=hide_icon)
        password.config(show='*')

password_lbl = Label(frame, fg='black', bg='white', text='Password', font=('Helvetica', 11))
password_lbl.place(x=50, y=163)

password = Entry(frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
password.place(x=67, y=198)
password.insert(0, 'Password')

Frame(frame, width=215, height=2, bg='#969090').place(x=50, y=220)

password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
lbl_password = Label(frame, image=password_img, bg='white')
lbl_password.place(x=47, y=198)

password.bind('<FocusIn>', on_Click)
password.bind('<FocusOut>', on_Unclick)

security = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn1 = Button(frame, image=security, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn1.place(x=248, y=198)

#############################################______________________________________________________________________________
# creating placeholder using FocusIn, FocusOut event.
def on_hold(e):
    add=con_password.get()
    if add=='Confirm password':
        con_password.delete(0, 'end')
    else:
        con_password.get()

def on_free(e):
    psw1=con_password.get()
    if psw1 == '':
        con_password.insert(0, 'Confirm password')

def show_hide_icon():
    if con_password['show'] == '*':
        security_btn.config(image=show_icon)
        con_password.config(show='')

    else:
        security_btn.config(image=hide_icon)
        con_password.config(show='*')

con_password_lbl = Label(frame, fg='black', bg='white', text='Confirm password', font=('Helvetica', 11))
con_password_lbl.place(x=50, y=263)

con_password = Entry(frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
con_password.place(x=72, y=298)
con_password.insert(0, 'Confirm password')

Frame(frame, width=215, height=2, bg='#969090').place(x=50, y=320)

con_password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
lbl_con_password = Label(frame, image=con_password_img, bg='white')
lbl_con_password.place(x=50, y=298)

con_password.bind('<FocusIn>', on_hold)
con_password.bind('<FocusOut>', on_free)

security_con = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn = Button(frame, image=security_con, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn.place(x=248, y=298)

update_img = ImageTk.PhotoImage(Image.open('img_file/update1.png'))
update_btn = Button(frame, image=update_img, borderwidth=0, bg='white', cursor='hand2', command=login)
update_btn.place(x=60, y=350)
window.mainloop()