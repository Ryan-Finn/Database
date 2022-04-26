INSERTS = dict()

INSERTS['staff'] = (
    "INSERT INTO staff ("
    "    first_name, last_name, sex, birth_date, hire_date"
    ") VALUES (%(first_name)s, %(last_name)s, %(gender)s, %(birth_date)s, %(hire_date)s)")

INSERTS['customers'] = (
    "INSERT INTO customers ("
    "    customer_no, first_name, last_name"
    ") VALUES (%(customer_no)s, %(first_name)s, %(last_name)s)")

INSERTS['products'] = (
    "INSERT INTO products ("
    "    unit_price, quantity, locations"
    ") VALUES (%(unit_price)s, %(quantity)s, %(locations)s)")

INSERTS['shipments'] = (
    "INSERT INTO shipments () VALUES ()")

INSERTS['orders'] = (
    "INSERT INTO orders ("
    "    customer_no, products"
    ") VALUES (%(customer_no)s, %(products)s)")
