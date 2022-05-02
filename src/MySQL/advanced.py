ADVANCED = dict()

ADVANCED["foo"] = (
    "SELECT * FROM customers WHERE customer_no = (\n"
    "    SELECT customer_no\n"
    "    FROM orders\n"
    "    WHERE products LIKE '%%%s%%'\n"
    ")"
)
