import re

from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from api.models.orders import Orders


class Order (MethodView): 
    """ 
        class for getting  orders data
    """

    @jwt_required
    def post(self):
        """ 
            method for adding parcel order
        """

        current_user= get_jwt_identity()
        make_order = Orders()

        keys = ("parcel_type", "weight", "receiver", "pick_up", "destination")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400

        parcel_order = make_order.place_order(request.json['parcel_type'],request.json['weight'],
                request.json['receiver'],request.json['pick_up'], request.json['destination'], current_user[0])
        
        return jsonify({'message': parcel_order}), 201
           

class GetOrder(MethodView): 
    """ 
        method for getting  orders 
    """    

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
    """ 
        method for updating status 
    """
    @jwt_required
    def put(self, order_id):
        update_status = Orders()

        current_user=get_jwt_identity()
        if current_user[4] == False:
            return jsonify({'Message': 'Admin Only'})

        new_status = update_status.update_status(str(order_id), request.json['status'].strip())

        if new_status:
            response = {'message': 'status has been updated' }
            return jsonify(response), 200
        return jsonify({'msg': 'No orders '}), 400

class Location(MethodView):
    """ 
        method for updating location
    """
    @jwt_required
    def put(self, order_id):
    
        update_location = Orders()

        current_user=get_jwt_identity()
        if current_user[4] == False:
            return jsonify({'Message': 'Admin Only'})

        data = request.json
        keys = ("present_location", )

        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400
       
        new_location = update_location.update_location(str(order_id), data['present_location'].strip())

        if new_location:
            response= {'msg': 'location has been updated'}
            return jsonify(response), 200

class Destination(MethodView):
    """ 
        method for updating status 
    """
    @jwt_required
    def put(self,order_id):
       
        update_destination = Orders()
        current_user=get_jwt_identity()
        if current_user[4] == True:
            return jsonify({'Message': 'Only User can update location'}), 400

        keys = ("destination",)
        if not set(keys).issubset(set(request.json)):
            return jsonify({'msg':'missing data'}), 400

        new_destination = update_destination.update_destination(str(order_id), request.json['destination'].strip())

        if new_destination:
            response_object = {
            'message':'destination has been update'}
            return jsonify(response_object), 200 
        return jsonify({'msg': 'Order not found'}), 404
