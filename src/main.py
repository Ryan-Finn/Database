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
    __help = (
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
            self.newline = True

    # QUERIES
    def do_query(self, args):
        """      query <table> <selection> <conditions>"""
        args = parse(args)
        self.database.query(args[0], args[1: len(args)])

    def do_getCustomersOfProduct(self, args):
        """      getCustomersOfProduct <product_no>"""
        args = parse(args)
        self.database.advanced("getCustomersOfProduct", args)

    def do_getCustomersOfShipment(self, args):
        """      getCustomersOfShipment <shipment_no>"""
        args = parse(args)
        self.database.advanced("getCustomersOfShipment", args)

    def do_getShipmentsOfCustomer(self, args):
        """      getShipmentsOfCustomer <customer_no>"""
        args = parse(args)
        self.database.advanced("getShipmentsOfCustomer", args)

    def do_getShipmentsOfProduct(self, args):
        """      getShipmentsOfProduct <product_no>"""
        args = parse(args)
        self.database.advanced("getShipmentsOfProduct", args)

    def do_getUnshippedOrders(self, _):
        """      getUnshippedOrders"""
        self.database.advanced("getUnshippedOrders", ())

    def do_getShippedOrders(self, _):
        """      getShippedOrders"""
        self.database.advanced("getShippedOrders", ())

    def do_getDeliveredOrders(self, _):
        """      getDeliveredOrders"""
        self.database.advanced("getDeliveredOrders", ())

    # INSERTS
    def do_newStaff(self, args):
        """      newStaff <first_name> <last_name> <sex> <birth_date>"""
        args = list(parse(args))
        for i in range(len(args)):
            args[i] = f"'{args[i]}'"
        self.database.insert("staff", tuple(args))

    def do_newCustomer(self, args):
        """      newCustomer <first_name> <last_name>"""
        args = parse(args)
        self.database.insert("customers", (f"'{args[0]}'", f"'{args[1]}'"))

    def do_newProduct(self, args):
        """      newProduct <unit_price> <quantity> <locations>"""
        args = parse(args)
        self.database.insert("products", (args[0], args[1], f"'{args[2]}'"))

    def do_newLocation(self, args):
        """      newLocation <product_no> <location>"""
        args = parse(args)
        self.database.advanced("newLocation", (f"',{args[1]}'", args[0]))

    def do_newShipment(self, _):
        """      newShipment"""
        self.database.insert("shipments", ())

    def do_newOrder(self, args):
        """      newOrder <customer_no> <products>"""
        args = parse(args)
        self.database.insert("orders", (args[0], f"'{args[1]}'"))

    # UPDATES
    def do_updateFirstName(self, args):
        """      updateFirstName <staff_no> <new_first_name>"""
        args = parse(args)
        self.database.update(
            "staff", (f"first_name = '{args[1]}'", f"staff_no = '{args[0]}'"))

    def do_updateLastName(self, args):
        """      updateLastName <staff_no> <new_last_name>"""
        args = parse(args)
        self.database.update(
            "staff", (f"last_name = '{args[1]}'", f"staff_no = '{args[0]}'"))

    def do_updateSex(self, args):
        """      updateSex <staff_no> <new_sex>"""
        args = parse(args)
        self.database.update(
            "staff", (f"sex = '{args[1]}'", f"staff_no = '{args[0]}'"))

    def do_updateProductPrice(self, args):
        """      updateProductPrice <product_no> <new_unit_price>"""
        args = parse(args)
        self.database.update(
            "products", (f"unit_price = {args[1]}", f"product_no = '{args[0]}'"))

    def do_updateProductQuantity(self, args):
        """      updateProductQuantity <product_no> <new_quantity>"""
        args = parse(args)
        self.database.update(
            "products", (f"quantity = {args[1]}", f"product_no = '{args[0]}'"))

    def do_updateShipmentStatus(self, args):
        """      updateShipmentStatus <shipment_no> <new_status>"""
        args = parse(args)
        self.database.update(
            "shipments", (f"status = '{args[1]}'", f"shipment_no = {args[0]}"))

    def do_updateOrderShipment(self, args):
        """      updateOrderShipment <order_no> <new_shipment_no>"""
        args = parse(args)
        self.database.update(
            "orders", (f"shipment_no = {args[1]}", f"order_no = '{args[0]}'"))

    # DELETES
    def do_removeLocation(self, args):
        """      removeLocation <product_no> <location>"""
        args = parse(args)
        locs = self.database.query(
            "products", ("locations", f"product_no = {args[0]}"))
        locs = locs[0][0].split(",")
        locs.remove(args[1])
        self.database.update(
            "products", (f"locations = '{','.join(locs)}'", f"product_no = {args[0]}"))

    def do_help(self, args):
        if args == "":
            print(self.__help)
        super().do_help(args)

    def do_quit(self, _):
        self.database.close()
        return True

    def postcmd(self, stop, line):
        if self.newline:
            print()
        return super().postcmd(stop, line)


if __name__ == "__main__":
    main().cmdloop()
