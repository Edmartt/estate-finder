

import logging

from mysql.connector import ProgrammingError

from src.database.mysql_connection import MySQLConnection
from src.estate.data_access_layer.data_access_interface import DataAccessInterface


class MySQLDataAccessLayer(DataAccessInterface):

    def __init__(self, connector: MySQLConnection) -> None:

        self.connector = connector

    def read_properties_without_filters(self):

        query = '''
        SELECT p.id, p.address, p.city, s.name, p.price, p.description 

        FROM property AS p 

        INNER JOIN status_history as sh ON p.id = sh.property_id 

        INNER JOIN status AS s on s.id = sh.status_id 

        WHERE s.name = %s OR s.name = %s OR s.name = %s AND sh.update_date = (SELECT MAX(update_date) FROM status_history WHERE property_id = p.id );
        '''

        _, cursor = self.connector.get_connection()

        try:
            cursor.execute(query, ('pre_venta', 'en_venta', 'vendido',))
            result = cursor.fetchall()

            property_list = []

            if result:
                for row in result:
                    property_dict = {'address': row['address'], 'city': row['city'], 'status': row['name'], 'price':row['price'], 'description': row['description']}
                    property_list.append(property_dict)
                return property_list

        except ProgrammingError as ex:
            logging.exception(ex)

        finally:
            self.connector.close_connection()


    def read_properties_with_filters(self, *args: tuple):

        
        year = args[0] if len(args) > 0 else None
        city = args[1] if len(args) > 1 else None
        status = args[2] if len(args) > 2 else None
        
        query = '''
        SELECT p.id, p.address, p.city, s.name, p.price, p.description
        FROM property AS p
        INNER JOIN status_history as sh ON p.id = sh.property_id
        INNER JOIN status AS s on s.id = sh.status_id
        WHERE ((s.name = 'pre_venta' OR s.name = 'en_venta' OR s.name = 'vendido')
        AND sh.update_date = (SELECT MAX(update_date) FROM status_history WHERE property_id = p.id ))
        AND (p.year = %s OR %s IS NULL)
        AND (p.city = %s OR %s IS NULL)
        AND (s.name = %s OR %s IS NULL)
        '''
        
        params = [year, year, city, city, status, status]
        
        _, cursor = self.connector.get_connection()
        
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            
            property_list = []
            
            if result:
                for row in result:
                    property_dict = {'address': row['address'], 'city': row['city'], 'status': row['name'], 'price': row['price'], 'description': row['description']}
                    property_list.append(property_dict)
            
            return property_list
        
        except ProgrammingError as ex:
            logging.exception(ex)
        
        finally:
            self.connector.close_connection()
