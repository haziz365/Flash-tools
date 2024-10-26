from termcolor import colored
import subprocess
import os
import time

def definir_titre_fenetre(titre):
    if os.name == 'nt':  # Windows uniquement
        os.system(f"title {titre}")

def afficher_banniere():
    print(colored('''
███████╗██╗      █████╗ ███████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
█████╗  ██║     ███████║███████╗███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║     ███████╗██║  ██║███████║██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                         By hamza (trouve le secret XD)
    ''', 'red'))

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def afficher_options():
    print(colored('        Network                       Discord                        Utile', 'red'))
    print(colored('╔═════════════════════════════════════════════════════════════════════════════════════════╗', 'red'))
    print(colored('║ I > Info              │ 7  > Discord Bot Server Nuker │ 14 > Virus builder              ║', 'red'))
    print(colored('║ 1 > Website scanner   │ 8  > Token Nuker              │ 15 > Soon                       ║', 'red'))
    print(colored('║ 2 > Sql scanner       │ 9  > Token Spammer            │ 16 > Soon                       ║', 'red'))
    print(colored('║ 3 > Phone lookup      │ 10 > Token login              │ 17 > Soon                       ║', 'red'))
    print(colored('║ 4 > Email tracker     │ 11 > Nitro gen                │ 18 > Soon                       ║', 'red'))
    print(colored('║ 5 > Ip lookup         │ 12 > Discord ID Token         │ 19 > Soon                       ║', 'red'))
    print(colored('║ 6 > IP Port Scanner   │ 13 > Soon                     │ 20 > Soon                       ║', 'red'))
    print(colored('╚═════════════════════════════════════════════════════════════════════════════════════════╝', 'red'))
    print(colored("Entrez 'q' pour quitter.", 'red'))

def demander_choix():
    prompt = '''
┌───(admin@Flash)─[~/Flash/v1]
└──$ '''
    return input(colored(prompt, 'red'))

def lancer_programme(choix):
    # Détermine le dossier de base où se trouve le script principal
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Dictionnaire des programmes avec chemins relatifs
    programs = {
        'I': os.path.join(base_dir, 'program', 'Info.py'),
        '1': os.path.join(base_dir, 'program', 'Website-Info-Scanner.py'),
        '2': os.path.join(base_dir, 'program', 'Website-Vulnerability-Scanner.py'),
        '3': os.path.join(base_dir, 'program', 'Phone-Number-Lookup.py'),
        '4': os.path.join(base_dir, 'program', 'Email-Tracker.py'),
        '5': os.path.join(base_dir, 'program', 'Ip-Lookup.py'),
        '6': os.path.join(base_dir, 'program', 'Ip-Port-Scanner.py'),
        '7': os.path.join(base_dir, 'program', 'Discord-Bot-Server-Nuker.py'),
        '8': os.path.join(base_dir, 'program', 'Discord-Token-Nuker.py'),
        '9': os.path.join(base_dir, 'program', 'Discord-Token-Spammer.py'),
        '10': os.path.join(base_dir, 'program', 'Discord-Token-Login.py'),
        '11': os.path.join(base_dir, 'program', 'Discord-Nitro-Generator.py'),
        '12': os.path.join(base_dir, 'program', 'Discord-Token-To-Id-And-Brute.py'),
        '14': os.path.join(base_dir, 'program', 'Virus-Builder.py'),
        '23112011': os.path.join(base_dir, 'program', 'Img', 'Ponice.py'),
    }
    
    if choix in programs:
        try:
            print(colored('Lancement du programme choisi...', 'red'))
            time.sleep(1)  
            subprocess.run(["python", programs[choix]], check=True)
        except subprocess.CalledProcessError as e:
            print(colored(f"Erreur lors de l'exécution du programme: {e}", 'red'))
    else:
        print(colored('Choix non valide. Veuillez entrer un numéro valide.', 'red'))

def main():
    definir_titre_fenetre("Flash tools ║ by Cid9kageno")
    while True:
        clear_screen()
        afficher_banniere()
        afficher_options()
        choix = demander_choix()
        if choix.lower() == 'q':
            print(colored('Fermeture du programme...', 'red'))
            break
        clear_screen()
        lancer_programme(choix)
        input(colored('Appuyez sur Enter pour retourner au menu...', 'red'))

if __name__ == "__main__":
    main()
