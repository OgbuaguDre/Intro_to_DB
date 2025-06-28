import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (without selecting a specific database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="yourusername",     # replace with your MySQL username
            password="yourpassword"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
