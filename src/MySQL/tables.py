TABLES = dict()

TABLES["staff"] = (
    "CREATE TABLE staff ("
    "    staff_no TINYINT NOT NULL AUTO_INCREMENT,"
    "    first_name VARCHAR(16) NOT NULL,"
    "    last_name VARCHAR(16) NOT NULL,"
    "    sex ENUM('F', 'M', 'OTHER') NOT NULL,"
    "    birth_date DATE NOT NULL,"
    "    hire_date DATE NOT NULL,"
    "    PRIMARY KEY (staff_no)"
    ")"
)

TABLES["customers"] = (
    "CREATE TABLE customers ("
    "    customer_no MEDIUMINT NOT NULL AUTO_INCREMENT,"
    "    first_name VARCHAR(16) NOT NULL,"
    "    last_name VARCHAR(16) NOT NULL,"
    "    PRIMARY KEY (customer_no)"
    ")"
)

TABLES["products"] = (
    "CREATE TABLE products ("
    "    product_no SMALLINT NOT NULL AUTO_INCREMENT,"
    "    unit_price DOUBLE NOT NULL,"
    "    quantity SMALLINT NOT NULL,"
    "    locations TINYTEXT NOT NULL,"
    "    PRIMARY KEY (product_no)"
    ")"
)

TABLES["shipments"] = (
    "CREATE TABLE shipments ("
    "    shipment_no INT NOT NULL AUTO_INCREMENT,"
    "    status ENUM('PROCESSING', 'IN-TRANSIT', 'DELIVERED') NOT NULL,"
    "    shipment_date DATETIME,"
    "    delivery_date DATETIME,"
    "    PRIMARY KEY (shipment_no)"
    ")"
)

TABLES["orders"] = (
    "CREATE TABLE orders ("
    "    order_no INT NOT NULL AUTO_INCREMENT,"
    "    shipment_no INT DEFAULT 1,"
    "    customer_no MEDIUMINT NOT NULL,"
    "    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,"
    "    products TEXT NOT NULL,"
    "    PRIMARY KEY (order_no)"
    # "    KEY shipment_no (shipment_no),"
    # "    KEY customer_no (customer_no),"
    ")"
)

# i = 'warehouses'
# TABLES[i] = (
#     "CREATE TABLE {} ("
#     "    ware_no char(4) NOT NULL,"
#     "    ware_name varchar(40) NOT NULL,"
#     "    address varchar(40) NOT NULL,"
#     "    PRIMARY KEY (ware_no), UNIQUE KEY address (address)"
#     ")".format(i))
#
# i = 'dept_emp'
# TABLES[i] = (
#     "CREATE TABLE {} ("
#     "    emp_no int NOT NULL,"
#     "    dept_no char(4) NOT NULL,"
#     "    from_date date NOT NULL,"
#     "    to_date date NOT NULL,"
#     "    PRIMARY KEY (emp_no,dept_no), KEY emp_no (emp_no),"
#     "    KEY dept_no (dept_no),"
#     "    CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY (emp_no) "
#     "       REFERENCES employees (emp_no) ON DELETE CASCADE,"
#     "    CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY (dept_no) "
#     "       REFERENCES departments (dept_no) ON DELETE CASCADE"
#     ")".format(i))
#
# i = 'dept_manager'
# TABLES[i] = (
#     "CREATE TABLE {} ("
#     "    emp_no int NOT NULL,"
#     "    dept_no char(4) NOT NULL,"
#     "    from_date date NOT NULL,"
#     "    to_date date NOT NULL,"
#     "    PRIMARY KEY (emp_no,dept_no),"
#     "    KEY emp_no (emp_no),"
#     "    KEY dept_no (dept_no),"
#     "    CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY (emp_no) "
#     "       REFERENCES employees (emp_no) ON DELETE CASCADE,"
#     "    CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY (dept_no) "
#     "       REFERENCES departments (dept_no) ON DELETE CASCADE"
#     ")".format(i))
#
# i = 'titles'
# TABLES[i] = (
#     "CREATE TABLE {} ("
#     "    emp_no int NOT NULL,"
#     "    title varchar(50) NOT NULL,"
#     "    from_date date NOT NULL,"
#     "    to_date date DEFAULT NULL,"
#     "    PRIMARY KEY (emp_no,title,from_date), KEY emp_no (emp_no),"
#     "    CONSTRAINT titles_ibfk_1 FOREIGN KEY (emp_no)"
#     "       REFERENCES employees (emp_no) ON DELETE CASCADE"
#     ")".format(i))
