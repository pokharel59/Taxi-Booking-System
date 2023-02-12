# importing all the required libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def loging_out():
    root.destroy()
    import login

def select_data(event):
    selected_item = tree.item(tree.focus())
    did_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    licenseno_entry.delete(0, 'end')
    did_entry.insert(0, selected_item["values"][0])
    username_entry.insert(0, selected_item["values"][1])
    address_entry.insert(0, selected_item["values"][2])
    email_entry.insert(0, selected_item["values"][3])
    contact_entry.insert(0, selected_item["values"][4])
    licenseno_entry.insert(0, selected_item["values"][5])

#bind the function to the TreeView


def clear_data():
# clearing all the entry boxex if clear button is clicked.
    did_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    licenseno_entry.delete(0, 'end')

# Retriving datas from drivers table.
sql = """SELECT * FROM drivers"""
conn = mysql.connector.connect(host="localhost", user="root", password="",port=3306, database="tbs")
cursor = conn.cursor()
cursor.execute(sql)
data = cursor.fetchall()

#creating viewwing window for admin.
root = tk.Tk()
root.geometry('1250x650')
root.resizable(False, False)
root.configure(bg='white')
root.title('Taxi Bookng System')

style = ttk.Style()
style.theme_use('default')
style.configure('Treeview', background='#D3D3D3', foregroung='black', rowheight=25, fieldbackground='#D3D3D3')

win_bg = ImageTk.PhotoImage(Image.open('img_file/admin_bg.png'))
bg_lbl = Label(root, image=win_bg)
bg_lbl.pack()

title = Label(root, text='Drivers', font=('League spartan', 20, 'bold'), bg='white', fg='black')
title.place(x=570, y=1)

# creating frame to iinsert treeview widget inside it.
frame = tk.Frame(root, bg='white', width=636, height=300)
frame.place(x=20, y=37)

#crearing the scrollbar foe treeview widget.
tree_scroll = Scrollbar(frame)
tree_scroll.configure(width=15)
tree_scroll.pack(side=RIGHT, fill=Y)

# creating the treeview widget for driver detail.
tree = ttk.Treeview(frame, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show="headings", height=5)
tree.heading("col1", text="DID")
tree.heading("col2", text="Username")
tree.heading("col3", text="Address")
tree.heading("col4", text="Email")
tree.heading("col5", text="Contact No.")
tree.heading("col6", text="License No.")
tree.pack(fill="both", expand=True)
# label frame created to insert drivers detail according to feild name.

def assign():
    if username_entry.get() != '' or address_entry.get() != '' or email_entry.get() != '' or contact_entry.get() != '' or licenseno_entry != '' or did_entry != '':
        messagebox.showinfo('Taxi Booking System', 'Driver is assigned!')
    else:
        print('Error')

frame_record = LabelFrame(root, text='Records', width=1218, height=120, bg='#D3D3D3')
frame_record.place(x=20, y=180)

username_label =  Label(frame_record, text='username', bg='#D3D3D3', font=('League spartan', 10))
username_label.place(x=25, y=60)

username_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9))
username_entry.place(x=120, y=60)

address_label =  Label(frame_record, text='Address', bg='#D3D3D3', font=('League spartan', 10))
address_label.place(x=180, y=15)

address_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9))
address_entry.place(x=260, y=15)

email_label =  Label(frame_record, text='Email', bg='#D3D3D3', font=('League spartan', 10))
email_label.place(x=420, y=15)

email_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9))
email_entry.place(x=490, y=15)

contact_label =  Label(frame_record, text='Contact No.', bg='#D3D3D3', font=('League spartan', 10))
contact_label.place(x=650, y=15)

contact_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9))
contact_entry.place(x=750, y=15)

licenseno_label =  Label(frame_record, text='License No.', bg='#D3D3D3', font=('League spartan', 10))
licenseno_label.place(x=890, y=15)

licenseno_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9))
licenseno_entry.place(x=980, y=15)

did_label =  Label(frame_record, text='DID', bg='#D3D3D3', font=('League spartan', 10))
did_label.place(x=25, y=15)

did_entry = Entry(frame_record, borderwidth=3, font=('League spartan', 9), width=8)
did_entry.place(x=70, y=15)

#bind the function to the TreeView
tree.bind('<ButtonRelease-1>', select_data)

buttons = LabelFrame(root, text='Buttons', width=1218, height=90, bg='#D3D3D3')
buttons.place(x=20, y=299)

assign_buttons = Button(buttons, text='Assign', width=20, bg='#D3D3D3', command=assign)
assign_buttons.place(x=500, y=20)

clear_btn = Button(buttons, text='Clear', width=20, bg='#D3D3D3', command=clear_data)
clear_btn.place(x=300, y=20)

logout_btn = Button(buttons, text='Logo out', width=20, bg='#D3D3D3', command=loging_out)
logout_btn.place(x=700, y=20)

# Insert some data
for item in data:
    tree.insert("", "end", text="Item", values=item)

tree.tag_configure("oddrow", background="white")
tree.tag_configure("evenrow", background="lightblue")

root_items = tree.get_children("")

# creating loop to colour the datas if the modulas 2 is equal to 0.
for i in range(len(root_items)):
    if i % 2 == 0:
        tree.item(tree.get_children("")[i], tags=("evenrow",))
    else:
        tree.item(tree.get_children("")[i], tags=("oddrow",))

customer_frame = Frame(root, width=1250, height=300, bg='red')
customer_frame.place(x=120, y=440)

customer = Label(root, text='Customer', font=('League spartan', 20, 'bold'), bg='white', fg='black')
customer.place(x=565, y=395)

query = """SELECT * FROM ride_detail"""
con = mysql.connector.connect(host="localhost", user="root", password="",port=3306, database="tbs")
cursr = con.cursor()
cursr.execute(query)
record = cursr.fetchall()

treeview_scroll = Scrollbar(customer_frame)
treeview_scroll.configure(width=15)
treeview_scroll.pack(side=RIGHT, fill=Y)

treeview = ttk.Treeview(customer_frame, columns=("col1", "col2", "col3", "col4", "col5"), show="headings", height=7)
treeview.heading("col1", text="SNO.")
treeview.heading("col2", text="Username")
treeview.heading("col3", text="Pickup Location")
treeview.heading("col4", text="Dropoff Location")
treeview.heading("col5", text="Pickup Time")
treeview.pack(fill="both", expand=True)

for item in record:
    treeview.insert("", "end", text="Item", values=(item[0], item[1], item[2], item[3], item[4]))

treeview.tag_configure("oddrow", background="white")
treeview.tag_configure("evenrow", background="lightblue")

root_item = treeview.get_children("")

for i in range(len(root_item)):
    if i % 2 == 0:
        treeview.item(treeview.get_children("")[i], tags=("evenrow",))
    else:
        treeview.item(treeview.get_children("")[i], tags=("oddrow",))

root.mainloop()
