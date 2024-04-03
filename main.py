import tkinter as tk
from monitoring import connect_to_database

def afficher_produits():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT product_id, name, meta_title FROM oc_product_description")
            products = cursor.fetchall()

            for product in products:
                text_box.insert(tk.END, f"ID du produit : {product[0]}  -+-  Nom : {product[1]}  -+-  Titre : {product[2]}\n\n\n")

        finally:
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

def afficher_utilisateurs():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT firstname, username, code, ip, email FROM oc_user")
            utilisateurs = cursor.fetchall()

            for utilisateur in utilisateurs:
                text_box.insert(tk.END, f"Nom : {utilisateur[0]}  -+-  Groupe : {utilisateur[1]}  -+-  Code : {utilisateur[2]}  -+-  IP : {utilisateur[3]}  -+-  Email : {utilisateur[4]}\n\n\n")

        finally:
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

def afficher_utilisateurs_connectes():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT user_login_id, ip, date_added FROM oc_user_login")
            users = cursor.fetchall()

            for user in users:
                text_box.insert(tk.END, f"ID : {user[0]}  -+-  IP : {user[1]}  -+-  Date Ajoutée : {user[2]}\n\n\n")

        finally:
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')

def afficher_transactions():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT customer_id, order_id, amount FROM oc_customer_transaction")
            transactions = cursor.fetchall()

            for transaction in transactions:
                text_box.insert(tk.END, f"ID du client : {transaction[0]}  -+-  ID de la commande : {transaction[1]}  -+-  Montant : {transaction[2]}\n\n\n")

        finally:
            cursor.close()
            connection.close()
            print('Connexion MySQL fermée')


root = tk.Tk()
root.title("MonitoringApp")
root.config(bg='blue')

b1 = tk.Button(root, text="Produits", command=afficher_produits, bg='white', fg='blue')
b1.grid(row=0, column=0)

b2 = tk.Button(root, text="Administrateurs", command=afficher_utilisateurs, bg='white', fg='blue')
b2.grid(row=0, column=1)

b3 = tk.Button(root, text="Utilisateurs Connectés", command=afficher_utilisateurs_connectes, bg='white', fg='blue')
b3.grid(row=0, column=2)

b4 = tk.Button(root, text="Transactions", command=afficher_transactions, bg='white', fg='blue')
b4.grid(row=0, column=3)

text_box = tk.Text(root, width=150, height=30)
text_box.grid(row=1, column=0, columnspan=4)

root.mainloop()
