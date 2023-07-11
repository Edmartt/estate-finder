from flask import jsonify, make_response

from src import estate


@estate.estate_routes.errorhandler(401)
def not_authorized(error):
    return make_response(jsonify({'response': 'not authorized'}), 401)


@estate.estate_routes.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'response': 'bad request'}), 400)


@estate.estate_routes.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'response': 'resource not found'}), 404)
