import getpass
import hashlib
import re

# Lade die shadow Datei und gib sie zurück
def load_shadow_file():
    f = open("shadow")
    return f.read()


# Lade credentials (Login-Daten) und gib sie zurück
def load_credentials():
    line = load_shadow_file()
    return line.split(":")[0:2]


# speichere die shadow Datei
def save_shadow_file(username, password):
    line = ":".join([username, password])
    f = open("shadow", "w")
    f.write(line)


def show_username(username):
    print(f"Dein Username ist '{username}'.")


# Ändere das Passwort und gib es zurück
def change_password(oldPassword):
    # Da das Programm beendet wird, falls nicht erfolgreich, reicht das so
    input_current_password(oldPassword, "Gib dein altes Passwort ein: ")
    newPassword = input_password("Gib dein neues Passwort ein: ")
    while not\
            (len(newPassword) >= 5 and
             len(re.findall(r'[a-z]', newPassword)) > 0 and
             len(re.findall(r'[0-9]', newPassword)) > 0):
        print("Dein Passwort erfüllt die Richtlinien nicht.")
        print("Mindestens 5 Zeichen und es soll Kleinbuchstaben und Zahlen enthalten.")
        newPassword = input_password("Gib dein neues Passwort ein: ")
    return get_password_hash(newPassword)


# Berechne Passworthash
def get_password_hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# Verschleierte Passworteingabe
def input_password(prompt="Gib dein Passwort ein: "):
    return getpass.getpass(prompt)
    # getpass.getpass(prompt) ist identisch zu input(prompt) nur ohne Zeichendarstellung bei Eingabe


# Fragt das aktuelle Passwort Passwort ab
def input_current_password(password, prompt="Gib dein Passwort ein: "):
    maxPasswordTries = 3
    passwordTries = 0
    while passwordTries < maxPasswordTries:
        passwordTries += 1
        passwordTry = get_password_hash(input_password(prompt))
        if passwordTry == password:
            return True
        else:
            print("Passwort ist falsch, bitte erneut eingeben.)")
            print(f"Du hast noch {maxPasswordTries-passwordTries} Versuche.")
    exit()  # alternativ könnte man return False nutzen und weitere Dinge tun, nicht nur das Programm beenden


# Ändere den Usernamen und gib ihn zurück
def change_username():
    return input("Bitte gib einen neuen Usernamen ein: ")


# User-Anmeldung
# Gibt True zurück wenn erfolgreich, sonst False
def login(username, password):
    userInput = input("Gib deinen Usernamen an: ")
    passwordSuccess = input_current_password(password, "Gib dein Passwort an: ")
    if userInput == username and passwordSuccess:
        return True
    else:
        return False


# Menü-Hilfe anzeigen
def print_help():
    print("h: (Diese) Hilfe anzeigen")
    print("d: Zeige Usernamen an")
    print("p: Passwort ändern")
    print("u: Usernamen ändern")
    print("q: Quit / Programm beenden")


# Programmstart
# Lade User Zugangsdaten aus Datei
username, password = load_credentials()

# Login
while not login(username, password):
    print("Username oder Benutzer verkehrt, bitte probiere es erneut!")

print("Login erfolgreich!")

# Hauptschleife mit Abfrage, was getan werden soll
while True:
    choice = input("Was möchtest du tun? (Gib 'h' für Hilfe ein)\n> ")
    if choice == "h":  # help
        print_help()
    elif choice == "d":  # display
        show_username(username)
    elif choice == "p":  # password
        password = change_password(password)  # Parameter oldPassword = password
    elif choice == "u":  # user
        username = change_username()
    elif choice == "q":  # quit
        save_shadow_file(username, password)
        exit()
    else:
        print("Ich verstehe die Eingabe nicht.")


# TODO
# Mehrere Benutzer ermöglichen
    # User-ID einführen
# Angriff mit Doppelpunkt untersuchen
    # Funktion zum Überprüfen der shadow-Datei auf Korrektheit
# Logs erstellen
# 2FA (2-Faktor-Authentifizierung)
