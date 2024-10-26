# Flash tools ║ by Cid9kageno
import subprocess

# Code couleur rouge pour le texte
color_code = '\033[31m'
reset_color = '\033[0m'

# Définissez le chemin de vos programmes ici
program_1_path = r"C:\\Users\\HP\Desktop\\Tools\\Flash tools\\program\\Personne.py"
program_2_path = r"C:\\Users\\HP\Desktop\\Tools\\Flash tools\\program\\siteweb.py"

def program_1():
    print(f"{color_code}Exécution.{color_code}")
    subprocess.run(["python", program_1_path], shell=True)  # Exécution du programme 1

def program_2():
    print(f"{color_code}Exécution{color_code}")
    subprocess.run(["python", program_2_path], shell=True)  # Exécution du programme 2

def main_menu():
    print(f"{color_code}Flash tools ║ by Cid9kageno{color_code}")
    print("1. Ip de personne")
    print("2. Ip de site web")
    print("0. Quitter")

    # Invite de commande Kali Linux personnalisée
    prompt = "┌───(admin@Flash)─[~/Flash/v1]\n└──$ "
    
    choice = input(prompt)

    if choice == '1':
        program_1()
    elif choice == '2':
        program_2()
    elif choice == '0':
        print(f"{color_code}Au revoir!{color_code}")
    else:
        print(f"{color_code}Choix invalide, veuillez réessayer.{color_code}")
        main_menu()

if __name__ == "__main__":
    main_menu()
