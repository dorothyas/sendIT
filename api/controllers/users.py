from flask import jsonify, request
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.users import Users
import re

from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity


class Signup(MethodView):
    """  """

    def post(self):
        user = Users()

        keys = ("user_name","user_email", "contact","user_password","admin")

        data = request.json()

        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        if data['user_name'] == "":
            return jsonify({'Message':'Enter Username'}), 400

        if ' ' in data['user_name']:
            return jsonify({'Message':'User name should not contain any spaces'}), 400

        if data['user_email'] == "":
            return jsonify({'Message':'Enter Email'}), 400

        if ' ' in data['user_email']:
            return jsonify({'Message':'Email should not contain any spaces'}), 400

        if not isinstance(data['contact'], int):
            return jsonify({'Message':'Contact should be an integer'}), 400
            
        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, data['user_email']):
            return jsonify({'message':'Enter valid Email'}), 400

        user_password = request.json['user_password']
        hashed_password = generate_password_hash(user_password, method= 'sha256')
        user_cred = user.register_user( request.json['user_name'], request.json['user_email'], request.json['contact'],hashed_password, request.json['admin'])
        if user_cred == 'Email already exists':
            return jsonify({'message': user_cred}), 401
        return jsonify({'message': user_cred}), 201
        
class Signin(MethodView):

    def post(self):

        signin_user =  Users()
        
        keys = ("user_name", "user_password")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        if request.json['user_name'] == "":
            return jsonify({'Message':'Enter Username'}), 400

        if ' ' in request.json['user_name']:
            return jsonify({'Message':'User name should not contain any spaces'}), 400

        if request.json['user_password'] == "":
            return jsonify({'Message':'Enter User_password'}), 400

        user_id = signin_user.get_user(request.json['user_name'], request.json['user_password'])
        if not user_id:
            return jsonify({'Message': 'User does not exist'})
        return jsonify({'access_token': create_access_token(identity= user_id),
            'Message': 'User logged in'})
        







