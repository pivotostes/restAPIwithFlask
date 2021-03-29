from operator import ne
from flask_jwt_extended.utils import get_jwt_header
from flask_jwt_extended.view_decorators import jwt_required
from models.user import UserModel
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                         type=str,
                         required=True,
                         help="This field cannot be blank."
                         )
_user_parser.add_argument('password',
                         type=str,
                         required=True,
                         help="This field cannot be blank."
                         )

class UserRegister(Resource):

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'} , 404
        return user.json()

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found.'} , 404
        user.delete_from_db()
        return {'message': 'User deleted'}, 200

class UserList(Resource):
    classmethod
    def get(cls):
        users = {'users': list(map(lambda x: x.json(), UserModel.query.all()))}
        return users

class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        # This is what the 'authenticate()' function used to do
        if user and safe_str_cmp(user.password, data['password']):
            # identity= is what the 'identity()' function used to do
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {'message': 'Invalid credentials.'}, 401

class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200

