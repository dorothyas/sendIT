from flask.views import MethodView
from api.controllers.users import Signup, Signin

class Urls(object):
 
    @staticmethod
    def get_url(app):

        app.add_url_rule('/api/v1/auth/signup',
                         view_func=Signup.as_view('create_account'), methods=['POST',])
        app.add_url_rule('/api/v1/auth/login',
                         view_func=Signin.as_view('login'), methods=['POST',])                                            
        app.add_url_rule('/api/v1/auth/parcel',
                        view_func=Signin.as_view('make order'), methods=['POST',])                                            