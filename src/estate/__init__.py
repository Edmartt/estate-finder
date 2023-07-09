

from flask import Blueprint


estate_routes = Blueprint('estate', __name__)

from . import routes
