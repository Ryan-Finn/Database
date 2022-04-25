import mysql.connector
from tables import TABLES
from inserts import INSERTS
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

DB_NAME = 'test'
config = {
    'user': 'root',
    'password': 'P56?rN8C$fo?b?yR',
    'host': 'localhost',
    'database': DB_NAME,
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

data_employee = {
    'first_name': 'Geert',
    'last_name': 'Vanderkelen',
    'hire_date': date(1999, 6, 14),
    'gender': 'M',
    'birth_date': date(1977, 6, 14),
}

# Insert new employee
cursor.execute(INSERTS['employees'], data_employee)
emp_no = cursor.lastrowid
tomorrow = datetime.now().date() + timedelta(days=1)

# Insert salary information
data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
}
cursor.execute(INSERTS['salaries'], data_salary)

# Make sure data is committed to the database
cnx.commit()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = date(1999, 1, 1)
hire_end = date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

cursor.close()
cnx.close()
