#importing all the required modules and libraries.
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from searchdata import searchall, searchdriver
import mysql.connector
from tkintermapview import TkinterMapView

def import_profile():
    window.destroy()
    import profile

# function to destroy window import login if logout button is clicked.
def logout():
    window.destroy()
    import login
#function to destroy window and import registration window if signup button is clicked.
def signup_page():
    window.destroy()
    import registration

# function to destry window and import forgetpassword window if firget password button is placed.
def forget_password():
    window.destroy()
    import forgetpassword


def databaseCheck():
# checking if the username and password is entry box is filled or not if not filled than poping the message box to give alert.

    if user_entry.get() == 'Type your username' or password_entry.get() == 'Type Password':
        messagebox.showerror('Error', 'All field must be filled.')

    elif user_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All field must be filled.')

# checking if username or password is of admin than inporting admin window.

    elif user_entry.get() == 'admin' and password_entry.get() == 'admin':
        window.destroy()
        import admin


    else:
        # retreiving the username and password from user inputed value in the particular entry box if user inputed value is in databse than
        #impoting next window else checking user inputed value is from drivers table tham importing drivers view booking if user inputed value is none
        #than pooping up yhe meassage box giving alert that user did not exist

        username = user_entry.get()
        password = password_entry.get()
        record = searchall(username, password)
        if record == None:
            username = user_entry.get()
            password = password_entry.get()
            record = searchdriver(username, password)
            if record == None:
                messagebox.showinfo('Taxi Booking System', 'user did not match!')
            else:
                window.destroy()
                import driverViewbooking
        else:
            window.withdraw()

            def confirmbook():
# Alerting the users if they clicked the button withount insertinfg data in entry box.
                if pickup_entry.get() == 'Pickup location' or dropoff_entry.get() == 'Dropoff location' or picktime_entry.get() == 'Pickup time':
                    messagebox.showerror('Incorrect', 'enter valid locations and time.')

                elif pickup_entry.get() == '' or dropoff_entry.get() == '' or picktime_entry.get() == '':
                    messagebox.showerror('Incorrect', 'All feilds required')
# if datas are inserted into entry box than inserting those datas into ride_details table.
                else:
                    sql = """INSERT INTO ride_detail VALUES(%s, %s, %s, %s, %s)"""
                    values = ['', user_entry.get(), pickup_entry.get(), dropoff_entry.get(), picktime_entry.get()]

                    conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                                   database='tbs')
                    cursor = conn.cursor()
                    cursor.execute(sql, values)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    print('Record inserted sucessfully')

# withdraw method is used to in confirm window to hide the window and import next window if all the criteria is fullfilled.s
                    confirm_window.withdraw()

                    def validation():
# checking if the edit window entry box entry boxes are filled or not if not then alerting the user.
                        if dropoff_entr == '' or pickup_entr == '' or pickup_time_entry == '':
                            messagebox.showinfo('Invalid' 'All must be required')
                        else:
# if user filled all the entry box ang click the button than the value is updated in the rie_detail table.
                            sql = """UPDATE ride_detail set pickup_location=%s, dropoff_location=%s, pickup_time=%s WHERE username=%s"""
                            values = (
                            dropoff_entr.get(), pickup_entr.get(), pickup_time_entry.get(), user_entry.get())
                            conn = mysql.connector.connect(host='localhost', user='root', port=3306,
                                                           password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            conn.commit()
                            cursor.close()
                            conn.close()
                            print('Sucessfull!')
# updating the data and withdrawing the edit window and importing the view booking window.
                            edit_window.withdraw()
# retreiving the datas from tables of drivers for driver details.

                            def confirm():
                                messagebox.showinfo('Taxi Booking System', 'Congratulation! Your ride is booked.')
                                view_window.destroy()
                                edit_window.destroy()
                                confirm_window.deiconify()

                            def delete_ride():
                                sql = """DELETE FROM ride_detail WHERE username=%s"""
                                values = (user_entry.get(),)

                                conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                               database='tbs')
                                cursor = conn.cursor()
                                cursor.execute(sql, values)
                                conn.commit()
                                conn.close()
                                cursor.close()

                                confirm_window.deiconify()
                                view_window.destroy()
                                edit_window.destroy()


                            sql = """SELECT username FROM drivers WHERE did=%s"""
                            values = (1,)

                            conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            record = cursor.fetchone()
                            conn.close()
                            cursor.close()

                            sql = """SELECT address FROM drivers WHERE did=%s"""
                            values = (1,)

                            conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            record1 = cursor.fetchone()
                            conn.close()
                            cursor.close()

                            sql = """SELECT email FROM drivers WHERE did=%s"""
                            values = (1,)

                            conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            record2 = cursor.fetchone()
                            conn.close()
                            cursor.close()

                            sql = """SELECT phone_no FROM drivers WHERE did=%s"""
                            values = (1,)

                            conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            record3 = cursor.fetchone()
                            conn.close()
                            cursor.close()

                            sql = """SELECT license_no FROM drivers WHERE did=%s"""
                            values = (1,)

                            conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                                           database='tbs')
                            cursor = conn.cursor()
                            cursor.execute(sql, values)
                            record4 = cursor.fetchone()
                            conn.close()
                            cursor.close()
