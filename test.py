import cmd
from Database import Database


def parse(arg):
    return tuple(map(str, arg.split()))


class main(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.database = Database('test')

    def do_help(self, args):
        string = "\
        Tables:\n\
            staff:      staff_no, first_name, last_name, sex, birth_date, hire_date\n\
            customers:  customer_no, first_name, last_name\n\
            products:   product_no, unit_price, quantity, locations\n\
            shipments:  shipment_no, status, shipment_date, delivery_date\n\
            orders:     order_no, shipment_no, customer_no, order_date, products\n\
        Attributes:\n\
            birth_date, hire_date, ship_date, delivery_date, order_date: YYYY-MM-DD\n\
            sex:                    M, F, or OTHER\n\
            status:                 PROCESSING, IN-TRANSIT, or DELIVERED\n\
            locations, products:    'a, b, c, etc.'\n\
        Examples:\n\
            Inserting:  insert staff 'Ryan' 'Finn' M 1998-10-01 2022-05-06\n\
            Updating:   update staff 'first_name = Not Ryan' 'staff_no = 1'\n\
            Deleting:   delete staff 3\n\
            Querying:   query staff\
        "
        print(string)
        super().do_help(args)

    def do_insert(self, args):
        """insert [table] [data]
        Insert [data] into [table]"""
        args = parse(args)
        print("Inserted into row ", self.database.insert(args[0], args[1:len(args)]))
        print()

    def do_update(self, args):
        """update [table] [set] [where]
        Update [table] by setting [set] where [where]"""
        args = parse(args)
        self.database.update(args[0], args[1:len(args)])
        print()

    def do_delete(self, args):
        """delete [table] [data]
        Delete [data] from [table]"""
        args = parse(args)
        self.database.delete(args[0], args[1:len(args)])
        print()

    def do_query(self, args):
        """query [table] [select] [where] [between]
        Query [select] from [table] where [where] between [between]"""
        args = parse(args)
        self.database.query(args[0], args[1:len(args)])
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
