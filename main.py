import time
import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_config = {
    'host': 'mariadb-galera.default.svc.cluster.local',
    'user': 'myuser',
    'password': 'test123',
    'database': 'my-k8s-service'
}

def create_connection():
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MariaDB")
    except Error as e:
        print(f"Error: {e}")
    return connection

def create_table(connection):
    """Create table if it does not exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS my_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        data VARCHAR(255) NOT NULL
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def insert_data(connection, data):
    """Insert data into the database."""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO my_table (data) VALUES (%s)", (data,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def main():
    cnt = 0
    connection = create_connection()
    if connection is None:
        return

    create_table(connection)

    while True:
        cnt += 1
        time.sleep(1)
        if cnt == 30:
            print("Alive and kicking")
            insert_data(connection, "Alive and kicking")
            cnt = 0

if __name__ == "__main__":
    main()