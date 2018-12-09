from flask.views import MethodView
from api.controllers.users import Signup, Signin
from api.controllers.orders import Order, GetOrder, Status, Location, Destination, CancelOrder, SpecificUser

class Urls(object):
 
    @staticmethod
    def get_url(app):

        app.add_url_rule('/api/v1/auth/signup',
                         view_func=Signup.as_view('create_account'), methods=['POST',])
        app.add_url_rule('/api/v1/auth/login',
                         view_func=Signin.as_view('login'), methods=['POST',])                                            
        app.add_url_rule('/api/v1/parcels',
                        view_func=Order.as_view('make order'), methods=['POST',]) 
        app.add_url_rule('/api/v1/parcels',
                         view_func=GetOrder.as_view('GetOrders'),
                         defaults={'order_id': None}, methods=['GET',])
        app.add_url_rule('/api/v1/parcels/<int:order_id>',
                         view_func=GetOrder.as_view('one_order'), methods=['GET',])
        app.add_url_rule('/api/v1/parcels/<int:order_id>/status',
                         view_func=Status.as_view('update_status'), methods=['PUT',])   
        app.add_url_rule('/api/v1/parcels/<int:order_id>/destination',
                         view_func=Destination.as_view('update destination'), methods=['PUT',])
        app.add_url_rule('/api/v1/parcels/<int:order_id>/presentlocation',
                         view_func=Location.as_view('update location'), methods=['PUT',]) 
        app.add_url_rule('/api/v1/parcels/<int:order_id>/cancel',
                         view_func= CancelOrder.as_view('cancel_status'),methods=['PUT',])
        app.add_url_rule('/api/v1/users/<int:user_id>/parcels',
                         view_func= SpecificUser.as_view('specfic_user'), methods=['GET',])                                                                                                                            