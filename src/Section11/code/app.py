from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity

config = app_config[app_active]

app = Flask(__name__)
config.APP = app

config.APP.secret_key = config.SECRET
config.APP.config.from_object(config)
config.APP.config.from_pyfile('config.py')
config.APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

jwt = JWT(app, authenticate, identity) # creates endpoint /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)