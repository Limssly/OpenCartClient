import mysql.connector

# Configuration de la connexion à la base de données OpenCart
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'opencartdb'
}

# Fonction pour capturer et afficher les requêtes SQL
def execute_and_log_query(query, args=None):
    try:
        print("Executing query:", query)
        cursor.execute(query, args)
        connection.commit()
    except mysql.connector.Error as e:
        print('Erreur execution de la requête:', e)

# Connexion à la base de données
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('Connexion à la base de données réussie !')

        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            print(table)

except mysql.connector.Error as e:
    print('Erreur de connexion à la base de données:', e)

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print('Base de données fermée')
