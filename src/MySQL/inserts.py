INSERTS = dict()

INSERTS["staff"] = (
    "INSERT INTO staff (\n"
    "    first_name, last_name, sex, birth_date\n"
    ") VALUES (%s, %s, %s, %s);"
)

INSERTS["customers"] = (
    "INSERT INTO customers (\n"
    "    first_name, last_name"
    ") VALUES (%s, %s);"
)

INSERTS["products"] = (
    "INSERT INTO products (\n"
    "    unit_price, quantity, locations\n"
    ") VALUES (%s, %s, %s);"
)

INSERTS["shipments"] = "INSERT INTO shipments (shipment_no) VALUES (NULL);"

INSERTS["orders"] = (
    "INSERT INTO orders (\n"
    "    customer_no, products\n"
    ") VALUES (%s, %s);")
