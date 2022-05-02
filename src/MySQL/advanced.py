ADVANCED = dict()

ADVANCED["getCustomersOfProduct"] = (
    "SELECT c.*\n"
    "FROM customers c JOIN orders o USING (customer_no)\n"
    "WHERE products LIKE '%%%s%%'\n"
    "GROUP BY customer_no;\n"
)

ADVANCED["getCustomersOfShipment"] = (
    "SELECT c.*\n"
    "FROM customers c JOIN orders o USING (customer_no)\n"
    "WHERE shipment_no = %s\n"
    "GROUP BY customer_no;\n"
)

ADVANCED["getShipmentsOfCustomer"] = (
    "SELECT s.*\n"
    "FROM shipments s JOIN orders o USING (shipment_no)\n"
    "WHERE customer_no = %s\n"
    "GROUP BY shipment_no;\n"
)

ADVANCED["getShipmentsOfProduct"] = (
    "SELECT s.*\n"
    "FROM shipments s JOIN orders o USING (shipment_no)\n"
    "WHERE products LIKE '%%%s%%'\n"
    "GROUP BY shipment_no;\n"
)

ADVANCED["getUnshippedOrders"] = (
    "SELECT o.*\n"
    "FROM shipments s JOIN orders o USING (shipment_no)\n"
    "WHERE status = 'PROCESSING'\n"
    "GROUP BY order_no;\n"
)

ADVANCED["getShippedOrders"] = (
    "SELECT o.*\n"
    "FROM shipments s JOIN orders o USING (shipment_no)\n"
    "WHERE status = 'IN-TRANSIT'\n"
    "GROUP BY order_no;\n"
)

ADVANCED["getDeliveredOrders"] = (
    "SELECT o.*\n"
    "FROM shipments s JOIN orders o USING (shipment_no)\n"
    "WHERE status = 'DELIVERED'\n"
    "GROUP BY order_no;\n"
)

ADVANCED["newLocation"] = (
    "UPDATE products SET locations = CONCAT(locations, %s) WHERE product_no = %s;"
)