# creating the view bookin window.
                            view_window = Toplevel(edit_window)
                            view_window.geometry('700x450')
                            view_window.resizable(False, False)
                            view_window.configure(bg='#6A2AF7')
                            view_window.title('viewBooking')

                            detail_img = ImageTk.PhotoImage(Image.open('img_file/Rectangle 23.png'))
                            detail_lbl = Label(view_window, image=detail_img, bg='#6A2AF7')
                            detail_lbl.place(x=9, y=195)

                            trip_img = ImageTk.PhotoImage(Image.open('img_file/Trip.png'))
                            trip = Label(view_window, bg='#6A2AF7', image=trip_img)
                            trip.place(x=310, y=15)

                            user_img = ImageTk.PhotoImage(Image.open('img_file/Rectangle 30.png'))
                            user_lbl = Label(view_window, image=user_img, bg='#6A2AF7')
                            user_lbl.place(x=540, y=10)

                            user_name = Label(view_window, text=user_entry.get(), bg='white', fg='black', font=('Lwague spartan', 13))
                            user_name.place(x=560, y=15)

                            from_img = ImageTk.PhotoImage(Image.open('img_file/From.png'))
                            from_lbl = Label(view_window, bg='#6A2AF7', image=from_img)
                            from_lbl.place(x=60, y=60)

                            from_entry = Label(view_window, text=pickup_entry.get(), bg='#6A2AF7', fg='white', font=('League spartan', 17, 'bold'))
                            from_entry.place(x=70, y=90)

                            to_img = ImageTk.PhotoImage(Image.open('img_file/To.png'))
                            to_lbl = Label(view_window, bg='#6A2AF7', image=to_img)
                            to_lbl.place(x=610, y=60)

                            to_entry = Label(view_window, text=dropoff_entry.get(), bg='#6A2AF7', fg='white', font=('League spartan', 17, 'bold'))
                            to_entry.place(x=550, y=90)

                            cancelbtn_img = ImageTk.PhotoImage(Image.open('img_file/Component 16.png'))
                            cancel_btn = Button(view_window, image=cancelbtn_img, borderwidth=0, bg='white', command=delete_ride)
                            cancel_btn.place(x=170, y=200)


                            confirmbtn_img = ImageTk.PhotoImage(Image.open('img_file/Component 15.png'))
                            confirm_btn = Button(view_window, image=confirmbtn_img, borderwidth=0, bg='white', command=confirm)
                            confirm_btn.place(x=380, y=200)

                            back_img = ImageTk.PhotoImage(Image.open('img_file/back.png'))
                            back_btn = Button(view_window, image=back_img, bg='#6A2AF7', borderwidth=0)
                            back_btn.place(x=10, y=10)

                            driver_img = ImageTk.PhotoImage(Image.open(('img_file/Driver.png')))
                            driver_lbl = Label(view_window, image=driver_img, bg='white')
                            driver_lbl.place(x=50, y=240)

                            driver_frm = Frame(view_window, bg='#6A2AF7', width=90, height=3)
                            driver_frm.place(x=50, y=270)

                            driver_username = Label(view_window, text=str(*record), fg='black', bg='white',
                                                    font=('League spartan', 12))
                            driver_username.place(x=45, y=280)

                            driver_detail = Label(view_window, text='Details', fg='black', bg='white',
                                                  font=('League spartan', 12, 'bold'))
                            driver_detail.place(x=50, y=320)

                            detail_frame = Frame(view_window, bg='#6A2AF7', width=610, height=3)
                            detail_frame.place(x=40, y=315)

                            detail_frame1 = Frame(view_window, bg='#6A2AF7', width=3, height=95)
                            detail_frame1.place(x=40, y=315)

                            driver_address = Label(view_window, text='Driver is from ' + str(*record1), fg='black',
                                                   bg='white', font=('League spartan', 12))
                            driver_address.place(x=50, y=350)

                            driver_mail = Label(view_window, text=' Email of driver is ' + str(*record2), fg='black',
                                                bg='white', font=('League spartan', 12))
                            driver_mail.place(x=215, y=350)

                            driver_phone = Label(view_window, text=' Contact no. of driver is ' + str(*record3),
                                                 fg='black', bg='white', font=('League spartan', 12))
                            driver_phone.place(x=380, y=350)

                            driver_license = Label(view_window, text=' License no. of driver is ' + str(*record4),
                                                   fg='black', bg='white', font=('League spartan', 12))
                            driver_license.place(x=46, y=380)

                            detail_frame = Frame(view_window, bg='#6A2AF7', width=610, height=3)
                            detail_frame.place(x=40, y=410)

                            detail_frame2 = Frame(view_window, bg='#6A2AF7', width=3, height=98)
                            detail_frame2.place(x=650, y=315)

                            price = Label(view_window, text='235', fg='grey', font=('League spartan', 15, 'bold'),
                                          bg='white')
                            price.place(x=620, y=200)

                            price_lbl = Label(view_window, text='Total:', fg='grey',
                                              font=('League spartan', 15, 'bold'), bg='white')
                            price_lbl.place(x=555, y=200)

                            driver_img2 = ImageTk.PhotoImage(Image.open('img_file/icons8-driver-100.png'))
                            driver_lbl2 = Label(view_window, image=driver_img2, bg='white', width=75, height=75)
                            driver_lbl2.place(x=570, y=230)

                            user_entry.delete(0, 'end')
                            pickup_entry.delete(0, 'end')
                            dropoff_entry.delete(0, 'end')
                            picktime_entry.delete(0, 'end')

                            pickup_entry.insert(0, 'Pickup location')
                            dropoff_entry.insert(0, 'Dropoff location')
                            picktime_entry.insert(0, 'Pickup time')

                            view_window.mainloop()

