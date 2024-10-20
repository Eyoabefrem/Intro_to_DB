import mysql.connector

def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="Chalachubechebete#1"  
        )
        
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

if __name__ == "__main__":
    create_database()