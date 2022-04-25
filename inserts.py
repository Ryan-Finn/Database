INSERTS = dict()

i = 'employees'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    first_name, last_name, hire_date, gender, birth_date"
    ") VALUES (%(first_name)s, %(last_name)s, %(hire_date)s, %(gender)s, %(birth_date)s)".format(i))

i = 'departments'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    dept_no, dept_name"
    ") VALUES (%(dept_no)s, %(dept_name)s)".format(i))

i = 'salaries'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    emp_no, salary, from_date, to_date"
    ") VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)".format(i))

i = 'dept_emp'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    emp_no, dept_no, from_date, to_date"
    ") VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)".format(i))

i = 'dept_manager'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    emp_no, dept_no, from_date, to_date"
    ") VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)".format(i))

i = 'titles'
INSERTS[i] = (
    "INSERT INTO {} ("
    "    emp_no, title, from_date, to_date"
    ") VALUES (%(emp_no)s, %(title)s, %(from_date)s, %(to_date)s)".format(i))
