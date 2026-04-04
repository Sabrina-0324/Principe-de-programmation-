   TP PHP MVC & API REST

Ce TP consiste à utiliser PHP pour consommer une API REST et afficher une liste d’étudiants.
Il permet de comprendre une organisation simple inspirée du modèle MVC (Model, View, Controller).


Le TP est structuré en plusieurs parties :

config/ : configuration de l’API
services/ : gestion des requêtes vers l’API
views/ : affichage des données
assets/ : style CSS
test_api*.php : fichiers de test
 
Principe
Les données sont récupérées depuis une API en JSON.
Le fichier StudentService envoie les requêtes HTTP (GET, POST, DELETE) et retourne les données.
Les données sont ensuite affichées dans une vue sans mélanger avec la logique.

API
URL : http://127.0.0.1:5000
Méthodes utilisées :
GET
POST
DELETE

Objectif
Comprendre le fonctionnement d’une API REST
Organiser le code en PHP
Séparer logique et affichage

Conclusion
Ce TP montre comment structurer simplement une application PHP et utiliser une API REST pour manipuler des données.