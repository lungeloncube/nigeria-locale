import functools

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource, Namespace, fields
from flask import request, abort
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
import uuid
from hmac import compare_digest

auth_namespace = Namespace("auth", description="a namespace for authentication")


def is_valid(api_key):
    user_key = User.find_by_api_key(api_key)
    if user_key and compare_digest(user_key, api_key):
        return True


signup_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description='An email'),
        'password': fields.String(required=True, description='A password'),
        'api_key': fields.String(required=True, description='api key to access resources')
    }
)

user_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description='An email'),
        'password_hash': fields.String(required=True, description='A password'),
        'api_key': fields.String(required=True, description='api key to access resources')

    }
)


@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        data = request.get_json()

        new_user = User(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password')),
            api_key=uuid.uuid4().hex
        )
        new_user.save()
        return new_user, HTTPStatus.CREATED



