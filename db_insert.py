import mysql.connector
from mysql.connector import Error

def create_connection( ):
    try:
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            port="3306",
            database="inventory_pos_db",

auth_plugin='mysql_native_password',
            use_pure="True"
            )
        if conn.is_connected( ):
            print("connected to mysql successfully..")
            return conn

    except Error as e:
        print("Error:",e)

conn=create_connection( )
print(conn)

def insert_record(conn):
    try:
        cursor=conn.cursor()
        product_data=[("Wireless Mouse", "Electronics", 799.00, 50),
            ("Mechanical Keyboard", "Electronics", 2499.00, 30),
            ("USB-C Cable", "Accessories", 299.00, 100),
            ("Gaming Headset", "Electronics", 1899.00, 20),
            ("Laptop Stand", "Accessories", 1299.00, 40),
            ("HD Webcam", "Electronics", 3499.00, 25),
            ("Ergonomic Chair", "Furniture", 8999.00, 10),
            ("Bluetooth Speaker", "Electronics", 1599.00, 35),
            ("External Hard Drive", "Electronics", 4500.00, 15),
            ("Desk Pad", "Accessories", 499.00, 60)
        ]
        query="insert into products(product_name,category,price,stock_quantity) values(%s,%s,%s,%s"
        cursor.executemany(query,product_data)
        conn.commit( )
        print("Record inserted succsessfully")
    except Error as e:
        print("Error as",e)

conn=create_connection( )
print(conn)
insert_record(conn)

def insert_record(conn):
    try:
        cursor = conn.cursor()
        product_data = [
            ("Wireless Mouse", "Electronics", 799.00, 50),
            ("Mechanical Keyboard", "Electronics", 2499.00, 30),
            ("USB-C Cable", "Accessories", 299.00, 100),
            ("Gaming Headset", "Electronics", 1899.00, 20),
            ("Laptop Stand", "Accessories", 1299.00, 40),
            ("HD Webcam", "Electronics", 3499.00, 25),
            ("Ergonomic Chair", "Furniture", 8999.00, 10),
            ("Bluetooth Speaker", "Electronics", 1599.00, 35),
            ("External Hard Drive", "Electronics", 4500.00, 15),
            ("Desk Pad", "Accessories", 499.00, 60)
        ]
        
        # Added the VALUES (%s, %s, %s, %s) clause here:
        query = "INSERT INTO products (product_name, category, price, stock_quantity) VALUES (%s, %s, %s, %s)"
        
        cursor.executemany(query, product_data)
        conn.commit()
        print("Record inserted successfully")
        
    except Error as e:
        print("Error as", e)
conn=create_connection( )
print(conn)
insert_record(conn)

def insert_record(conn):
    try:
        cursor=conn.cursor( )
        customer_data=[("Piyush Mehra","9850802824"),
                       ("Shantanu Nair","9945257525"),
                       ("Rohan Mehta", "9911223344"),
            ("Ananya Singh", "9765432109"),
            ("Vikram Verma", "9898989898"),
            ("Neha Deshmukh", "9123456789"),
            ("Kiran Rao", "9876512345"),
            ("Siddharth Joshi", "9988776655"),
            ("Pooja Nair", "9765123480"),
            ("Amit Kulkarni", "9822001122")
        ]

        query="insert into customers(customer_name,phone) values(%s,%s)"
        cursor.executemany(query,customer_data)
        conn.commit( )
        print("record inserted succesfully")
        cursor.close( )

    except Error as e:
        print("Error as",e)

conn=create_connection( )
print(conn)
insert_record(conn)

