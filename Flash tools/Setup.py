import subprocess
import sys

# Liste des paquets à installer
packages = [
    "setuptools",
    "pyinstaller",
    "auto-py-to-exe",
    "urllib3",
    "PyQt5",
    "PyQtWebEngine",
    "colorama",
    "psutil",
    "keyboard",
    "requests",
    "dnspython",
    "deep-translator",
    "phonenumbers",
    "bcrypt",
    "beautifulsoup4",
    "pypiwin32",
    "whois",
    "cryptography",
    "screeninfo",
    "GPUtil",
    "pycryptodome",
    "discord.py",
    "discord",
    "Pillow",
    "browser-cookie3",
    "opencv-python",
    "pyautogui"
]

# Installation des paquets
for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
