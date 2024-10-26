# Flash tools ║ IP de Personne
import subprocess

# Code couleur rouge pour le texte
color_code = '\033[31m'
reset_code = '\033[0m'

def display_ips():
    ip_list = [
        ("https://www.cned.fr", "51.11.239.227 / Port : 80"),
        ("https://www.youtube.com", "216.58.209.78 / Port : 80"),
    ]

    print(f"{color_code}Liste des adresses IP :{reset_code}")
    for name, ip in ip_list:
        print(f"{color_code}{name} : {ip}{reset_code}")

def run_program():
    # Chemin vers le programme à exécuter
    program_path = r"C:\\Users\\HP\Desktop\\Tools\\Flash tools\\program\\Config\\Main.py"
    subprocess.run(["python", program_path], shell=True)

def pause():
    input(f"{color_code}Appuyez sur Entrée pour Continue.{reset_code}")
    run_program()

if __name__ == "__main__":
    print(f"{color_code}Flash tools ║ IP de Site web{reset_code}")
    display_ips()
    pause()
