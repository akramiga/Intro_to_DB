import mysql.connector
from mysql.connector import Error
host = "localhost"
user = "root"
password = "diego3107"
database = "alx_book_store"
try:
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(f"Database '{database}' created successfully or already exists.")

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")    