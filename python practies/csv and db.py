import csv
import sqlite3 as sql
'''with open("emp5.csv","w",newline="") as f:
         w=csv.writer(f)
         w.writerow(["ENO","ENAME","ESAL","EADDR"])
         n = int(input("Enter Number of Employees:"))
         for i in range(n):
                  eno = int(input("enter employee No:"))
                  ename = input("enter employee ename:")
                  esal = float(input("enter employee salary:"))
                  eaddr = input("enter employee address:")
                  w.writerow([eno,ename,esal,eaddr])'''
print("Total Employees data written to csv file successfully")

f = open("emp5.csv","r")
r = csv.reader(f)
data = list(r)
data.pop(0)


conn = sql.connect("csv_database.db")
conn.execute(""" CREATE TABLE if not exists emp5
                           (ID INT  PRIMARY KEY NOT NULL,
                            NAME    TEXT        NOT NULL,
                            SALARY  REAL,
                            ADDRESS REAL);""")


conn.executemany("INSERT INTO emp5 VALUES(?,?,?,?)",data)
conn.commit()


info = conn.execute("SELECT *from emp5")
for row in info:
         print("ID = ", row[0])
         print("NAME= ", row[1])
         print("SAL = ", row[2])
         print("ADDRESS = ",row[3])


conn.close()
