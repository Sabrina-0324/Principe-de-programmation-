from flask import Flask, jsonify, request
# Importation de Flask pour créer l'API
# jsonify pour retourner du JSON
# request pour lire les données envoyées par le client

app = Flask(__name__)
# Création de l'application Flask

# Liste des étudiants (données temporaires en mémoire)
students = [
    {"id": 1, "name": "youcef", "age": 21},
    {"id": 2, "name": "samir", "age": 41}
]

# Route principale
@app.route('/')
def home():
    # Message affiché quand on accède à /
    return "Bienvenue dans l'API de gestion des étudiants !"

# GET : récupérer tous les étudiants
@app.route('/students', methods=['GET'])
def get_students():
    # Retourne la liste des étudiants en format JSON
    return jsonify(students)

# POST : ajouter un nouvel étudiant
@app.route('/students', methods=['POST'])
def add_student():
    # Récupère les données envoyées en JSON
    new_student = request.get_json()
    # Ajoute un ID automatiquement
    new_student["id"] = len(students) + 1
    # Ajoute l'étudiant à la liste
    students.append(new_student)
    # Retourne l'étudiant créé avec le code 201
    return jsonify(new_student), 201

# GET : récupérer un étudiant par son ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    # Recherche de l'étudiant par ID
    student = next((s for s in students if s['id'] == id), None)
    if student:
        # Si trouvé, retourne l'étudiant
        return jsonify(student)
    # Sinon, message d'erreur
    return jsonify({"message": "Étudiant non trouvé"}), 404

# PUT : modifier un étudiant existant
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    # Recherche de l'étudiant
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        # Étudiant non trouvé
        return jsonify({"message": "Étudiant non trouvé"}), 404
    # Récupère les nouvelles données
    data = request.get_json()
    # Met à jour les informations
    student.update(data)
    # Retourne l'étudiant modifié
    return jsonify(student)

# DELETE : supprimer un étudiant
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    # Supprime l'étudiant avec l'ID donné
    students = [s for s in students if s['id'] != id]
    # Message de confirmation
    return jsonify({"message": "Étudiant supprimé"}), 200

# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)
    # debug=True permet de voir les erreurs facilement
