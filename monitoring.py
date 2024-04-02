# Fonction pour récupérer et afficher le nombre de clients
def get_customer_count():
    try:
        # Connexion à la base de données OpenCart
        connection = mysql.connector.connect(host='127.0.0.1',
                                             user='root',
                                             password='root',
                                             database='opencartdb')
        
        if connection.is_connected():
            # Création de l'objet Cursor pour exécuter des requêtes SQL
            cursor = connection.cursor()

            # Exécution de la requête pour récupérer le nombre de clients
            cursor.execute("SELECT COUNT(*) FROM oc_customer")
            customer_count = cursor.fetchone()[0]

            # Affichage du nombre de clients dans l'étiquette result_label
            result_label.config(text="Nombre de clients: {}".format(customer_count))

    except mysql.connector.Error as e:
        print('Erreur de connexion à la base de données:', e)

    finally:
        # Fermeture de la connexion à la base de données
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

# Fonction pour récupérer et afficher le nombre d'utilisateurs connectés
def get_online_user_count():
    try:
        # Connexion à la base de données OpenCart
        connection = mysql.connector.connect(host='localhost',
                                             user='votre_utilisateur',
                                             password='votre_mot_de_passe',
                                             database='votre_base_de_donnees')
        
        if connection.is_connected():
            # Création de l'objet Cursor pour exécuter des requêtes SQL
            cursor = connection.cursor()

            # Exécution de la requête pour récupérer le nombre d'utilisateurs connectés
            cursor.execute("SELECT COUNT(*) FROM oc_customer_online")
            online_user_count = cursor.fetchone()[0]

            # Affichage du nombre d'utilisateurs connectés dans l'étiquette result_label
            result_label.config(text="Nombre d'utilisateurs connectés: {}".format(online_user_count))

    except mysql.connector.Error as e:
        print('Erreur de connexion à la base de données:', e)

    finally:
        # Fermeture de la connexion à la base de données
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

# Fonction pour récupérer et afficher les produits depuis la base de données
def get_product_list():
    try:
        # Connexion à la base de données OpenCart
        connection = mysql.connector.connect(host='localhost',
                                             user='votre_utilisateur',
                                             password='votre_mot_de_passe',
                                             database='votre_base_de_donnees')
        
        if connection.is_connected():
            # Création de l'objet Cursor pour exécuter des requêtes SQL
            cursor = connection.cursor()

            # Exécution de la requête pour récupérer les produits
            cursor.execute("SELECT model FROM oc_product")
            products = cursor.fetchall()

            # Construction de la liste des produits
            product_list = '\n'.join([product[0] for product in products])

            # Affichage de la liste des produits dans l'étiquette result_label
            result_label.config(text="Liste des produits:\n{}".format(product_list))

    except mysql.connector.Error as e:
        print('Erreur de connexion à la base de données:', e)

    finally:
        # Fermeture de la connexion à la base de données
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

# Fonction pour effacer le texte de l'étiquette result_label
def clear_result_label():
    result_label.config(text="")
