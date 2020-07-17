import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')

# for in memory database
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE EMPLOYEES(
first text,
last text,
pay integer)""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?)", (emp.first, emp.last, emp.pay))


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM EMPLOYEES WHERE last=:last ", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE EMPLOYEES SET pay=:pay 
        WHERE first=:first and last=:last""", {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM EMPLOYEES WHERE
        first=:first AND last=:last""", {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Prins', 'John', 1234)
emp_2 = Employee('Hivk', 'John', 9000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('John')
print(emps)

update_pay(emp_1,10000)
remove_emp(emp_2)

emps = get_emps_by_name('John')
print(emps)

conn.close()