def insert_record(conn):
    cursor=conn.cursor( )
    sales_data=[
            (1, 1, 2, 1598.00, '2026-01-05'), (2, 3, 5, 1495.00, '2026-01-06'), 
            (3, 2, 1, 2499.00, '2026-01-08'), (4, 5, 2, 2598.00, '2026-01-10'), 
            (5, 4, 1, 1899.00, '2026-01-12'), (6, 6, 1, 3499.00, '2026-01-15'), 
            (7, 8, 3, 4797.00, '2026-01-17'), (8, 10, 4, 1996.00, '2026-01-20'), 
            (9, 7, 1, 8999.00, '2026-01-22'), (10, 9, 2, 9000.00, '2026-01-25'),
            (1, 3, 2, 598.00, '2026-01-28'), (3, 1, 1, 799.00, '2026-01-30'), 
            (5, 2, 2, 4998.00, '2026-02-01'), (2, 5, 1, 1299.00, '2026-02-02'), 
            (4, 8, 2, 3198.00, '2026-02-04'), (7, 4, 2, 3798.00, '2026-02-05'), 
            (9, 10, 5, 2495.00, '2026-02-07'), (6, 9, 1, 4500.00, '2026-02-09'), 
            (8, 6, 2, 6998.00, '2026-02-10'), (10, 7, 1, 8999.00, '2026-02-12'),
            (2, 1, 3, 2397.00, '2026-02-14'), (4, 3, 1, 299.00, '2026-02-15'), 
            (1, 5, 3, 3897.00, '2026-02-17'), (3, 8, 1, 1599.00, '2026-02-18'), 
            (6, 2, 1, 2499.00, '2026-02-20'), (5, 10, 2, 998.00, '2026-02-22'), 
            (8, 4, 3, 5697.00, '2026-02-24'), (10, 6, 1, 3499.00, '2026-02-25'), 
            (7, 9, 1, 4500.00, '2026-02-27'), (9, 1, 4, 3196.00, '2026-02-28'),
            (3, 7, 1, 8999.00, '2026-03-01'), (1, 6, 2, 6998.00, '2026-03-02'), 
            (5, 3, 3, 897.00, '2026-03-04'), (2, 9, 2, 9000.00, '2026-03-05'), 
            (4, 2, 1, 2499.00, '2026-03-07'), (8, 5, 2, 2598.00, '2026-03-08'), 
            (6, 8, 4, 6396.00, '2026-03-10'), (10, 1, 1, 799.00, '2026-03-12'), 
            (7, 10, 3, 1497.00, '2026-03-14'), (9, 4, 2, 3798.00, '2026-03-15'),
            (1, 2, 1, 2499.00, '2026-03-17'), (2, 4, 1, 1899.00, '2026-03-18'), 
            (3, 6, 1, 3499.00, '2026-03-20'), (4, 8, 2, 3198.00, '2026-03-22'), 
            (5, 1, 5, 3995.00, '2026-03-24'), (6, 3, 4, 1196.00, '2026-03-25'), 
            (7, 5, 1, 1299.00, '2026-03-27'), (8, 7, 1, 8999.00, '2026-03-28'), 
            (9, 9, 1, 4500.00, '2026-03-30'), (10, 10, 2, 998.00, '2026-03-31'),
            (2, 6, 2, 6998.00, '2026-04-01'), (1, 8, 1, 1599.00, '2026-04-03'), 
            (4, 10, 5, 2495.00, '2026-04-04'), (3, 1, 2, 1598.00, '2026-04-06'), 
            (5, 9, 2, 9000.00, '2026-04-08'), (8, 2, 1, 2499.00, '2026-04-10'), 
            (7, 3, 3, 897.00, '2026-04-11'), (6, 5, 2, 2598.00, '2026-04-13'), 
            (10, 4, 1, 1899.00, '2026-04-15'), (9, 7, 1, 8999.00, '2026-04-17'),
            (3, 3, 2, 598.00, '2026-04-18'), (1, 4, 2, 3798.00, '2026-04-20'), 
            (2, 7, 1, 8999.00, '2026-04-22'), (5, 6, 1, 3499.00, '2026-04-24'), 
            (4, 1, 3, 2397.00, '2026-04-25'), (6, 10, 1, 499.00, '2026-04-27'), 
            (9, 8, 2, 3198.00, '2026-04-28'), (7, 2, 2, 4998.00, '2026-04-30'), 
            (8, 9, 1, 4500.00, '2026-05-02'), (10, 5, 3, 3897.00, '2026-05-04'),
            (1, 10, 4, 1996.00, '2026-05-05'), (3, 9, 1, 4500.00, '2026-05-07'), 
            (2, 8, 3, 4797.00, '2026-05-09'), (5, 7, 1, 8999.00, '2026-05-10'), 
            (4, 6, 1, 3499.00, '2026-05-12'), (7, 1, 2, 1598.00, '2026-05-14'), 
            (8, 3, 1, 299.00, '2026-05-15'), (6, 4, 2, 3798.00, '2026-05-17'), 
            (10, 2, 1, 2499.00, '2026-05-19'), (9, 5, 2, 2598.00, '2026-05-20'),
            (2, 2, 1, 2499.00, '2026-05-22'), (4, 4, 1, 1899.00, '2026-05-24'), 
            (1, 6, 1, 3499.00, '2026-05-25'), (3, 8, 2, 3198.00, '2026-05-27'), 
            (6, 1, 1, 799.00, '2026-05-28'), (5, 5, 4, 5196.00, '2026-05-30'), 
            (8, 10, 2, 998.00, '2026-06-01'), (7, 9, 2, 9000.00, '2026-06-03'), 
            (10, 3, 3, 897.00, '2026-06-05'), (9, 7, 1, 8999.00, '2026-06-07'),
            (3, 5, 1, 1299.00, '2026-06-08'), (1, 7, 1, 8999.00, '2026-06-10'), 
            (5, 2, 2, 4998.00, '2026-06-12'), (2, 10, 1, 499.00, '2026-06-14'), 
            (4, 9, 1, 4500.00, '2026-06-15'), (7, 6, 2, 6998.00, '2026-06-17'), 
            (6, 8, 1, 1599.00, '2026-06-19'), (8, 1, 3, 2397.00, '2026-06-20'), 
            (10, 4, 2, 3798.00, '2026-06-22'), (9, 3, 4, 1196.00, '2026-06-25')
        ]
    query="insert into sales(customer_id,product_id,quantity_sold,total_amount,sale_date) values(%s,%s,%s,%s,%s)"
    cursor.executemany(query,sales_data)
    print("Record inserted succesfully")
    conn.commit( )

conn=create_connection( )
print(conn)
insert_record(conn)
