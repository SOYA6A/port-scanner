# Port Scanner 📥

## Description
Un petit scanner de ports que j'ai codé pour apprendre les bases de la cybersécurité et la programmation réseau.

## Quel est ce projet ?
C'est un programme Python qui scanne les ports d'une adresse IP pour voir lesquels sont ouverts. J'ai fait cela afin de mieux comprendre comment fonctionnent les réseaux et les bases de la reconnaissance en sécurité informatique.

## Comment ça marche ?
Le programme demande :

- Une adresse IP (ou un nom de domaine)
- Un port de début
- Un port de fin


il vérifie tous les ports entre ces deux numéros pour voir s'ils sont ouverts ou fermés.


## Installation
```bash
git clone https://github.com/SOYA6A/port-scanner.git
cd port-scanner
python port-scanner.py
```
Pas besoin d'installer de librairies supplémentaires, j'utilise juste les modules Python de base.

## Exemple
```
Entrez l'adresse IP à scanner : scanme.org
Entrez le port de début : 1
Entrez le port de fin : 100

Port 33 ouvert
Port 77 ouvert
```
voici un autre exemple en image:
<img width="996" height="411" alt="Screenshot 2025-12-11 at 21 09 44" src="https://github.com/user-attachments/assets/33699315-8dfe-4831-8880-ee2f4f486249" />

## Ce que j'ai appris

- Comment utiliser les sockets en Python
- Les bases du protocole TCP/IP
- Le multi-threading pour accélérer le scan
- Comment structurer un programme Python
