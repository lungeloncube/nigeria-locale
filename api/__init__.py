from flask import Flask
from flask_restx import Api
from .locations.views import locations_namespace
from .auth.views import auth_namespace
from .config.config import config_dict


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    api.add_namespace(locations_namespace, path='/locations')
    api.add_namespace(auth_namespace, path='/auth')

    return app