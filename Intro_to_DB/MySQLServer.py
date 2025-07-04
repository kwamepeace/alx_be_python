import mysql.connector
from mysql.connector import errorcode
try:
    connection = mysql.connector.connect(
        host="localhost",
        username="root",
        password="password"

    )
    cursor = connection.cursor
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("alx_book_store created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    connection.close()