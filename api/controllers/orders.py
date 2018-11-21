from flask import jsonify, request
from flask.views import MethodView
from api.models.orders import Orders
import re

from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity

class Order (MethodView):    
    @jwt_required
    def post(self):
        make_order = Orders()

        keys = ("parcel_type", "weight", "receiver", "pick_up", "destination", "present_location")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        parcel_order = make_order.place_order(request.json['parcel_type'],request.json['weight'],request.json['receiver'],request.json['pick_up'],request.json['present_location'], request.json['destination'])
        
        return jsonify({'message': parcel_order}), 201
           

class GetOrder(MethodView):    
    @jwt_required
    def get(self, order_id):
        make_order = Orders

        if order_id is None:
            orders_list = make_order.get_orders(self)
            if orders_list == "no parcel found":
                return jsonify({"Orders": orders_list}), 404
            return jsonify({"Orders": orders_list}), 200
            
        order_list = make_order.get_one_order(self, order_id)
        if order_list == "Order not available at the moment":
            return jsonify({"message": "No orders yet"}), 400
        return jsonify({"Orders": order_list}), 200


class Status(MethodView):
    @jwt_required
    def put(self, order_id):
        update_status = Orders()

        new_status = update_status.update_status(str(order_id), request.json['status'].strip())

        if new_status:
            response = {'message': new_status }
            return jsonify(response), 200
        return jsonify({'msg': 'No orders '}), 400

class Location(MethodView):

    @jwt_required
    def put(self, order_id):
    
        update_location = Orders()

        data = request.json
        keys = ('present_location')

        if keys not in data:
            return 'missing data'
        try:
            present_location = data['present_location'].strip()
        except:
            return 'Invalid data',400
        if not present_location:
            return 'Empty data',400
        new_location = update_location.update_location(str(order_id), request.json['present_location'].strip())

        if new_location:
            response= {'message': new_location }
            return jsonify(response), 200
        return jsonify({'Alert':"Not Authorised to perform this task"}),400
class Destination(MethodView):
    @jwt_required
    def put(self,order_id):
       
        update_destination = Orders()

        keys = ("destination")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'msg':'missing data'}), 400

        new_destination = update_destination.update_destination(str(order_id), request.json['destination'].strip())

        if not new_destination:
            return jsonify({'msg': 'order not found'})
            
        response = {'data': new_destination,
        'msg':'successfully changed destination'
        }
        return jsonify(response), 200
        
   


       
