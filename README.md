#  Principe de Programmation 

Ce dépôt regroupe les supports de cours ainsi que les travaux pratiques du module Principe de Programmation (Master 1 Informatique).

Les dossiers correspondent aux séances de cours (CM) et aux travaux pratiques (TP).

---

## Structure du dépôt

```bash
Principe-de-programmation-/
│
├── API REST/            # API REST Flask (Python)
├── API+DAO/             # API REST avec base de données MySQL
├── TP1/                 # SOAP Java
├── TP2/                 # Consommation API REST en PHP
├── TP4/                 # REST + MySQL + Docker
├── docker-compose.yml   # Orchestration Docker
└── docker_notes.txt     # Notes de cours Docker
```

---

## Contenu des séances

### API REST (Python - Flask)

Mise en place d’une API REST simple avec Flask.

**Objectifs :**
- Création de routes (GET, POST)
- Tests avec Postman
- Manipulation de données en Python

**Fichiers principaux :**
- `app.py` → point d’entrée de l’API  
- `rest.py` → exercices de base  
- `students/`, `products/` → exemples de ressources  

---

### API + DAO (Python + MySQL)

Introduction à l’architecture avec séparation des couches.

**Objectifs :**
- Connexion à une base MySQL
- Organisation en DAO (Data Access Object)
- Requêtes SQL structurées

**Fichiers principaux :**
- `app.py` → contrôleur principal  
- `db.py` → connexion base de données  
- `repository.py` → requêtes SQL  
- `config.py` → paramètres de connexion  

---

### TP1 - SOAP (Java)

Découverte du protocole SOAP.

**Objectifs :**
- Création d’un service web en Java
- Tests de requêtes SOAP
- Compréhension des services web classiques  

---

### TP2 - PHP + API REST

Consommation d’une API REST depuis PHP.

**Objectifs :**
- Appels HTTP (GET)
- Affichage dynamique des données
- Communication entre PHP et API Flask  

---

### TP4 - Docker + MySQL + API

Conteneurisation complète du projet.

**Objectifs :**
- Création d’un Dockerfile
- Utilisation de docker-compose
- Lancement API + base de données MySQL

**Démarrage :**
```bash
docker compose up --build
```

**Services :**
- API REST (Flask)
- Base de données MySQL  

---

## Technologies utilisées

- Python (Flask)
- PHP
- Java
- MySQL
- Docker / Docker Compose
- REST API
- SOAP
- Postman
