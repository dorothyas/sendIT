from flask import Flask
from flask_jwt_extended import JWTManager

from api.models.db import Connection
from api.routes import Urls

APP = Flask(__name__)

Urls.get_url(APP)
APP.config['JWT_SECRET_KEY'] = 'secretKEY' 
jwt = JWTManager(APP)

if __name__=='__main__':
    APP.run()
