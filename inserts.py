INSERTS = dict()

INSERTS['employees'] = (
    "INSERT INTO employees ("
    "    first_name, last_name, hire_date, gender, birth_date"
    ") VALUES (%(first_name)s, %(last_name)s, %(hire_date)s, %(gender)s, %(birth_date)s)")

INSERTS['departments'] = (
    "INSERT INTO employees ("
    "    dept_name"
    ") VALUES (%(dept_name)s)")

INSERTS['salaries'] = (
    "INSERT INTO employees ("
    "    emp_no, salary, from_date, to_date"
    ") VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

INSERTS['dept_emp'] = (
    "INSERT INTO employees ("
    "    first_name, last_name, hire_date, gender, birth_date"
    ") VALUES (%s, %s, %s, %s, %s)")

INSERTS['dept_manager'] = (
    "INSERT INTO employees ("
    "    first_name, last_name, hire_date, gender, birth_date"
    ") VALUES (%s, %s, %s, %s, %s)")

INSERTS['titles'] = (
    "INSERT INTO employees ("
    "    first_name, last_name, hire_date, gender, birth_date"
    ") VALUES (%s, %s, %s, %s, %s)")
