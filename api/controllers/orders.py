from flask import jsonify, request
from flask.views import MethodView
from api.models.orders import Orders
import re

from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity

class Order (MethodView):    
    @jwt_required
    def post(self):
        make_order = Orders()

        keys = ("user_name","user_email", "contact","user_password","admin")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        parcel_order = make_order.place_order(request.json['parcel_type'],request.json['weight'],request.json['receiver'],request.json['pick_up'],request.json['present_location'])
        
        return jsonify({'message': parcel_order}), 201
           

