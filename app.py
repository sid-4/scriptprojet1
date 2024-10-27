from flask import Flask, jsonify
from pymongo import MongoClient

# Initialisation de l'application Flask
app = Flask(__name__)

# Route de base pour vérifier le fonctionnement de l'API
@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur l'API !"

# Connexion à MongoDB
client = MongoClient("mongodb+srv://sidgasmi04:xnBHZ6mXFBdZFnsG@cluster0.4gipc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Remplacez par votre URI MongoDB
db = client['ProjetSessionScriptDB']  # Remplacez par le nom de votre base de données
users_collection = db['Users']  # Remplacez par le nom de votre collection

# Endpoint pour récupérer tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        user['_id'] = str(user['_id'])  # Convertit l'ObjectId en chaîne de caractères
        users.append(user)
    return jsonify(users)

# Lancer le serveur en mode débogage pour plus de détails en cas d'erreur
if __name__ == '__main__':
    app.run(debug=True)
