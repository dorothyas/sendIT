from flask import jsonify, request
from flask.views import MethodView

from api.models.users import Users
import re

from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity


class Signup(MethodView):
    """  """

    def post(self):
        user = Users()

    
        data = request.get_json()
        
        # keys = ("user_name","user_email", "contact","user_password","admin")

        # if not set(keys).issubset(set(request.json)):
        #     return jsonify({"Message":'Missing data'}), 400

        # if data['user_name'] == "":
        #     return jsonify({'Message':'Enter Username'}), 400

        # if  data['user_name'].strip()== '':
        #     return jsonify({'Message':'User name should not contain any spaces'}), 400

        # if data['user_email'] == "":
        #     return jsonify({'Message':'Enter Email'}), 400

        # if ' ' in data['user_email']:
        #     return jsonify({'Message':'Email should not contain any spaces'}), 400

        # if not isinstance(data['contact'], int):
        #     return jsonify({'Message':'Contact should be an integer'}), 400
            
        # pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        # if not re.match(pattern, data['user_email']):
        #     return jsonify({'message':'Enter valid Email'}), 400


        user_name = data.get("user_name")
        user_email = data.get("user_email")
        contact = data.get("contact")
        user_password = data.get("user_password")
        admin = data.get("admin")
        user_details = user.register_user(user_name, user_email, contact, user_password, admin)
        if user_details == "Email exists boss, Please use another email":
            return jsonify({'message': user_details,
                            'status':'success'}), 401
                            

        return jsonify({'message': user_details}), 201
        
class Signin(MethodView):

    def post(self):

        user =  Users()
        
        keys = ("user_name", "user_password")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        if request.json['user_name'].strip() == "":
            return jsonify({'Message':'Enter Username'}), 400

        if ' ' in request.json['user_name']:
            return jsonify({'Message':'User name should not contain any spaces'}), 400

        if request.json['user_password'].strip() == "":
            return jsonify({'Message':'Enter User_password'}), 400

        logged_user = user.get_user(request.json['user_name'], request.json['user_password'])
        if not logged_user:
            return jsonify({'Message': 'User does not exist'})
        return jsonify({'access_token': create_access_token(identity=logged_user),
            'Message': 'User logged in'})
        







