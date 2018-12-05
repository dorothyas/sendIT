import psycopg2
import os


class Connection:
    """class handles Database connection"""

    def __init__(self):

        try:
            if(os.getenv("FLASK_ENV")) == "Production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            elif(os.getenv("FLASK_ENV")) == "TESTING":
                self.connection = psycopg2.connect(dbname= 'test_db',
                                        user='postgres',
                                        password='dorothy',
                                        host='localhost',
                                        port='5432'
                                        )
            else:
                self.connection = psycopg2.connect(dbname= 'sendIT',
                                        user='postgres',
                                        password='dorothy',
                                        host='localhost',
                                        port='5432'
                                        )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.DatabaseError) as error:
            raise error
            
        self.create_tables()


    def create_tables(self):
        """ This method creates tables in the PostgreSQL database"""
        
        table = "CREATE TABLE IF NOT EXISTS users ( user_id SERIAL PRIMARY KEY, \
            user_name VARCHAR(10), user_email VARCHAR(100) UNIQUE, user_password VARCHAR(100), \
            admin BOOLEAN NOT NULL);"
        self.cursor.execute(table)
        
        table = "CREATE TABLE IF NOT EXISTS orders \
			( order_id SERIAL PRIMARY KEY, parcel_type VARCHAR(15),\
             weight INTEGER, receiver VARCHAR(15), \
            pick_up VARCHAR(15), destination VARCHAR(15), \
            status VARCHAR (255) DEFAULT 'pending',\
             present_location VARCHAR(15) DEFAULT 'none', \
             user_id INTEGER REFERENCES users(user_id)) ;"
        self.cursor.execute(table)

    def drop_tables(self):
        """
            method deletes tables
        """

        drop_user_table = "DROP TABLE users cascade"
        drop_orders_table = "DROP TABLE orders cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_orders_table) 

