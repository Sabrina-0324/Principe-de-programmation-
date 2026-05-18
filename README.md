Principe de Programmation

Ce dépôt regroupe les supports de cours ainsi que les travaux pratiques du module Principe de Programmation.
Les différents dossiers correspondent aux séances de cours (CM) et aux travaux pratiques (TP).

Structure du dépôt

Principe-de-programmation-/
│
├── API REST/              # API REST Flask (Python)
├── API+DAO/               # API REST avec accès base de données
├── TP1/                   # SOAP Java
├── TP2/                   # Consommation API REST en PHP
├── TP4/                   # REST + MySQL + Docker
├── docker-compose.yml     # Orchestration des services Docker
└── docker_notes.txt      # Notes de cours Docker
Contenu des séances
API REST (Python)

Mise en place d’une API REST simple avec Flask.

Création de routes GET / POST
Tests avec Postman
Manipulation de données via Python

Fichiers principaux :

app.py : point d’entrée de l’API
rest.py : exercices de base
students/products : exemples de ressources
API + DAO (Python + MySQL)

Introduction à la séparation des couches (DAO).

Connexion à une base MySQL
Requêtes SQL via repository
Organisation en architecture MVC simplifiée

Fichiers principaux :

app.py : contrôleur principal
db.py : connexion base de données
repository.py : requêtes SQL
config.py : paramètres de connexion
TP1 - SOAP (Java)

Découverte du protocole SOAP.

Création d’un service web Java
Tests de requêtes SOAP
Rédaction d’un rapport
TP2 - PHP + API REST

Consommation d’une API REST depuis PHP.

Appels HTTP GET
Affichage des données côté web
Communication entre PHP et API Flask
TP4 - Docker + MySQL

Mise en conteneurisation du projet.

Création d’un Dockerfile pour l’API
Utilisation de Docker Compose
Lancement d’une base MySQL + API
Orchestration des services
Docker
Lancer le projet avec Docker Compose
docker compose up --build
Services inclus
API REST (Flask)
Base de données MySQL
Technologies utilisées
Python (Flask)
PHP
Java
MySQL
Docker / Docker Compose
REST API
SOAP
Postman
