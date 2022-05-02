import re
from cmd import Cmd

from Database import Database


def parse(args):
    args = re.sub(r" *, *", ",", args)
    args = re.sub(r" *= *", "=", args)
    args = args.replace(" ", "#").replace(",", ", ").replace("=", " = ")
    return tuple(args.split("#"))


class main(Cmd):
    prompt = "\nHost: "

    def __init__(self):
        super().__init__()
        self.newline = False
        self.config = {"raise_on_warnings": True}
        self.database = None

    def default(self, args):
        args = parse(args)
        if self.prompt == "\nHost: ":
            self.prompt = "Username: "
            self.config["host"] = args[0]
        elif self.prompt == "Username: ":
            self.prompt = "Password: "
            self.config["user"] = args[0]
        elif self.prompt == "Password: ":
            self.prompt = "Schema: "
            self.config["password"] = args[0]
        elif self.prompt == "Schema: ":
            self.prompt = "cmd>> "
            self.database = Database(args[0], self.config)
            print("Type `help` for more information.\nType `quit` to exit the program.\n")
        elif self.prompt == "cmd>> ":
            self.newline = True

    def do_getCustomersOfProduct(self, args):
        args = parse(args)
        self.database.advanced("foo", args)

    def do_getShipmentsForCustomer(self, args):
        args = parse(args)
        self.database.advanced("foo", args)

    def do_help(self, args):
        string = (
            "\nDatabase tables:\n"
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
            "  locations, products:    \"a, b, c, etc.\""
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
        if self.newline:
            print()
        return super().postcmd(stop, line)


if __name__ == "__main__":
    main().cmdloop()
