import tkinter as tk
from tkinter import ttk
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

notebook = ttk.Notebook(root)

# Crée un Frame pour chaque onglet
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

notebook.add(tab1, text='Produits')
notebook.add(tab2, text='Administrateurs')
notebook.add(tab3, text='Utilisateurs Connectés')
notebook.add(tab4, text='Transactions')

notebook.pack(expand=1, fill='both')

# Ajoute les boutons spécifiques à chaque onglet
b1 = tk.Button(tab1, text="Produits", command=afficher_produits, bg='white', fg='blue')
b1.pack()
text_box = tk.Text(tab1, height=10, width=40)
text_box.pack()

b2 = tk.Button(tab2, text="Administrateurs", command=afficher_utilisateurs, bg='white', fg='blue')
b2.pack()
text_box = tk.Text(tab2, height=10, width=40)
text_box.pack()

b3 = tk.Button(tab3, text="Utilisateurs Connectés", command=afficher_utilisateurs_connectes, bg='white', fg='blue')
b3.pack()
text_box = tk.Text(tab3, height=10, width=40)
text_box.pack()

b4 = tk.Button(tab4, text="Transactions", command=afficher_transactions, bg='white', fg='blue')
b4.pack()
text_box = tk.Text(tab4, height=10, width=40)
text_box.pack()

root.mainloop()
