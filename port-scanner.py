import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} ouvert")
        else:
            print(f"Port {port} fermé")

def main():
    ip = input("Entrez l'adresse IP à scanner : ")
    start_port = int(input("Entrez le port de début : "))
    end_port = int(input("Entrez le port de fin : "))

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    main()