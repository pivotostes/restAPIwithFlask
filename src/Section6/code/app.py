from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from config import app_active, app_config
from resources.user import UserRegister
from resources.item import Item, ItemList
from security import authenticate, identity

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    api = Api(app)
    jwt = JWT(app, authenticate, identity) # creates endpoint /auth

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')

    app.run(port=5000, debug=True)
