# School API — README

## Description

Ce tp consiste à développer une API REST simple en utilisant Flask et MySQL. Le but principal est de comprendre comment une application web peut communiquer avec une base de données et exposer des données sous forme d’API. À travers ce TP, j’ai mis en place une petite application capable de gérer des étudiants en effectuant des opérations de consultation, d’ajout et de suppression.

## Organisation des fichiers

Le fichier **app.py** constitue le point d’entrée de l’application. Il sert à créer le serveur Flask et à définir les différentes routes de l’API. C’est lui qui reçoit les requêtes HTTP envoyées par le client et qui renvoie les réponses au format JSON.

Le fichier **config.py** contient les paramètres de connexion à la base de données MySQL. Il permet de centraliser les informations comme l’hôte, le port, l’utilisateur, le mot de passe et le nom de la base. Cette approche évite de répéter la configuration dans plusieurs fichiers.

Le fichier **db.py** est responsable de la création de la connexion vers MySQL. Il fournit une fonction réutilisable qui ouvre la connexion et gère les erreurs éventuelles. Les autres parties de l’application utilisent cette fonction pour accéder à la base de données.

Le fichier **repository.py** représente la couche d’accès aux données. Il contient les requêtes SQL nécessaires pour récupérer les étudiants, en ajouter de nouveaux ou en supprimer. Ce fichier sert d’intermédiaire entre l’application Flask et la base de données.

## Fonctionnement général

Le fonctionnement de l’application est simple. Lorsqu’un client envoie une requête vers l’API, le serveur Flask la reçoit d’abord. Ensuite, l’application appelle les fonctions du repository qui exécutent les requêtes SQL appropriées via la connexion fournie par le module de base de données. Une fois les données récupérées, elles sont renvoyées au client sous forme de réponse JSON. Cette séparation des responsabilités rend le code plus clair et plus facile à maintenir.

## Prérequis

Pour exécuter ce TP, il est nécessaire d’avoir Python installé ainsi qu’un serveur MySQL en fonctionnement. La base de données utilisée doit s’appeler **school_api** et contenir la table des étudiants. Il faut également installer les bibliothèques nécessaires comme Flask et le connecteur MySQL pour Python.

## Conclusion

Ce TP m’a permis de comprendre les bases de la création d’une API REST avec Flask, la connexion à une base de données MySQL et l’organisation d’une application en plusieurs couches. Il constitue une première étape vers le développement d’applications web plus complètes et mieux structurées.
