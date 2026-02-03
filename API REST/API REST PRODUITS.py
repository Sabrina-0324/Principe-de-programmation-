from flask import Flask, jsonify, request
# Importation de Flask pour créer l'API
# jsonify pour retourner des données JSON
# request pour récupérer les données envoyées

app = Flask(__name__)
# Création de l'application Flask

# Liste des produits (données stockées en mémoire)
products = [
    {"id": 1, "name": "Stylo", "price": 10},
    {"id": 2, "name": "Cahier", "price": 50}
]

# Route principale
@app.route('/')
def home():
    # Message affiché sur la page d'accueil
    return "Bienvenue dans l'API de gestion des produits !"

# GET : récupérer tous les produits
@app.route('/products', methods=['GET'])
def get_products():
    # Retourne la liste des produits en JSON
    return jsonify(products)

# POST : ajouter un nouveau produit
@app.route('/products', methods=['POST'])
def add_product():
    # Récupère les données envoyées par le client
    new_product = request.get_json()
    # Ajoute un ID automatiquement
    new_product["id"] = len(products) + 1
    # Ajoute le produit à la liste
    products.append(new_product)
    # Retourne le produit créé
    return jsonify(new_product), 201

# GET : récupérer un produit par ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    # Recherche du produit par son ID
    product = next((p for p in products if p['id'] == id), None)
    if product:
        # Si trouvé, retourne le produit
        return jsonify(product)
    # Sinon, message d'erreur
    return jsonify({"message": "Produit non trouvé"}), 404

# PUT : modifier un produit
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    # Recherche du produit
    product = next((p for p in products if p['id'] == id), None)
    if not product:
        # Produit non trouvé
        return jsonify({"message": "Produit non trouvé"}), 404
    # Récupère les nouvelles données
    data = request.get_json()
    # Met à jour le produit
    product.update(data)
    # Retourne le produit modifié
    return jsonify(product)

# DELETE : supprimer un produit
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    # Supprime le produit avec l'ID donné
    products = [p for p in products if p['id'] != id]
    # Message de confirmation
    return jsonify({"message": "Produit supprimé"}), 200

# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)
    # debug=True affiche les erreurs pour faciliter le développement
