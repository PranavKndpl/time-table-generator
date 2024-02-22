import mysql.connector as mycon 
import sys
from tkinter import *

def insert1():
            print("Inserting a Record:")
            ttnum = int(input("Enter Time Table Number:"))
            clss = input("Enter Time Table Class (in Roman):").upper()
            section = input("Enter Time Table Section:").upper()
            day1 = input("Enter Time Table Day:").title()
            time1 = input("Enter Time Table Time (HH:MM):")
            subject = input("Enter Time Table Subject:").title()
            qry = "insert into octimetable (ttnum,clss,section,day1,time1,subject) values \
        ({},'{}','{}','{}','{}','{}')".format(ttnum,clss,section,day1,time1,subject)    
            cur.execute(qry)
            con.commit()
            count = cur.rowcount
            print(count,"record is inserted successfully.")
            
def display():
            count = cur.rowcount
            if count>0:
                qry = "Select * from octimetable order by ttnum"   
                cur.execute(qry)
                data = cur.fetchall()
                print(count," records are retrived successfully.")
                
                print("|----------|-------|----------|-----------|-------|-------------------------|")
                print("| TTNumber | Class | Section  | Day       | Time  | Subject                 |")
                print("|----------|-------|----------|-----------|-------|-------------------------|")
                for row in data:
                    print("| {0:<9d}| {1:<6s}| {2:<9s}| {3:<10s}| {4:<6s}| {5:<24s}|\
    ".format(row[0],row[1],row[2],row[3],row[4],row[5]))
                print("|----------|-------|----------|-----------|-------|-------------------------|")
            else:
                print("No Records To Display")
        
def update():
            print("Update a Record")
            ttnum = int(input("Enter Time Table Number:"))
            qry = "Select * from octimetable where ttnum = {}  order by ttnum".format(ttnum)
            cur.execute(qry)
            row = cur.fetchone()
            count = cur.rowcount
            print(count," record is searched successfully.")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| TTNumber | Class | Section  | Day       | Time  | Subject                 |")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| {0:<9d}| {1:<6s}| {2:<9s}| {3:<10s}| {4:<6s}| {5:<24s}|\
".format(row[0],row[1],row[2],row[3],row[4],row[5]))
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            clss = input("Enter Time Table Class (New) or . old value:").upper()
            section = input("Enter Time Table Section (New) or . old value:").upper()
            day1 = input("Enter Time Table Day (New) or . old value:").title()
            time1 = input("Enter Time Table Time (New) or . old value:")
            subject = input("Enter Time Table Subject (New) or . old value:").title()
            if clss == '.':
                clss = row[1]
            if section == '.':
                section = row[2]
            if day1 == '.':
                day1 = row[3]
            if time1 == '.':
                time1 = row[4]
            if subject == '.':
                subject = row[5]
            qry = "update octimetable set clss = '{}', section = '{}', day1 = '{}',\
time1 = '{}', subject = '{}' where ttnum = {}".format(clss,section,day1,time1,subject,ttnum)
            cur.execute(qry)
            con.commit()
            count = cur.rowcount
            print(count," record is updated successfully.")
    
def delete():
            print("Delete a Record")
            ttnum = int(input("Enter Time Table Number:"))
            qry = "Select * from octimetable where ttnum = {}".format(ttnum)
            cur.execute(qry)
            row = cur.fetchone()
            count = cur.rowcount
            print(count," record is searched successfully.")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| TTNumber | Class | Section  | Day       | Time  | Subject                 |")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| {0:<9d}| {1:<6s}| {2:<9s}| {3:<10s}| {4:<6s}| {5:<24s}|\
".format(row[0],row[1],row[2],row[3],row[4],row[5]))
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            qry = "delete from octimetable where ttnum = {}  order by ttnum".format(ttnum)
            cur.execute(qry)
            print("Record is deleted successfully.")
            con.commit()
            count = cur.rowcount
            print(count," record is deleted successfully.")

def search():
            print("Search a Record")
            ttnum = int(input("Enter Time Table Number:"))
            qry = "Select * from octimetable where ttnum = {}  order by ttnum".format(ttnum)
            cur.execute(qry)
            row = cur.fetchone()
            count = cur.rowcount
            print(count," record is searched successfully.")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| TTNumber | Class | Section  | Day       | Time  | Subject                 |")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| {0:<9d}| {1:<6s}| {2:<9s}| {3:<10s}| {4:<6s}| {5:<24s}|\
".format(row[0],row[1],row[2],row[3],row[4],row[5]))
            print("|----------|-------|----------|-----------|-------|-------------------------|")

def exit2():
    con.close()
    root.destroy()
    print("exiting...")
    sys.exit()
def exit1():
    root.destroy()
    print("exiting...")
    sys.exit()
def new():
    frm.destroy()

    Label(text="Menu",fg="black" ,font=("Ariel",25,"bold","italic")).place(x=330,y=25,anchor="center")
    Button(text="Insert",command=insert1,height=2,width=8).place(x=100,y=70)
    Button(text="Update",command=update,height=2,width=8).place(x=200,y=70)
    Button(text="Search",command=search,height=2,width=8).place(x=300,y=70)
    Button(text="Delete",command=delete,height=2,width=8).place(x=400,y=70)
    Button(text="Display",command=display,height=2,width=8).place(x=500,y=70)
    Button(text="Exit",command=exit2,height=2,width=8).place(x=300,y=150)
    
def connector():
    try:
        global cur,con
        con = mycon.connect(host='{}'.format(hostval.get()),user='{}'.format(userval.get()),passwd='{}'.format(pasval.get()))
                
        if con.is_connected():  
            print("Python is connected to MYSQL Successfully.")
            cur = con.cursor()  
            cur.execute("Create database if not exists onlineclass") 
            cur.execute("use onlineclass") 
            cur.execute("create table if not exists octimetable(ttnum int(5) primary key, clss char(5),\
        section char(5),day1 char(15),time1 char(10), subject char(25))")

            print("Input First Character Of Operation")
            new()        
    except:
        print("Python is not connected to MYSQL Successfully. Connection Failed.")
        sys.exit()


    

root=Tk()
root.geometry("700x300")
root.minsize(300,150)
root.maxsize(700,300)
root.title("Time Table Generator")

frm=LabelFrame(root)
frm.grid(pady=(120,10),padx=(0,20))

hname= Label(frm,text=" host name")
uname= Label(frm,text="username")
pas=Label(frm,text="password")

hname.grid(row=1,column=0)
uname.grid(row=2,column=0)
pas.grid(row=3,column=0)

hostval=StringVar()
userval=StringVar()
pasval=StringVar()

host= Entry(frm,textvariable=hostval)
user= Entry(frm,textvariable=userval)
password= Entry(frm,textvariable=pasval)

host.grid(row=1,column=1)
user.grid(row=2,column=1)
password.grid(row=3,column=1)

Button(frm,text="Enter",command=connector,bg="white",height=1,width=5).place(x=10,y=60)
Button(frm,text="Exit",command=exit1,bg="white",height=1,width=5).place(x=100,y=60)
Label(text="Time Table Generator",fg="black",font=("Ariel",25,"bold","italic")).place(x=370,y=25,anchor="center")
          
root.mainloop()

            


    
