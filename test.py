import mysql.connector
from tables import TABLES
from inserts import INSERTS
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


class Database:
    def __init__(self, database_name):
        config = {
            'user': 'root',
            'password': 'P56?rN8C$fo?b?yR',
            'host': '127.0.0.1',
            'raise_on_warnings': True,
        }

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute("DROP DATABASE IF EXISTS {}".format(database_name))

        try:
            cursor.execute("USE {}".format(database_name))
        except mysql.connector.Error as err:
            print("Database {} does not exist.".format(database_name))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                try:
                    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8MB4'".format(database_name))
                    print("Database {} created successfully.".format(database_name))
                    cnx.database = database_name
                except mysql.connector.Error as err:
                    print("Failed creating database: {}".format(err))
                    exit(1)
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

        self.cnx = cnx
        self.cursor = cursor

    def insert(self, table_name, data):
        self.cursor.execute(INSERTS[table_name], data)
        self.cnx.commit()
        return self.cursor.lastrowid

    def query(self, statement, args):
        self.cursor.execute(statement, args)
        results = []
        for row in self.cursor:
            results.append(row)
        return results

    def close(self):
        self.cursor.close()
        self.cnx.close()


database = Database('test')

data_employee = {
    'first_name': 'Geert',
    'last_name': 'Vanderkelen',
    'hire_date': date(1999, 6, 14),
    'gender': 'M',
    'birth_date': date(1977, 6, 14),
}
emp_no = database.insert('employees', data_employee)

tomorrow = datetime.now().date() + timedelta(days=1)
data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
}
database.insert('salaries', data_salary)

hire_start = date(1999, 1, 1)
hire_end = date(1999, 12, 31)
query = ("SELECT emp_no, first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")
results = database.query(query, (hire_start, hire_end))

for (emp_no, first_name, last_name, hire_date) in results:
    print("{}: {}, {} was hired on {:%d %b %Y}".format(emp_no, last_name, first_name, hire_date))

database.close()
