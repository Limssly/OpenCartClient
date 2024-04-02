import mysql.connector

# Configuration de la connexion à la base de données OpenCart
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'opencartdb'
}

# Connexion à la base de données
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('Connected to MySQL database')

        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            print(table)

except mysql.connector.Error as e:
    print('Error connecting to MySQL database:', e)

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
