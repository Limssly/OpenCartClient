import mysql.connector

def connect_to_database():
    try:
        # Connect to the OpenCart database
        connection = mysql.connector.connect(host='127.0.0.1',
                                             user='root',
                                             password='root',
                                             database='opencartdb')
        return connection
    except mysql.connector.Error as e:
        print('Erreur de connexion à la base de données:', e)
        return None
