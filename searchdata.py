import mysql.connector
import sys
from tkinter import messagebox

def search(username):
    sql = """SELECT * FROM customers WHERE username=%s"""
    values = (username,)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def searchdrivers(username):
    sql = """SELECT * FROM drivers WHERE username=%s"""
    values = (username,)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def searchall(username, password):
    sql = """SELECT * FROM customers WHERE username=%s and password=%s"""
    values = (username, password)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def searchUsername(username):
    sql = """SELECT * FROM customers WHERE username=%s"""
    values = (username)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def updatePassword():
    sql = """UPDATE customers set passwrod=%s WHERE cid=%s"""
    values = (password.get(), uid.get())
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result

def searchmail(email):
    sql = """SELECT * FROM customers WHERE email=%s"""
    values = (email,)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

sql = """SELECT cid from users WHERE username=%s"""
values = ('Aayush Pokharel', )
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
    print(('Error'))

def profileAddress(username):
    sql = """SELECT address From customers WHERE username=%s"""
    values = (username, )
    conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                           database='tbs')
    cursor = conn.cursor()
    cursor.execute(sql, values)
    record = cursor.fetchone()
    if record!=None:
        print('Your id is', record)
    cursor.close()
    conn.close()

def searchdriver(username, password):
    sql = """SELECT * FROM drivers WHERE username=%s and password=%s"""
    values = (username, password)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def drivermail(email):
    sql = """SELECT * FROM drivers WHERE email=%s"""
    values = (email, )
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', port=3306, password='',
                                       database='tbs')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record