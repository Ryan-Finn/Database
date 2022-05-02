import cmd
import re

from Database import Database


def parse(args):
    args = re.sub(r" *, *", ",", args)
    args = re.sub(r" *= *", "=", args)
    args = args.replace(" ", "#").replace(",", ", ").replace("=", " = ")
    return tuple(args.split("#"))


class main(cmd.Cmd):
    intro = "Type `help` for more information.\nType `quit` to exit the program.\n"

    def __init__(self):
        super().__init__()
        self.database = Database("test")

    def do_getCustomersOfProduct(self, args):
        args = parse(args)
        self.database.advanced("foo", args)

    def do_getShipmentsForCustomer(self, args):
        args = parse(args)
        self.database.advanced("foo", args)

    def do_help(self, args):
        string = (
            "Database tables:\n"
            "================\n"
            "  staff:      staff_no, first_name, last_name, sex, birth_date, hire_date\n"
            "  customers:  customer_no, first_name, last_name\n"
            "  products:   product_no, unit_price, quantity, locations\n"
            "  shipments:  shipment_no, status, shipment_date, delivery_date\n"
            "  orders:     order_no, shipment_no, customer_no, order_date, products\n"
            "\nAttribute formats:\n"
            "==================\n"
            "  staff_no, product_no, shipment_no, order_no: set automatically\n"
            "  birth_date, hire_date, ship_date, delivery_date, order_date: YYYY-MM-DD\n"
            "  sex:                    M, F, or OTHER\n"
            "  status:                 PROCESSING, IN-TRANSIT, or DELIVERED\n"
            '  locations, products:    "a, b, c, etc."\n'
            "\nExamples:\n"
            "=========\n"
            "  Inserting:  insert staff Ryan Finn M 1998-10-01 2022-05-06\n"
            "  Updating:   update staff first_name=Bryan staff_no=1\n"
            "  Deleting:   delete staff 3\n"
            "  Querying:   query staff first_name, last_name, birth_date sex = F"
        )
        print(string)
        super().do_help(args)

    def do_insert(self, args):
        """insert [table] [data]
        Example: insert staff 'Ryan' 'Finn' M 1998-10-01 2022-05-06"""
        args = parse(args)
        self.database.insert(args[0], args[1: len(args)])

    def do_update(self, args):
        """update [table] [set] [where]
        Example: update staff first_name=Bryan staff_no=1"""
        args = parse(args)
        self.database.update(args[0], args[1: len(args)])

    def do_delete(self, args):
        """delete [table] [data]
        Delete [data] from [table]"""
        args = parse(args)
        self.database.delete(args[0], args[1: len(args)])

    def do_query(self, args):
        """query [table] [select] [where]
        Query [select] from [table] where [where]"""
        args = parse(args)
        self.database.query(args[0], args[1: len(args)])

    def do_quit(self, _):
        """Close database connection and exit program"""
        self.database.close()
        return True

    def postcmd(self, stop, line):
        print()
        return super().postcmd(stop, line)


if __name__ == "__main__":
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
