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
    print(colored('║ 1 > Website scanner   │ 8  > Token Nuker              │ 15 > Soon B                     ║', 'red'))
    print(colored('║ 2 > Sql scanner       │ 9  > Token Spammer            │ 16 > Soon C                     ║', 'red'))
    print(colored('║ 3 > Phone lookup      │ 10 > Token login              │ 17 > Soon D                     ║', 'red'))
    print(colored('║ 4 > Email tracker     │ 11 > Nitro gen                │ 18 > Soon E                     ║', 'red'))
    print(colored('║ 5 > Ip lookup         │ 12 > Discord ID Token         │ 19 > Soon F                     ║', 'red'))
    print(colored('║ 6 > IP Port Scanner   │ 13 > Soon                     │ 20 > Soon G                     ║', 'red'))
    print(colored('╚═════════════════════════════════════════════════════════════════════════════════════════╝', 'red'))

def demander_choix():
    prompt = '''
┌───(admin@Flash)─[~/Flash/v1]
└──$ '''
    return input(colored(prompt, 'red'))

def lancer_programme(choix):
    programs = {
        'I': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Info.py',
        '1': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Website-Info-Scanner.py',
        '2': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Website-Vulnerability-Scanner.py',
        '3': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Phone-Number-Lookup.py',
        '4': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Email-Tracker.py',
        '5': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Ip-Lookup.py',
        '6': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Ip-Port-Scanner.py',
        '7': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\\Discord-Bot-Server-Nuker.py',
        '8': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Discord-Token-Nuker.py',
        '9': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Discord-Token-Spammer.py',
        '10': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Discord-Token-Login.py',
        '11': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Discord-Nitro-Generator.py',
        '12': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Discord-Token-To-Id-And-Brute.py',
        '14': 'C:\\Users\HP\\Desktop\Tools\\Flash tools\program\\Virus-Builder.py',
        # Ajoutez les nouveaux chemins pour les options supplémentaires ici
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
    definir_titre_fenetre("Flash tools ║ by Cid9kageno")  # Titre de la fenêtre
    clear_screen()
    afficher_banniere()
    afficher_options()
    choix = demander_choix()
    clear_screen()
    lancer_programme(choix)
    input(colored('Appuyez sur Enter pour fermer...', 'red'))

if __name__ == "__main__":
    main()
