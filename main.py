import mysql.connector  # 4/29, 5/2


class Database:
    def __init__(self, host, user, password, database):
        mydb = mysql.connector.connect(host=host, user=user, password=password)

        mycursor = mydb.cursor()
        mycursor.execute("DROP DATABASE IF EXISTS " + database)
        mycursor.execute("CREATE DATABASE " + database)

        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

    def createTable(self, name, attributes):
        table = self.mydb.cursor()
        table.execute("CREATE TABLE IF NOT EXISTS " + name + " (" + attributes + ")")
        return table

    def insert(self, table, sql, values):
        table.executemany(sql, values)
        self.mydb.commit()
        return table


def main():
    db = Database("localhost", "root", "P56?rN8C$fo?b?yR", "myDB")

    table = db.createTable("customers", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)")

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    values = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
    ]
    table = db.insert(table, sql, values)


if __name__ == '__main__':
    main()