# creating the edit window.
                    edit_window = Toplevel(confirm_window)
                    edit_window.geometry('900x500')
                    edit_window.resizable(False, False)
                    edit_window.title('Taxi Bookng System')

                    win_bg = ImageTk.PhotoImage(Image.open('img_file/Component 4.png'))
                    bg_lbl = Label(edit_window, image=win_bg)
                    bg_lbl.pack()

                    frame = Frame(edit_window, bg='white', width=638, height=411, highlightbackground='black',
                                  highlightthickness=1)
                    frame.place(x=123, y=44)

                    rounded_img = ImageTk.PhotoImage(Image.open('img_file/rounded_back.png'))
                    rounded_btn = Button(edit_window, image=rounded_img, borderwidth=0, bg='white')
                    rounded_btn.place(x=10, y=10)

                    map = TkinterMapView(frame, width=620, height=210, corner_radius=30)
                    map.place(x=8, y=2)
                    map.set_address(dropoff_entry.get(), marker=True)

                    drop_img = ImageTk.PhotoImage(Image.open('img_file/location-pin1.png'))
                    drop_lbl = Label(frame, bg='white', image=drop_img)
                    drop_lbl.place(x=40, y=220)

                    dropoff_entr = Entry(frame, borderwidth=0, bg='#FFFFFF', font=('Helvetiva', 12))
                    dropoff_entr.insert(0, dropoff_entry.get())
                    dropoff_entr.place(x=65, y=220)

                    frame4 = Frame(frame, height=2, bg='black', width=400)
                    frame4.place(x=60, y=245)

                    pick_img = ImageTk.PhotoImage(Image.open('img_file/location-pin1.png'))
                    pick_lbl = Label(frame, bg='white', image=pick_img)
                    pick_lbl.place(x=40, y=275)

                    pickup_entr = Entry(frame, borderwidth=0, bg='#FFFFFF', font=('Helvetiva', 12))
                    pickup_entr.insert(0, pickup_entry.get())
                    pickup_entr.place(x=65, y=275)

                    frame2 = Frame(frame, height=2, bg='black', width=400)
                    frame2.place(x=60, y=300)

                    timer_img = ImageTk.PhotoImage(Image.open('img_file/timer1.png'))
                    timer_lbl = Label(frame, bg='white', image=timer_img)
                    timer_lbl.place(x=40, y=330)

                    pickup_time_entry = Entry(frame, borderwidth=0, bg='#FFFFFF', font=('Helvetiva', 12))
                    pickup_time_entry.insert(0, picktime_entry.get())
                    pickup_time_entry.place(x=65, y=330)

                    frame3 = Frame(frame, height=2, bg='black', width=400)
                    frame3.place(x=60, y=355)

                    confirm_img = ImageTk.PhotoImage(Image.open('img_file/Component 12.png'))
                    confirm_btn = Button(frame, image=confirm_img, bg='#FFFFFF', borderwidth=0,
                                         command=validation)
                    confirm_btn.place(x=150, y=365)

                    def onenter(e):
                        help_lbl.config(text='Now, you can confirm exact place by seeing map.')

                    def onleave(e):
                        help_lbl.config(text='')

                    help_img = ImageTk.PhotoImage(Image.open('img_file/help1.png'))
                    help_btn = Button(frame, image=help_img, borderwidth=0, bg='white')
                    help_btn.place(x=613, y=0)

                    help_lbl = Label(frame, text='', bg='white')
                    help_lbl.place(x=340, y=2)

                    help_btn.bind('<Enter>', onenter)
                    help_btn.bind('<Leave>', onleave)

                    edit_window.mainloop()

