from .db import Connection

conn= Connection() 

class Orders():
    """ class for orders data """
   
    def place_order(self, parcel_type, weight, receiver, pick_up, destination, present_location):
    
        query = ("INSERT INTO orders (parcel_type, weight, receiver, pick_up, destination, present_location) VALUES('{}', '{}', '{}', '{}','{}','{}')".format( parcel_type, weight, receiver, pick_up, destination, present_location))
        conn.cursor.execute(query)
        return 'Order Added'

