# importing all the required modules and libraries.
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from searchdata import searchdrivers
#creating the function to destro registration window and import login window.
def login_page():
    reg_window.destroy()
    import login
# creating the function that clear datas if user is already signed up
def clear():
    user.delete(0, 'end')
    address.delete(0, 'end')
    email.delete(0, 'end')
    contact.delete(0, 'end')
    password.delete(0, 'end')
    con_password.delete(0, 'end')
    license.delete(0, 'end')
# function that fill the placeholder after clearin data.
def fill():
    user.insert(0, 'Type your username')
    address.insert(0, 'Type your address')
    email.insert(0, 'Example@gmail.com')
    contact.insert(0, 'Phone no.')
    password.insert(0, 'Type password')
    con_password.insert(0, 'Confirm password')

# function for validation and inserting data into the table.
def datastore():
    # checking if the data has filled the all feild or not.
    if user.get() == 'Type your username' or address.get() == 'Type your address' or email.get() == 'Example@gmail.com' or contact.get() == 'Phone no.' or password.get() == 'Type Password' or con_password.get() == 'Confirm password':
        messagebox.showerror('Error', 'All field must be filled.')

    elif user.get() == '' or address.get() == '' or email.get() == '' or contact.get() == '' or password.get() == '' or con_password.get() == '' or license == '' :
         messagebox.showerror('Error', 'All field must be filled.')

    else:
        # adding limitations to contact no and password.
        phone = contact.get()
        if phone.isalnum():
            val = phone
            if len(val) > 10 or len(val) < 10:
                messagebox.showinfo('Contact', 'Invalid contact no.')
            else:
                psw = password.get() and con_password.get()
                if psw.isalnum() and psw != 'Type password':
                    value = psw
                    if len(value) > 8 or len(value) < 8:
                        messagebox.showerror('Error', 'password limitation not fulfilled (must be 8 character).')

                    elif password.get() != con_password.get():
                        messagebox.showerror('Error', 'Password mismatched!')

                    elif license.get() == '':
                        messagebox.showinfo('license ', 'please enter your license no.')

                    else:
                        username = user.get()
                        record = searchdrivers(username)
                        if record != None:
                            messagebox.showinfo('Taxi Booking System', 'user already exist!')
                            clear()
                            fill()
                        else:
                            sql = """INSERT INTO drivers VALUES(%s, %s, %s, %s, %s, %s, %s)"""
                            values = ['', user.get(), address.get(), email.get(), contact.get(), license.get(), password.get() ]
                            conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            conn.commit()
                            cursor.close()
                            conn.close()
                            print('Record inserted sucessfully')
                            messagebox.showinfo('Taxi booking system', 'Your records are saved!')
                            clear()
                            fill()
                            reg_window.destroy()
                            import login
# creating the registration window.
reg_window = Tk()
reg_window.geometry('900x650')
reg_window.title('Taxi booking system')
reg_window.resizable(False, False)

win_bg = ImageTk.PhotoImage(Image.open('img_file/Component 8.png'))
bg_lbl = Label(reg_window, image=win_bg)
bg_lbl.pack()

reg_frame = Frame(reg_window, width=350, height=640, bg='white', highlightbackground='black', highlightthickness=1)
reg_frame.place(x=300, y=5)

login = ImageTk.PhotoImage(Image.open('img_file/Sign up1.png'))
lbl1 = Label(reg_frame, image=login, bg='white')
lbl1.place(x=100, y=5)

#####################______________________________________________________________________
# creating placeholder using FocusIn, FocusOut event.
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

user = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
user.place(x=70, y=76)
user.insert(0, 'Type your username')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=98)

user_img = ImageTk.PhotoImage(Image.open('img_file/user_icon_1.png'))
user_img_lbl = Label(reg_frame, image=user_img, bg='white')
user_img_lbl.place(x=50, y=76)

user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# #########################__________________________________________________________________________
# creating placeholder using FocusIn, FocusOut event.
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

address = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
address.place(x=70, y=150)
address.insert(0, 'Type your address')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=174)

add_img = ImageTk.PhotoImage(Image.open('img_file/addimg.png'))
lbl_add = Label(reg_frame, image=add_img, bg='white')
lbl_add.place(x=50, y=150)

address.bind('<FocusIn>', on_Enter)
address.bind('<FocusOut>', on_Leave)
# #####################################___________________________________________________
# creating placeholder using FocusIn, FocusOut event.
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

email = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
email.place(x=72, y=230)
email.insert(0, 'Example@gmail.com')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=254)

mail_img = ImageTk.PhotoImage(Image.open('img_file/mailimg.png'))
lbl_mail = Label(reg_frame, image=mail_img, bg='white')
lbl_mail.place(x=50, y=230)

email.bind('<FocusIn>', on_click)
email.bind('<FocusOut>', on_unclick)
#
# ##########################################__________________________________________________________________________
## creating placeholder using FocusIn, FocusOut event.
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

contact = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
contact.place(x=73, y=310)
contact.insert(0, 'Phone no.')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=332)

phone_img = ImageTk.PhotoImage(Image.open('img_file/phoneimg.png'))
lbl_phone = Label(reg_frame, image=phone_img, bg='white')
lbl_phone.place(x=50, y=310)

contact.bind('<FocusIn>', on_Click)
contact.bind('<FocusOut>', on_Unclick)

# #####################################################________________________________________________________________
show_icon = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
hide_icon = ImageTk.PhotoImage(Image.open('img_file/passwordEye1.png'))
# creating placeholder using FocusIn, FocusOut event.
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

password = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
password.place(x=72, y=385)
password.insert(0, 'Type password')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=408)

password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
lbl_password = Label(reg_frame, image=password_img, bg='white')
lbl_password.place(x=50, y=385)

password.bind('<FocusIn>', onClick)
password.bind('<FocusOut>', onUnclick)

security = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn1 = Button(reg_frame, image=security, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn1.place(x=257, y=386)

# ###################################################___________________________________________________________________

show_icon = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
hide_icon = ImageTk.PhotoImage(Image.open('img_file/passwordEye1.png'))
# creating placeholder using FocusIn, FocusOut event.
def on_hold(e):
    psw1=con_password.get()
    if psw1=='Confirm password':
        con_password.delete(0, 'end')
    else:
        contact.get()

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

con_password_lbl = Label(reg_frame, fg='black', bg='white', text='Confirm password', font=('Helvetica', 11))
con_password_lbl.place(x=50, y=429)

con_password = Entry(reg_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
con_password.place(x=72, y=460)
con_password.insert(0, 'Confirm password')

Frame(reg_frame, width=230, height=2, bg='#969090').place(x=50, y=482)

con_password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
lbl_con_password = Label(reg_frame, image=con_password_img, bg='white')
lbl_con_password.place(x=50, y=460)

con_password.bind('<FocusIn>', on_hold)
con_password.bind('<FocusOut>', on_free)

security_con = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn = Button(reg_frame, image=security_con, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn.place(x=257, y=460)

# #############################################################________________________________________________________

sign_in = Label(reg_frame, text='Have an account?', fg='black', bg='white', font=('Helvetica', 8))
sign_in.place(x=50, y=555)

sign_in_btn = Button(reg_frame, text='sign in.', font=('Helvetica', 8), fg='Black', bg='White', borderwidth=0, width=5, cursor='hand2', command=login_page)
sign_in_btn.place(x=141, y=555)

Frame(reg_frame, width=34, height=1, bg='Black').place(x=143, y=575)

license_img = ImageTk.PhotoImage(Image.open('img_file/cid.png'))
license_lbl = Label(reg_frame, image=license_img, bg='white')
license_lbl.place(x=50, y=529)

license_no_lbl = Label(reg_frame, fg='black', bg='white', text='License No.', font=('Helvetica', 11))
license_no_lbl.place(x=50, y=500)

license = Entry(reg_frame, width=25, borderwidth=3)
license.place(x=105, y=529)

# creating hover button using Enter, leave event.
def onEnter(event):
    global create_img
    create_img = ImageTk.PhotoImage(Image.open('img_file/Group 6.png'))
    create_btn.config(image=create_img)

def onLeave(event):
    global create_img
    create_img = ImageTk.PhotoImage(Image.open('img_file/Group 5.png'))
    create_btn.config(image=create_img)

create_img = ImageTk.PhotoImage(Image.open('img_file/Group 5.png'))
create_btn = Button(reg_frame, image=create_img, borderwidth=0, bg='white', cursor='hand2', command=datastore)
create_btn.place(x=110, y=585)

create_btn.bind('<Enter>', onEnter)
create_btn.bind('<Leave>', onLeave)

reg_window.mainloop()