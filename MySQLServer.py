import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no specific database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="yourusername",     # replace with your MySQL username
            password="yourpassword"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
