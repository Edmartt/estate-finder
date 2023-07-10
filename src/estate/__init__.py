

from flask import Blueprint


estate_routes = Blueprint('estate', __name__, url_prefix='/api/v1')

from . import routes
