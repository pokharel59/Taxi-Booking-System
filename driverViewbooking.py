#importing all the required modules and libraries.
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

# creaing the function that destroy the window and call the import wimdow.
def back():
    driver_view_window.destroy()
    import login

def finished_trip():
    driver_view_window.destroy()
    import login

def confirm_book():
    messagebox.showinfo('Taxi Booking Sytem', 'Get ready for the ride!')


# retreiving customers datas from customer table to create customer detail.
sql = """SELECT username FROM customers WHERE cid=%s"""
values = (1, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT pickup_location FROM ride_detail WHERE s_no=%s"""
values = (21, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record1 = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT dropoff_location FROM ride_detail WHERE s_no=%s"""
values = (21, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record2 = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT pickup_time FROM ride_detail WHERE s_no=%s"""
values = (21, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record3 = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT email FROM customers WHERE cid=%s"""
values = (2, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record4 = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT phone_no FROM customers WHERE cid=%s"""
values = (2, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record5 = cursor.fetchone()
conn.close()
cursor.close()

sql = """SELECT payment_method FROM customers WHERE cid=%s"""
values = (2, )

conn = mysql.connector.connect(user='root', host='localhost', port=3306, password='',
                                       database='tbs')
cursor = conn.cursor()
cursor.execute(sql, values)
record6 = cursor.fetchone()
conn.close()
cursor.close()

#creating view window
driver_view_window = Tk()
driver_view_window.geometry('700x450')
driver_view_window.resizable(False, False)
driver_view_window.configure(bg='#6A2AF7')
driver_view_window.title('viewBooking')

customer_img2 = ImageTk.PhotoImage(Image.open('img_file/icons8-driver-100.png'))
customer_lbl2 = Label(driver_view_window, image=customer_img2, bg='#6A2AF7', width=75, height=75)
customer_lbl2.place(x=325, y=142)

customer_img = ImageTk.PhotoImage(Image.open('img_file/Rectangle 23.png'))
customer_lbl = Label(driver_view_window, image=customer_img, bg='#6A2AF7')
customer_lbl.place(x=9, y=195)

trip_img = ImageTk.PhotoImage(Image.open('img_file/Upcoming Trips.png'))
trip = Label(driver_view_window, bg='#6A2AF7', image=trip_img)
trip.place(x=50, y=10)

upc_trip = Label(driver_view_window, bg='#6A2AF7', fg='white', text=('From godawari To tirpureshwor'), font=('Leagur spartan', 13))
upc_trip.place(x=55, y=55)

driver_name = Label(driver_view_window, bg='#6A2AF7', fg='white', text=('From tinkune To chandragiri'), font=('Leagur spartan', 13))
driver_name.place(x=55, y=110)

trip_frame = Frame(driver_view_window, bg='white', height=3, width=360)
trip_frame.place(x=50, y=80)

trip_frame1 = Frame(driver_view_window, bg='white', height=3, width=360)
trip_frame1.place(x=50, y=135)

user_img = ImageTk.PhotoImage(Image.open('img_file/Rectangle 30.png'))
user_lbl = Label(driver_view_window, image=user_img, bg='#6A2AF7')
user_lbl.place(x=540, y=8)

driver_name = Label(driver_view_window, bg='white', fg='black', text=('Tek bahadur'), font=('Leagur spartan', 13))
driver_name.place(x=560, y=12)

cancelbtn_img = ImageTk.PhotoImage(Image.open('img_file/Component 16.png'))
cancel_btn = Button(driver_view_window, image=cancelbtn_img, borderwidth=0, bg='white', command=finished_trip)
cancel_btn.place(x=170, y=200)

confirmbtn_img = ImageTk.PhotoImage(Image.open('img_file/Component 15.png'))
confirm_btn = Button(driver_view_window, image=confirmbtn_img, borderwidth=0, bg='white', command=confirm_book)
confirm_btn.place(x=385, y=200)

back_img = ImageTk.PhotoImage(Image.open('img_file/back.png'))
back_lbl = Button(driver_view_window, image=back_img, bg='#6A2AF7', borderwidth=0, command=back)
back_lbl.place(x=10, y=10)

customer1_img = ImageTk.PhotoImage(Image.open(('img_file/Customer.png')))
customer1_lbl = Label(driver_view_window, image=customer1_img, bg='white')
customer1_lbl.place(x=40, y=235)

customer_frm = Frame(driver_view_window, bg='#6A2AF7', width=130, height=3)
customer_frm.place(x=40, y=265)

customer_username = Label(driver_view_window, text=str(*record), fg='black', bg='white', font=('League spartan', 12))
customer_username.place(x=45, y=275)

customer_detail = Label(driver_view_window, text='Details', fg='black', bg='white', font=('League spartan', 12, 'bold'))
customer_detail.place(x=50, y=320)

customer_frame =  Frame(driver_view_window, bg='#6A2AF7', width=610, height=3)
customer_frame.place(x=40, y=315)

detail_frame1 = Frame(driver_view_window, bg='#6A2AF7', width=3, height=115)
detail_frame1.place(x=40, y=315)

customer_pickup = Label(driver_view_window, text='Pickup Location of customer is ' + str(*record1), fg='black', bg='white', font=('League spartan', 12))
customer_pickup.place(x=50, y=350)

customer_dropoff = Label(driver_view_window, text=' Dropoff Location of customer is ' + str(*record2), fg='black', bg='white', font=('League spartan', 12))
customer_dropoff.place(x=350, y=350)

customer_pickup_time = Label(driver_view_window, text=' Pickup time of customer is ' + str(*record3), fg='black', bg='white', font=('League spartan', 12))
customer_pickup_time.place(x=45, y=375)

customer_email = Label(driver_view_window, text=' Email of customer is ' + str(*record4), fg='black', bg='white', font=('League spartan', 12))
customer_email.place(x=270, y=375)

customer_contact = Label(driver_view_window, text=' Phone no. of customer is ' + str(*record5), fg='black', bg='white', font=('League spartan', 12))
customer_contact.place(x=315, y=400)

customer_payment = Label(driver_view_window, text=' Payment method. of customer is ' + str(*record6), fg='black', bg='white', font=('League spartan', 12))
customer_payment.place(x=45, y=400)

detail_frame =  Frame(driver_view_window, bg='#6A2AF7', width=610, height=3)
detail_frame.place(x=40, y=430)

detail_frame2 = Frame(driver_view_window, bg='#6A2AF7', width=3, height=118)
detail_frame2.place(x=650, y=315)

driver_view_window.mainloop()