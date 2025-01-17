import mysql.connector as conn
mydb=conn.connect(
    host="localhost",  # local host: same machine
    user="root",
    password="1234",
    database="cvr"
)
mycursor = mydb.cursor()
mycursor.execute("create table emp(empid int, ename varchar(20), city varchar(20), sal int)")

# manual inputs to insert data into tables
name = input("Enter name: ")
id = input("Enter id: ")
city = input("Enter city: ")
sal = input("Enter salary: ")
mycursor.execute("insert into emp values(%s,%s,%s,%s)", (id, name,city,sal))

# delete employee details manually by id 
id=input("Enter id to be deleted: ")
mycursor.execute("delete from emp where empid = %s",(id,)) #delete

#update details of employees manually
name = input("Enter name updated: ")
id = input("Enter id updated: ")
city = input("Enter city updated: ")
sal = input("Enter salary updated: ")
mycursor.execute("UPDATE emp SET ename = %s, city =  %s, sal =%s WHERE empid = %s", (name,city,sal,id)) #update details

#display all details
print("\nDisplaying all the details")
mycursor.execute("select * from emp ")
employees = mycursor.fetchall()
for employee in employees:
    print(employee)

#display in asc order
print("\nDetails in asc order by name")
mycursor.execute("select * from emp order by ename ")
employees = mycursor.fetchall()
for employee in employees:
    print(employee)

# print Details of employees earning greater than 50k and less than 70k
print("\nDetails of employees earning greater than 50k and less than 70k")
mycursor.execute("select * from emp where sal > 50000 and sal < 70000")
employees = mycursor.fetchall()
for employee in employees:
    print(employee)

# display details of employees whose city is Los Angeles
print("\nDetails of employees whose city is Los Angeles")
mycursor.execute("select * from emp where city='Los Angeles'")
employees = mycursor.fetchall()
for employee in employees:
    print(employee)
mydb.commit()
