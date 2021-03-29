from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from resources.user import UserRegister, User, UserList, UserLogin, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList

config = app_config[app_active]

app = Flask(__name__)
config.APP = app

config.APP.secret_key = config.SECRET
config.APP.config.from_object(config)
config.APP.config.from_pyfile('config.py')
config.APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

jwt = JWTManager(app) # not creating endpoint /auth

"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""
@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:  # Instead of hard-coding, you should read from a config file or a database
        return {'is_admin': True}
    return {'is_admin': False}

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)