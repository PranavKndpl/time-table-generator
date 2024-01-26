import mysql.connector as mycon #import mysql.connector package
import sys

hname = input("Enter MySQL Host Name (Default value is localhost) ")
portno = input("Enter MySQL Port Number (Default value is 3306) ")
uname = input("Enter MySQL User Name (Default value is root) ")
pwd = input("Enter MySQL Password (Default value is root for user root) ")
con = mycon.connect(host='{}'.format(hname),port='{}'.format(portno),user='{}'.format(uname),\
                    passwd='{}'.format(pwd)) #New style of Text Formatting is used 
if con.is_connected():  #True if connected otherwise False
    print("Python is connected to MYSQL Successfully.")
    cur = con.cursor()  #Creating Cursor
    cur.execute("Create database if not exists onlineclass") #Creating Database
    cur.execute("use onlineclass") #Using Database
    cur.execute("create table if not exists octimetable(ttnum int(5) primary key, clss char(5),\
section char(5),day1 char(15),time1 char(10), subject char(25))")   #Creating Table
    while True: #Infinite Loop
        print("\nCreate Retrive Update Delete (CRUD) OPERATION.\
\nInput First Character of Operation.\n")
        print("Insertion  Retreival  Updation  Deletion  Searching  Exit\n")
        inp = input("Enter Your Choice ").upper()
        if inp == 'I':
            print("Inserting a Record")
            ttnum = int(input("Enter Time Table Number "))
            clss = input("Enter Time Table Class (in Roman) ")
            section = input("Enter Time Table Section ")
            day1 = input("Enter Time Table Day ")
            time1 = input("Enter Time Table Time (HH:MM) ")
            subject = input("Enter Time Table Subject ")
            qry = "insert into octimetable (ttnum,clss,section,day1,time1,subject) values \
({},'{}','{}','{}','{}','{}')".format(ttnum,clss,section,day1,time1,subject)    #Inserting Record
            cur.execute(qry)
            con.commit()
            count = cur.rowcount
            print(count," record is inserted successfully.")
            print("Press Enter to continue.")
            input()
        elif inp == 'R':
            print("Retrieve a Record")
            qry = "Select * from octimetable order by ttnum"   #Accessing Records
            cur.execute(qry)
            data = cur.fetchall()
            count = cur.rowcount
            print(count," records are retrived successfully.")
            #New concept of Text formatting is used to display data in Tabular Form
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("| TTNumber | Class | Section  | Day       | Time  | Subject                 |")
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            for row in data:
                print("| {0:<9d}| {1:<6s}| {2:<9s}| {3:<10s}| {4:<6s}| {5:<24s}|\
".format(row[0],row[1],row[2],row[3],row[4],row[5]))
            print("|----------|-------|----------|-----------|-------|-------------------------|")
            print("Press Enter to continue.")
            input()
        elif inp == 'U':
            print("Update a Record")
            ttnum = int(input("Enter Time Table Number "))
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
            clss = input("Enter Time Table Class (New) or . old value ")
            section = input("Enter Time Table Section (New) or . old value ")
            day1 = input("Enter Time Table Day (New) or . old value ")
            time1 = input("Enter Time Table Time (New) or . old value ")
            subject = input("Enter Time Table Subject (New) or . old value ")
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
            print("Press Enter to continue.")
            input()
        elif inp == 'D':
            print("Delete a Record")
            ttnum = int(input("Enter Time Table Number "))
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
            print("Press Enter to continue.")
            input()
        elif inp == 'S':
            print("Search a Record")
            ttnum = int(input("Enter Time Table Number "))
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
            print("Press Enter to continue.")
            input()
        elif inp == 'E':
            con.close()
            print("Terminating Program")
            sys.exit(0)
        else:
            print("Wrong Input Try Again")
            print("Press Enter to continue.")
            input()
else:
    print("Python is not connected to MYSQL Successfully. Connection Failed.")
    sys.exit()
