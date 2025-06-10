# 📌 Rappels & Démarrage

## 📂 Outils & Rappels Pôle RH

### 🔹 Outils utilisés  
- **Metasploit** : Exploitation et tests d’intrusion  
- **Hydra** : Attaques par force brute sur services authentifiés  
- **OpenVAS** : Analyse des vulnérabilités réseau  
- **Wireshark** : Capture et analyse de trafic réseau  

💡 **Suggestion** : Collaborer avec les autres pôles pour enrichir les données collectées

---

## 🚀 Démarrage de l’environnement Docker

Pour lancer la toolbox complète en arrière-plan, exécutez la commande suivante :

```sh
sudo docker-compose up -d
```
## 📂 Structure du projet

Le projet est organisé de manière à faciliter la maintenance et l’intégration des outils :

- **`/scripts`**  
  Contient les scripts Python dédiés à chaque outil (Hydra, Metasploit, OpenVAS, Wireshark).  
  Chaque script lit les paramètres d’entrée, lance l’outil, et génère un fichier JSON résultat.

- **`/results`**  
  Dossier où sont stockés les fichiers JSON produits par les scripts, pour que l’interface web puisse les récupérer.

- **`Dockerfile`**  
  Définit l’environnement Docker avec tous les outils et dépendances nécessaires installés.

- **`main.py`** (optionnel)  
  Point d’entrée unique pour dispatcher les appels aux différents scripts en fonction du JSON reçu.

---

## ⚙️ Fonctionnement général

Le flux de travail global s’organise ainsi :

1. L’utilisateur renseigne les paramètres via l’interface web.  
2. L’interface web génère un fichier JSON avec ces paramètres et le transmet à la toolbox (via Docker, API, etc.).  
3. Le script Python correspondant au module ciblé lit ce JSON.  
4. Le script exécute l’outil avec les paramètres reçus.  
5. Les résultats sont formatés en JSON et sauvegardés dans `/results`.  
6. L’interface web récupère les résultats JSON pour affichage et analyse.

---

