from Database import Database
from datetime import date, datetime, timedelta


database = Database('test')

# data_employee = {
#     'first_name': 'Geert',
#     'last_name': 'Vanderkelen',
#     'hire_date': date(1999, 6, 14),
#     'gender': 'M',
#     'birth_date': date(1977, 6, 14),
# }
# emp_no = database.insert('employees', data_employee)
#
# tomorrow = datetime.now().date() + timedelta(days=1)
# data_salary = {
#     'emp_no': emp_no,
#     'salary': 50000,
#     'from_date': tomorrow,
#     'to_date': date(9999, 1, 1),
# }
# database.insert('salaries', data_salary)
#
# hire_start = date(1999, 1, 1)
# hire_end = date(1999, 12, 31)
# query = ("SELECT emp_no, first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")
# results = database.query(query, (hire_start, hire_end))
#
# for (emp_no, first_name, last_name, hire_date) in results:
#     print("{}: {}, {} was hired on {:%d %b %Y}".format(emp_no, last_name, first_name, hire_date))

database.close()
