import os
import mysql.connector

from src.database.database_interface import IDatabaseConnecton


class MySQLConnection(IDatabaseConnecton):

    def __init__(self) -> None:

        self.host = os.environ.get('MYSQL_HOST')
        self.port = os.environ.get('MYSQL_PORT')
        self.db = os.environ.get('MYSQL_DB')
        self.user = os.environ.get('MYSQL_USER')
        self.password = os.environ.get('MYSQL_PASSWORD')

    def get_connection(self) -> tuple:

        connection = mysql.connector.connect(
            host=self.host,
            database=self.db,
            user=self.user,
            password=self.password,
            port=self.port
        )

        cursor = connection.cursor(dictionary=True)
        return connection, cursor

    def close_connection(self, e=None):

        connection, cursor = self.get_connection()

        if connection is not None:

            connection.close()