# creating the confirm window.
            confirm_window = Toplevel(window)
            confirm_window.geometry('900x500')
            confirm_window.resizable(False, False)
            confirm_window.title('Taxi Bookng System')

            ########################################___________________________________________________________________________________

            win_bg = ImageTk.PhotoImage(Image.open('img_file/Component 4.png'))
            bg_lbl = Label(confirm_window, image=win_bg)
            bg_lbl.pack()

            frame = Frame(confirm_window, bg='white', width=689, height=411, highlightbackground='black',
                          highlightthickness=1)
            frame.place(x=113, y=44)

            user_name = str(user_entry.get())
            with open('username.txt', 'w') as f:
                f.write(user_name)

            taxi_lbl = Label(frame, text='Taxi               System', font=('League spartan', 13, 'bold'), fg='Black',
                             bg='#FFFFFF')
            taxi_lbl.place(x=0, y=0)

            booking_lbl = Label(frame, text='Booking', font=('league spartan', 13, 'bold'), fg='#F800EE', bg='#FFFFFF')
            booking_lbl.place(x=37, y=0)

            home_btn = Button(frame, text='Home', font=('League spartan', 12, 'bold'), borderwidth=0, bg='#FFFFFF',
                              fg='Black')
            home_btn.place(x=430, y=0)

            profile_btn = Button(frame, text='Profile', font=('League spartan', 12, 'bold'), borderwidth=0,
                                 bg='#FFFFFF',
                                 fg='Black', command=import_profile)
            profile_btn.place(x=520, y=0)

            logout_btn = Button(frame, text='Log out', font=('League spartan', 12, 'bold'), borderwidth=0, bg='#FFFFFF', fg='black', command=logout)
            logout_btn.place(x=600, y=0)

            description_img = ImageTk.PhotoImage(Image.open(('img_file/description.png')))
            description_lbl = Label(frame, image=description_img, bg='#FFFFFF')
            description_lbl.place(x=10, y=50)

            cab_img = ImageTk.PhotoImage(Image.open(('img_file/cab_img.png')))
            cab_lbl = Label(frame, image=cab_img, bg='#FFFFFF', height=315, width=338)
            cab_lbl.place(x=343, y=55)

            box_img = ImageTk.PhotoImage(Image.open('img_file/Variant2.png'))
            box_lbl = Label(frame, image=box_img, bg='#FFFFFF')
            box_lbl.place(x=10, y=190)
