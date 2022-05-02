TABLES = dict()

TABLES["staff"] = (
    "CREATE TABLE staff ("
    "    staff_no TINYINT NOT NULL AUTO_INCREMENT,"
    "    first_name VARCHAR(16) NOT NULL,"
    "    last_name VARCHAR(16) NOT NULL,"
    "    sex ENUM('F', 'M', 'OTHER') NOT NULL,"
    "    birth_date DATE NOT NULL,"
    "    hire_date DATE DEFAULT (CURRENT_DATE),"
    "    PRIMARY KEY (staff_no)"
    ");"
)

TABLES["customers"] = (
    "CREATE TABLE customers ("
    "    customer_no MEDIUMINT NOT NULL AUTO_INCREMENT,"
    "    first_name VARCHAR(16) NOT NULL,"
    "    last_name VARCHAR(16) NOT NULL,"
    "    PRIMARY KEY (customer_no)"
    ");"
)

TABLES["products"] = (
    "CREATE TABLE products ("
    "    product_no SMALLINT NOT NULL AUTO_INCREMENT,"
    "    unit_price DOUBLE NOT NULL,"
    "    quantity SMALLINT NOT NULL,"
    "    locations TINYTEXT NOT NULL,"
    "    PRIMARY KEY (product_no)"
    ");"
)

TABLES["shipments"] = (
    "CREATE TABLE shipments ("
    "    shipment_no INT NOT NULL AUTO_INCREMENT,"
    "    status ENUM('PROCESSING', 'IN-TRANSIT', 'DELIVERED') NOT NULL,"
    "    shipment_date DATETIME,"
    "    delivery_date DATETIME,"
    "    PRIMARY KEY (shipment_no)"
    ");"
)

TABLES["orders"] = (
    "CREATE TABLE orders ("
    "    order_no INT NOT NULL AUTO_INCREMENT,"
    "    shipment_no INT DEFAULT 1,"
    "    customer_no MEDIUMINT NOT NULL,"
    "    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,"
    "    products TEXT NOT NULL,"
    "    PRIMARY KEY (order_no)"
    ");"
)
