

from flask import jsonify, request
from flask.views import MethodView

from src.estate.data_access_layer.data_access_interface\
    import DataAccessInterface
from src.estate.utils.filter_validator import validate_http_filters
from src.estate.estate_errors.errors import bad_request, not_found


class EstateFinder(MethodView):

    def __init__(self, data_access: DataAccessInterface) -> None:
        self.data_access = data_access

    def get(self):
        filters = request.args

        if len(list(filters)) == 0:
            result = self.data_access.read_properties_without_filters()

            return jsonify({'response': result}), 200

        valid_filters = validate_http_filters(filters)

        if type(valid_filters) is dict:

            if valid_filters.get('not_valid'):
                not_valid_filter = valid_filters.get('not_valid')

                return jsonify({'response': f'some filters are not valid:\
                        {not_valid_filter}'}), 400

        args = valid_filters

        result = self.data_access.read_properties_with_filters(*args)

        return jsonify({'response': result}), 200
