# Flash tools ║ IP de Personne
import subprocess

# Code couleur rouge pour le texte
color_code = '\033[31m'
reset_code = '\033[0m'

def display_ips():
    ip_list = [
        ("nawelo", "81.51.17.129"),
        ("Riota", "76.65.187.156"),
        ("Natheo", "91.181.249.248"),
        ("Mathis", "90.27.130.211"),
        ("Thibault", "91.173.176.225"),
        ("Enis", "90.105.166.234"),
        ("Personne inconnu", "92.68.11.103"),
        ("Hacker", "72.195.34.58"),
    ]

    print(f"{color_code}Liste des adresses IP :{reset_code}")
    for name, ip in ip_list:
        print(f"{color_code}{name} : {ip}{reset_code}")

def run_program():
    # Chemin vers le programme à exécuter
    program_path = r"C:\\Users\\HP\Desktop\\Tools\\Flash tools\\program\\Config\\Main.py"
    subprocess.run(["python", program_path], shell=True)

def pause():
    input(f"{color_code}Appuyez sur Entrée pour continue{reset_code}")
    run_program()

if __name__ == "__main__":
    print(f"{color_code}Flash tools ║ IP de Personne{reset_code}")
    display_ips()
    pause()
