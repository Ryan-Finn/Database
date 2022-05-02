INSERTS = dict()

INSERTS["staff"] = (
    "INSERT INTO staff ("
    "first_name, last_name, sex, birth_date"
    ") VALUES (%s, %s, %s, %s);"
)

INSERTS["customers"] = (
    "INSERT INTO customers ("
    "first_name, last_name"
    ") VALUES (%s, %s);"
)

INSERTS["products"] = (
    "INSERT INTO products (" "unit_price, quantity, locations" ") VALUES (%s, %s, %s);"
)

INSERTS["shipments"] = "INSERT INTO shipments (shipment_no) VALUES (NULL);"

INSERTS["orders"] = "INSERT INTO orders (" "customer_no, products" ") VALUES (%s, %s);"
