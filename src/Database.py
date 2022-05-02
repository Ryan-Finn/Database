from csv import reader

import mysql.connector
from MySQL.advanced import ADVANCED
from mysql.connector import errorcode
from MySQL.inserts import INSERTS
from MySQL.queries import QUERIES
from MySQL.tables import TABLES
from MySQL.triggers import TRIGGERS
from MySQL.updates import UPDATES


# noinspection PyUnboundLocalVariable
class Database:
    def __init__(self, database_name, config):
        self.__database_name = database_name

        # config = {
        #     "user": "root",
        #     "password": "P56?rN8C$fo?b?yR",
        #     "host": "127.0.0.1",
        #     "raise_on_warnings": True,
        # }

        print("\nOPENING CONNECTION...")

        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
        except mysql.connector.Error as err:
            print(f"  Could not connect to database `{database_name}`.")
            print(f"    {err}\n")
            exit(1)

        try:
            cursor.execute(f"USE {database_name}")
            print("CONNECTED TO DATABASE")
        except mysql.connector.Error as err:
            print(f"  Database `{database_name}` does not exist.")
            if (
                err.errno == errorcode.ER_DB_DROP_EXISTS
                or err.errno == errorcode.ER_BAD_DB_ERROR
            ):
                self.__createDatabase(cursor, cnx, database_name)
                self.__createTables(cursor)
                self.__createTriggers(cursor)
                cnx.commit()
                print("CONNECTED TO DATABASE")
            else:
                print(f"    {err}\n")
                self.close()
                exit(1)
        print()
        self.__cnx = cnx
        self.__cursor = cursor

    def __createDatabase(self, cursor, cnx, database_name):
        try:
            cursor.execute(
                f"CREATE DATABASE {database_name} DEFAULT CHARACTER SET 'UTF8MB4'")
            print(f"  Database `{database_name}` created successfully.")
            cnx.database = database_name
        except mysql.connector.Error as err:
            print(f"  Database `{database_name}` creation failed.")
            print(f"    {err}\n")
            self.close()
            exit(1)

    @staticmethod
    def __createTables(cursor):
        for table_name in TABLES:
            try:
                cursor.execute(TABLES[table_name])
                with open(f"Initializations/{table_name}.csv") as file:
                    for line in reader(file):
                        if line[0] != '\\N':
                            cursor.execute(INSERTS[table_name], tuple(line))
                print(f"    Table `{table_name}` created successfully.")
            except mysql.connector.Error as err:
                print(f"    Table `{table_name}` creation failed.")
                print(f"      {err}")

    @staticmethod
    def __createTriggers(cursor):
        for trigger_name in TRIGGERS:
            try:
                cursor.execute(TRIGGERS[trigger_name])
                print(f"    Trigger `{trigger_name}` created successfully.")
            except mysql.connector.Error as err:
                print(f"    Trigger `{trigger_name}` creation failed.")
                print(f"      {err}")

    def query(self, table_name, args):
        if len(args) < 2:
            args = list(args)
            args.append(True)
            args = tuple(args)
        statement = QUERIES[table_name] % args
        try:
            self.__cursor.execute(statement)
        except mysql.connector.Error as err:
            print(err)
            return []

        results = []
        for row in self.__cursor:
            results.append(row)
        print(f"{statement}", *results, sep="\n  ")
        return results

    def insert(self, table_name, args):
        statement = INSERTS[table_name] % args
        print(f"{statement}:")
        try:
            self.__cursor.execute(statement)
            print(f"  Inserted into row {self.__cursor.lastrowid}")
            self.__cnx.commit()
        except mysql.connector.Error as err:
            print(err)

    def update(self, table_name, args):
        statement = UPDATES[table_name] % args
        print(statement)
        try:
            self.__cursor.execute(statement)
            print(f"Updated {self.__cursor.rowcount} rows")
            self.__cnx.commit()
        except mysql.connector.Error as err:
            print(err)

    def advanced(self, inst, args):
        statement = ADVANCED[inst] % args
        try:
            self.__cursor.execute(statement)
            if inst == "newLocation":
                self.__cnx.commit()
        except mysql.connector.Error as err:
            print(err)
            return []

        results = []
        for row in self.__cursor:
            results.append(row)
        print(f"{statement}", *results, sep="\n  ")
        return results

    def close(self):
        self.__cursor.execute(
            f"DROP DATABASE IF EXISTS {self.__database_name}")
        try:
            print("\nCLOSING CONNECTION...")
            self.__cursor.close()
            self.__cnx.close()
            print("DISCONNECTED FROM DATABASE")
        except mysql.connector.Error as err:
            print(
                f"  Could not disconnect from database `{self.__database_name}`.")
            print(f"    {err}\n")
            exit(1)
