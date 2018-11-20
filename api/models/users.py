from .db import Connection


conn = Connection() 
class Users:
    """ class for users data """

    def register_user(self, user_name, user_email, contact, user_password,admin):
        """ method for registering user """
    
        conn.cursor.execute("SELECT* FROM users where user_name = %s", [user_name])
        used_name = conn.cursor.fetchone()
        conn.cursor.execute("SELECT * FROM users WHERE user_email = %s", [user_email])
        used_email = conn.cursor.fetchone()
        if used_name:
            return 'Username already exists'
        if used_email:
            return 'Email already exists'
        add_user=("INSERT INTO users(user_name, user_email, contact, user_password, admin) VALUES('{}', '{}', '{}', '{}','{}')".format(user_name, user_email, contact, user_password, admin))
        conn.cursor.execute(add_user)
        return 'Account created'  

    def get_user(self, user_name, password):
        
        conn.cursor.execute("SELECT * FROM users where user_name = %s", [user_name])
        user = conn.cursor.fetchone() 
        return user
        
    def make_admin(self):
        query = "UPDATE users SET admin = {} WHERE user_id = '{}';".format(True, 1)
        conn.cursor.execute(query)
 
