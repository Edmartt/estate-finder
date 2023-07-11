

from src.database.mysql_connection import MySQLConnection
from src.estate import estate_routes
from src.estate.data_access_layer.data_access_implementation\
    import MySQLDataAccessLayer
from src.estate.http_estate import EstateFinder


connector = MySQLConnection()

data_access_implementation = MySQLDataAccessLayer(connector)

estates = EstateFinder.as_view('state finder', data_access_implementation)


estate_routes.add_url_rule('/estates', view_func=estates, methods=['GET'])
