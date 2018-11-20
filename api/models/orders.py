from .db import Connection

conn= Connection() 

class Orders():
    """ class for orders data """
   
    def place_order(self, parcel_type, weight, receiver, pick_up, destination, status, present_location):
    
        user_order = ("INSERT INTO orders (parcel_type, weight, receiver, pick_up, destination, status, present_location) VALUES('{}', '{}', '{}', '{}','{}','{}', '{}')".format( parcel_type, weight, receiver, pick_up, destination, status, present_location))
        conn.cursor.execute(user_order)
        return 'Order Added'

