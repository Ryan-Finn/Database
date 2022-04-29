import mysql.connector
from mysql.connector import errorcode
from csv import DictReader
from tables import TABLES
from inserts import INSERTS
from updates import UPDATES


# noinspection PyUnboundLocalVariable
class Database:
    def __init__(self, database_name):
        config = {
            'user': 'root',
            'password': 'P56?rN8C$fo?b?yR',
            'host': '127.0.0.1',
            'raise_on_warnings': True,
        }

        print("\nCONNECTING TO DATABASE...")

        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
        except mysql.connector.Error as err:
            print("  Could not connect to database `{}`.".format(database_name))
            print("    ", err, "\n")
            exit(1)

        try:
            cursor.execute("DROP DATABASE IF EXISTS {}".format(database_name))
            cursor.execute("USE {}".format(database_name))
        except mysql.connector.Error as err:
            print("  Database `{}` does not exist.".format(database_name))
            if err.errno == errorcode.ER_DB_DROP_EXISTS or err.errno == errorcode.ER_BAD_DB_ERROR:
                self.__createDatabase(cursor, cnx, database_name)
                self.__createTables(cursor)
            else:
                print("    ", err, "\n")
                self.close()
                exit(1)
        print()
        self.cnx = cnx
        self.cursor = cursor

    def __createDatabase(self, cursor, cnx, database_name):
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8MB4'".format(database_name))
            print("  Database `{}` created successfully.".format(database_name))
            cnx.database = database_name
        except mysql.connector.Error as err:
            print("  Database `{}` creation failed.".format(database_name))
            print("    ", err, "\n")
            self.close()
            exit(1)

    @staticmethod
    def __createTables(cursor):
        for table_name in TABLES:
            try:
                cursor.execute(TABLES[table_name])
                with open('Initializations/' + table_name + '.csv') as file:
                    for line in DictReader(file):
                        cursor.execute(INSERTS[table_name], line)
                print("    Table `{}` created successfully.".format(table_name))
            except mysql.connector.Error as err:
                print("    Table `{}` creation failed.".format(table_name))
                print("      ", err)

    def insert(self, table_name, data):
        try:
            self.cursor.execute(INSERTS[table_name], data)
            self.cnx.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(err)
            return -1

    def update(self, table_name, data):
        try:
            self.cursor.execute(UPDATES[table_name], data)
            self.cnx.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(err)
            return

    def delete(self, table_name, data):
        return

    def query(self, statement, args):
        try:
            self.cursor.execute(statement, args)
        except mysql.connector.Error as err:
            print(err)
            return []

        results = []
        for row in self.cursor:
            results.append(row)
        return results

    def close(self):
        self.cursor.close()
        self.cnx.close()
