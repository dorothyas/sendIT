from flask import Flask
from api.routes import Urls
from api.models.db import Connection
from flask_jwt_extended import JWTManager


APP = Flask(__name__)
# Connection().create_tables()
Urls.get_url(APP)
APP.config['JWT_SECRET_KEY'] = 'secretKEY' 
jwt = JWTManager(APP)

if __name__=='__main__':
    APP.run()