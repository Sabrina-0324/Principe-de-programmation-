TP Conteneurisation : Architecture Micro-services (Python & PHP)

Contexte du projet
Ce projet a pour objectif de mettre en place une architecture micro-services avec Docker.
L’application est séparée en deux parties : un back-end (API) et un front-end (site web), chacun dans un conteneur différent.

Architecture
Le projet contient deux services :

Service 1 : API (Python Flask)
Une API REST qui permet de gérer une liste d’étudiants.

Service 2 : Site Web (PHP)
Un site web qui récupère les données de l’API et les affiche.

Détails des services

API Python
Fichiers utilisés : api.py, requirements.txt, Dockerfile
Rôle : gérer des étudiants (ajouter, afficher, modifier, supprimer)
Port interne : 5000
Image Docker : python:3.12-slim

Fonctionnalités de l’API :

GET /students : afficher tous les étudiants
POST /students : ajouter un étudiant
GET /students/{id} : afficher un étudiant
PUT /students/{id} : modifier un étudiant
DELETE /students/{id} : supprimer un étudiant

Site Web PHP
Fichier utilisé : index.php
Rôle : afficher les données des étudiants depuis l’API
Méthode utilisée : file_get_contents
Port interne : 80
Image Docker : php

Docker Compose
Le fichier docker-compose.yml permet de lancer les deux services ensemble.

Fonctionnalités :

Communication entre les conteneurs
Le site PHP appelle l’API avec http://product-service/
Utilisation de volumes pour modifier le code sans redémarrer
Gestion des ports

Accès aux services :
API : http://localhost:5001
Site web : http://localhost:5002

Installation

Pré-requis

Docker installé
Docker Compose installé
Git installé

Lancer le projet
docker-compose up --build

Arrêter le projet
docker-compose down

Étapes du TP

Étape 1 : création d’une API Flask simple pour gérer des étudiants
Étape 2 : création du Dockerfile
Étape 3 : ajout du service PHP avec Docker Compose
Étape 4 : communication entre les services
Étape 5 : publication sur GitHub

Résat final

API accessible sur http://localhost:5001
Site web accessible sur http://localhost:5002

Conclusion

Ce TP permet de comprendre la conteneurisation, les micro-services et l’utilisation de Docker Compose.