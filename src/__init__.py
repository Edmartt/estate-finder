from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from config import config


def create_app(config_name: str) -> Flask:

    app = Flask(__name__)
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'

    swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'estate finder': 'search estates'
        }
    )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from src.estate import estate_routes

    app.register_blueprint(estate_routes)
    app.register_blueprint((swagger_blueprint))

    return app
