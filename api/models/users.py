from .db import Connection
from werkzeug.security import generate_password_hash, check_password_hash


class Users:
    """ class for users data """

    def register_user(self, user_name, user_email, contact, user_password, admin):
        """ method for registering user """
        conn=Connection() 

        conn.cursor.execute("SELECT * FROM users WHERE user_email = %s", [user_email])
        check_email = conn.cursor.fetchone()
        hashed_password = generate_password_hash(user_password, method='sha256')
        if check_email:
            return 'Email already exists'

        insert_user = "INSERT INTO users(user_name, user_email, contact, user_password, admin) \
        VALUES('{}', '{}', '{}', '{}','{}')".format(user_name, user_email, contact, hashed_password, admin)
        conn.cursor.execute(insert_user)
        return "Account successfully created, Please login"

    def get_user(self, user_name, password):
        conn=Connection() 
        conn.cursor.execute("SELECT * FROM users where user_name = %s", [user_name])
        user = conn.cursor.fetchone() 
        return user
        
    def make_admin(self):
        conn=Connection() 
        query = "UPDATE users SET admin = {} WHERE user_id = '{}';".format(True, 1)
        conn.cursor.execute(query)
 
