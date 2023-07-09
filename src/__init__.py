from flask import Flask
from config import config


def create_app(config_name: str) -> Flask:

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from src.estate import estate_routes
    app.register_blueprint(estate_routes)

    return app

