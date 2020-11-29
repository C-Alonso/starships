from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username field cannot be left blank!")
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Password field cannot be left blank!")

    def post(self):
        """Create new User"""
        request_data = UserRegister.parser.parse_args()
        # Check if USER with that username already exists.
        user_exists = UserModel.find_by_username(request_data["username"])

        if user_exists:
            return {"message": "This username is already taken!"}, 400

        # For each of the keys, the value is passed to the User Model
        user = UserModel(**request_data)
        user.upsert()

        return {"message": "User created successfully."}, 201
