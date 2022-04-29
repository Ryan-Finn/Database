import cmd
from Database import Database


def parse(arg):
    return tuple(map(str, arg.split()))


class main(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.database = Database('test')

    def do_test(self, args):
        args = parse(args)
        print(args[0], args[1:len(args)])

    def do_insert(self, args):
        """insert [table] [data]
        Insert into [table] with [data]
        Tables & Data syntax and order:
            staff: first_name, last_name, sex (M, F, OTHER), birth_date (YYYY-MM-DD), hire_date (YYYY-MM-DD)
            customers: customer_no, first_name, last_name
            products: unit_price, quantity, locations ("a, b, c, etc.")
            shipments:
            orders: customer_no, products ("a, b, c, etc.")"""
        args = parse(args)
        self.database.insert(args[0], args[1:len(args)])
        print()

    def do_quit(self, _):
        """Close database connection and exit program"""
        self.database.close()
        return True


if __name__ == '__main__':
    main().cmdloop()

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
