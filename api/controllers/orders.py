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
        
        return jsonify({'Message': parcel_order}), 201
           

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
            return jsonify({"Message": "No orders yet"}), 400
        return jsonify({"Orders": order_list}), 200

class SpecificUser(MethodView):
      
    @jwt_required
    def get(self, user_id):
       
        specific_user = Orders()
        current_user=get_jwt_identity()
        if current_user[4] == True:
            return jsonify({'Message': 'Admin Only'}), 400
        
        users_list = specific_user.specific_user_orders(user_id)
        if users_list == "no orders for this user":
            return jsonify({'Message': 'No Orders '}) , 404
        response_object = {'Orders': users_list}
        return jsonify(response_object), 200

class Status(MethodView):
    """ 
        method for updating status 
    """
    @jwt_required
    def put(self, order_id):
        update_status = Orders()

        current_user=get_jwt_identity()
        if current_user[4] == True:
            return jsonify({'Message': 'Admin Only'}), 400

        new_status = update_status.update_status(str(order_id), request.json['status'].strip())

        if new_status:
            response = {'Message': 'status has been updated' }
            return jsonify(response), 200
        return jsonify({'Message': 'No orders '}), 400

class Location(MethodView):
    """ 
        method for updating location
    """
    @jwt_required
    def put(self, order_id):
    
        update_location = Orders()

        current_user=get_jwt_identity()
        if current_user[4] == True:
            return jsonify({'Message': 'Admin Only'}), 400

        data = request.json
        keys = ("present_location", )

        if not set(keys).issubset(set(request.json)):
            return jsonify({"Message":'Missing data'}), 400
       
        new_location = update_location.update_location(str(order_id), data['present_location'].strip())

        if new_location:
            response= {'Message': 'location has been updated'}
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
            return jsonify({'Message':'missing data'}), 400

        new_destination = update_destination.update_destination(str(order_id), request.json['destination'].strip())

        if new_destination:
            response_object = {
            'Message':'destination has been updated'}
            return jsonify(response_object), 200 
        return jsonify({'Message': 'Order not found'}), 404

class CancelOrder(MethodView):
   
    @jwt_required
    def put(self, order_id):
        """
            this method for cancelling of an order
        """
        cancel_order = Orders() 
        current_user=get_jwt_identity()
        if current_user[4] == True:
            return jsonify({'Message': 'Only User can update location'}), 400
        
        data =request.get_json()
        keys = ("status")
        status_required =['cancelled']

        if keys not in data:
            return jsonify({'Message': 'Missing key'}), 400
        try:
            status = data['status'].strip()
        except AttributeError:
            return jsonify({'Message': 'invalid data'}),404
        if not status:
            return jsonify({'Message':'missing data'}),404
        if status not in status_required:
            return jsonify({'Message':'Status must only be cancelled'}), 400
        cancelled_order = cancel_order.update_cancel_status(str(order_id),request.json['status'].strip())

        if cancelled_order == 'No order found':
            return jsonify({'Message':'No order to be cancelled'}),404
        return jsonify({'Message': 'Order has been cancelled '}), 200
            

            