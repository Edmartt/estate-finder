

from flask import jsonify, request
from flask.views import MethodView

from src.estate.data_access_layer.data_access_interface import DataAccessInterface


class EstateFinder(MethodView):

    def __init__(self, data_access: DataAccessInterface) -> None:
        
        self.data_access = data_access

    def get(self):

        filters = request.args

        if len(list(filters)) == 0:
            result = self.data_access.read_properties_without_filters()

            return jsonify({'response': result}), 200

        year = filters.get('year')
        city = filters.get('city')
        status = filters.get('status')
        args = (year, city, status)

        result = self.data_access.read_properties_with_filters(*args)


        return jsonify({'response': result}), 200
