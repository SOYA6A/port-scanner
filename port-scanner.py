import socket # Importer la bibliothèque 'socket' pour gérer les connexions réseau
from concurrent.futures import  # Importer pour exécuter plusieurs tâches en même temps

def scan_port(ip, port):
    """
    Fonction qui vérifie si un port est ouvert sur une adresse IP donnée.

    Arguments :
    ip -- L'adresse IP que nous voulons scanner
    port -- Le port que nous voulons vérifier
    """
    # Créer un objet 'socket' qui nous permettra de se connecter
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)# Définir un délai d'attente de 1 seconde pour la connexion
        # Essayer de se connecter au port donné sur l'adresse IP
        result = sock.connect_ex((ip, port))
        # Vérifier si la connexion a réussi
        if result == 0:
            print(f"Port {port} ouvert") # si le port est ouvert, l'afficher
        else:
            print(f"Port {port} fermé") # si le port est fermé, l'afficher 

def main():
    """
    Fonction principale qui exécute le scanner de ports.
    """
    # Demander à l'utilisateur de saisir l'adresse IP à scanner
    ip = input("Entrez l'adresse IP à scanner : ")
    # Demander a l'utilisateur de saisir le port de début 
    start_port = int(input("Entrez le port de début : "))
    # Demander à l'utilisateur de saisir le port de fin 
    end_port = int(input("Entrez le port de fin : "))

# Utiliser ThreadPoolExecutor pour scanner plusieurs ports en même temps
    with ThreadPoolExecutor(max_workers=100) as executor:
        # à travers tous les ports de la place spécifiée
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port) #lancer la vérification du port 
# Cette condition vérifie si le script est exécuté directement
if __name__ == "__main__":
    main() #appeler la fonction principale pour démarrer le programme 