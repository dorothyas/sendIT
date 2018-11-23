from .db import Connection

conn= Connection() 

class Orders():
    """ class for orders data """
   
    def place_order(self, parcel_type, weight, receiver, pick_up, destination, present_location, user_id):
        """ 
            method for updating status 
        """
        query = ("INSERT INTO orders (parcel_type, weight, receiver, pick_up, destination, \
        present_location, user_id) VALUES\
        ('{}', '{}', '{}', '{}','{}','{}','{}')".format( parcel_type, weight, receiver, pick_up, \
        destination, present_location , user_id))
        conn.cursor.execute(query)
        return 'Order Added'

    def get_orders(self):

        conn.cursor.execute("SELECT * FROM orders")
        fetched_parcels = conn.cursor.fetchall() 

        keys=["order_id", "parcel_type", "weight", "receiver", "pick_up", "destination", "status", \
        "present_location","user_id"]
       
        parcels = []
        for parcel in fetched_parcels:
            parcels.append(dict(zip(keys, parcel)))
        if not fetched_parcels:    
            return "no parcel found"
        return  parcels 

    def get_one_order(self, order_id):
        
        conn.cursor.execute("SELECT * FROM orders WHERE order_id = %s", [order_id])
        fetched_parcel = conn.cursor.fetchone()
        if not fetched_parcel:
            return "Order not available at the moment" 
        
        one_parcel = []
        keys=["order_id", "parcel_type", "weight", "receiver", "pick_up", "destination", "status", \
        "present_location","user_id"]
       
        one_parcel.append(dict(zip(keys, fetched_parcel))) 
        return one_parcel    
            
    def update_status(self, order_id, status):
        conn.cursor.execute("""SELECT "order_id" FROM orders WHERE order_id = %s""",[order_id] )
        order_status=conn.cursor.fetchone()
        if not order_status:
            return "No parcel_order"
        query = "UPDATE  orders SET status = %s WHERE order_id = %s;"
        conn.cursor.execute(query,(status, order_id ))
        updated_rows = conn.cursor.rowcount
        return updated_rows

    def update_destination(self, order_id,destination):

        
        conn.cursor.execute("""SELECT "order_id" FROM orders WHERE order_id= %s""",(order_id, ) )
        get_destination=conn.cursor.fetchone()
        print(get_destination)
        if not get_destination:
            return "No parcel destination to update, please check order_id"
        query = "UPDATE orders SET destination = %s WHERE order_id = %s;"
        conn.cursor.execute(query,(destination, order_id, ))
        updated_rows = conn.cursor.rowcount
        return updated_rows



    def update_location(self,order_id, present_location):

        conn.cursor.execute("""SELECT "order_id" FROM orders WHERE order_id= %s""",(order_id, ) )
        get_present_location=conn.cursor.fetchone()
        if not get_present_location:
            return "please check order_id"
        query = "UPDATE  orders SET present_location = %s WHERE order_id = %s;"
        conn.cursor.execute(query,(present_location, order_id, ))
        updated_rows = conn.cursor.rowcount
        return updated_rows
            


            
        