# creating placeholder using FocusIn, FocusOut event.
            def onclick(e):
                if pickup_entry.get() == 'Pickup location':
                    pickup_entry.delete(0, 'end')

            def onleave(e):
                if pickup_entry.get() == '':
                    pickup_entry.insert(0, 'Pickup location')

            pickup_entry = Entry(frame, borderwidth=0, bg='#000000', fg='white', font=('League spartan', 12))
            pickup_entry.insert(0, 'Pickup location')
            pickup_entry.place(x=40, y=210)

            frame_pickup = Frame(frame, bg='white', height=2, width=200)
            frame_pickup.place(x=40, y=230)

            pickup_entry.bind('<FocusIn>', onclick)
            pickup_entry.bind('<FocusOut>', onleave)

 # creating placeholder using FocusIn, FocusOut event.
            def on_click(e):
                if dropoff_entry.get() == 'Dropoff location':
                    dropoff_entry.delete(0, 'end')

            def on_leave(e):
                if dropoff_entry.get() == '':
                    dropoff_entry.insert(0, 'Dropoff location')

            dropoff_entry = Entry(frame, borderwidth=0, bg='#000000', fg='white', font=('League spartan', 12))
            dropoff_entry.insert(0, 'Dropoff location')
            dropoff_entry.place(x=40, y=260)

            frame_dropoff = Frame(frame, bg='white', height=2, width=200)
            frame_dropoff.place(x=40, y=280)

            dropoff_entry.bind('<FocusIn>', on_click)
            dropoff_entry.bind('<FocusOut>', on_leave)

# creating placeholder using FocusIn, FocusOut event.
            def onenter(e):
                if picktime_entry.get() == 'Pickup time':
                    picktime_entry.delete(0, 'end')

            def onunenter(e):
                if picktime_entry.get() == '':
                    picktime_entry.insert(0, 'Pickup time')

            picktime_entry = Entry(frame, borderwidth=0, bg='#000000', fg='white', font=('League spartan', 12))
            picktime_entry.insert(0, 'Pickup time')
            picktime_entry.place(x=40, y=310)

            frame_picktime = Frame(frame, bg='white', height=2, width=200)
            frame_picktime.place(x=40, y=330)

            picktime_entry.bind('<FocusIn>', onenter)
            picktime_entry.bind('<FocusOut>', onunenter)

            ride_img = ImageTk.PhotoImage(Image.open('img_file/Variant3.png'))
            ride_btn = Button(frame, image=ride_img, bg='#FFFFFF', borderwidth=0,
                              command=confirmbook)
            ride_btn.place(x=70, y=370)



            confirm_window.mainloop()

# creating loggin window.
window = Tk()
window.geometry('900x500')
window.resizable(False, False)
window.title('login')

########################################___________________________________________________________________________________

win_bg = ImageTk.PhotoImage(Image.open('img_file/Component 4.png'))
bg_lbl = Label(window, image=win_bg)
bg_lbl.pack()

login_frame = Frame(window, width=315, height=435, bg='white')
login_frame.place(x=300, y=33)

login_img = ImageTk.PhotoImage(Image.open('img_file/Login.png'))
login_img_lbl = Label(login_frame, bg='white', image=login_img)
login_img_lbl.place(x=108, y=12)


##################################_______________________________________________________________
# creating placeholder using FocusIn, FocusOut event.
def onClick(event):
    name = user_entry.get()
    if name == 'Type your username':
        user_entry.delete(0, 'end')
    else:
        user_entry.get()


def onUnclick(event):
    name = user_entry.get()
    if name == '':
        user_entry.insert(0, 'Type your username')


username = Label(login_frame, fg='black', bg='white', text='Username', font=('Helvetica', 12))
username.place(x=50, y=80)

