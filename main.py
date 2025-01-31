import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "1499"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            client_encoding='utf8'
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE
                )
            """)
            print("Table created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")

def read_all_rows(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error reading all rows: {e}")

def read_one_row(connection, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            row = cursor.fetchone()
            if row:
                print(row)
            else:
                print("No row found with the given ID")
    except Exception as e:
        print(f"Error reading one row: {e}")

def create_row(connection, name, email):
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            print("Row created successfully")
    except Exception as e:
        print(f"Error creating row: {e}")

def update_row(connection, user_id, name, email):
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            print(f'Row "{user_id}" updated successfully')
    except Exception as e:
        print(f"Error updating row: {e}")

def delete_row(connection, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            print(f'Row "{user_id}" deleted successfully')
    except Exception as e:
        print(f"Error deleting row: {e}")

def main():
    connection = connect_to_db()
    need_row = 4
    if connection:
        # create_table(connection)

        create_row(connection, "John Doe", "john.doe@gmail.com")
        create_row(connection, "John Darling", "john.darlinggg@gmail.com")
        create_row(connection, "Lisa Maxwell", "lisa.max@gmail.com")
        create_row(connection, "Richard Castle", "rick.castle@gmail.com")
        
        print("All rows: ")
        read_all_rows(connection)
        print("Only", need_row, "row: ")
        read_one_row(connection, need_row)
        
        
        update_row(connection, 1, "Jane Doe", "jane.doe@example.com")
        
        
        delete_row(connection, 2)

        connection.close()

if __name__ == "__main__":
    main()