user_entry = Entry(login_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
user_entry.insert(0, 'Type your username')
user_entry.place(x=70, y=113)


user_frame = Frame(login_frame, width=215, height=2, bg='#969090')
user_frame.place(x=50, y=135)

user_img = ImageTk.PhotoImage(Image.open('img_file/user_icon_1.png'))
user_img_lbl = Label(login_frame, image=user_img, bg='white')
user_img_lbl.place(x=50, y=113)

user_entry.bind('<FocusIn>', onClick)
user_entry.bind('<FocusOut>', onUnclick)


#####################################________________________________________________________________
# creating placeholder using FocusIn, FocusOut event.
def onClick(event):
    password = password_entry.get()
    if password == 'Type your password':
        password_entry.delete(0, 'end')
    else:
        password_entry.get()


def onUnclick(event):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'Type your password')


password = Label(login_frame, fg='black', bg='white', text='Password', font=('Helvetica', 12))
password.place(x=50, y=180)

password_entry = Entry(login_frame, borderwidth=0, bg='white', fg='#434343', font=('Helvetica', 10), width=28)
password_entry.insert(0, 'Type your password')
password_entry.place(x=67, y=215)

password_frame = Frame(login_frame, width=215, height=2, bg='#969090')
password_frame.place(x=50, y=237)

password_img = ImageTk.PhotoImage(Image.open('img_file/free_icon_3.png'))
password_img_lbl = Label(login_frame, image=password_img, bg='white')
password_img_lbl.place(x=47, y=215)

password_entry.bind('<FocusIn>', onClick)
password_entry.bind('<FocusOut>', onUnclick)

######################################################_________________________________________________

forget_password = Button(login_frame, bg='white', borderwidth=0, cursor='hand2', fg='#3D3D3D', text='Forget password?',
                         font=('Helvetica', 9, 'underline'), command=forget_password)
forget_password.place(x=170, y=240)

login_btn_img = ImageTk.PhotoImage(Image.open('img_file/Default.png'))
login_btn = Button(login_frame, image=login_btn_img, bg='white', borderwidth=0, cursor='hand2',
                   command=databaseCheck)
login_btn.place(x=57, y=279)

or_lbl = Label(login_frame, bg='white', fg='#969090', font=('League spartan', 15, 'bold'), text='or')
or_lbl.place(x=138, y=327)


#####################################_______________________________________________________
# creating placeholder using FocusIn, FocusOut event.
def onEnter(event):
    global signup_btn_img
    signup_btn_img = ImageTk.PhotoImage(Image.open('img_file/signup_grad(img).png'))
    signup_btn.config(image=signup_btn_img)


def onLeave(event):
    global signup_btn_img
    signup_btn_img = ImageTk.PhotoImage(Image.open('img_file/signup(img).png'))
    signup_btn.config(image=signup_btn_img)


signup_btn_img = ImageTk.PhotoImage(Image.open('img_file/signup(img).png'))
signup_btn = Button(login_frame, image=signup_btn_img, bg='white', borderwidth=0, cursor='hand2', command=signup_page)
signup_btn.place(x=88, y=364)

signup_btn.bind('<Enter>', onEnter)
signup_btn.bind('<Leave>', onLeave)
########################################__________________________________________________________________

show_icon = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
hide_icon = ImageTk.PhotoImage(Image.open('img_file/passwordEye1.png'))


def show_hide_icon():
    if password_entry['show'] == '*':
        security_btn.config(image=show_icon)
        password_entry.config(show='')

    else:
        security_btn.config(image=hide_icon)
        password_entry.config(show='*')


security = ImageTk.PhotoImage(Image.open('img_file/passordEye.png'))
security_btn = Button(login_frame, image=security, borderwidth=0, bg='white', cursor='hand2', command=show_hide_icon)
security_btn.place(x=248, y=217)

driver_signup = Label(login_frame, text='If you are driver', bg='white', fg='black', font=('League spartan', 10))
driver_signup.place(x=60, y=410)

def driver_registration():
    window.destroy()
    import driverRegistration

driver_signup_btn = Button(login_frame, text='Sign up', borderwidth=0, bg='white', fg='black', font=('League spartan', 10), cursor='hand2', command=driver_registration)
driver_signup_btn.place(x=151, y=409)

driver_signup_frame = Frame(login_frame, width=50, height=1, bg='black')
driver_signup_frame.place(x=153, y=430)

driver_here = Label(login_frame, text='here', bg='white', fg='black', font=('League spartan', 10))
driver_here.place(x=203, y=410)

####################################_____________________________________________________________________________

window.mainloop()
