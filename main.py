import getpass
import hashlib

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
    if input_password(oldPassword, "Wie ist dein altes Passwort: ") == oldPassword:
        newInput = getpass.getpass("Gib dein neues Passwort ein: ")
        # in newInput sollen mindestens 5 Zeichen sein
        newPassword = hashlib.sha256(newInput.encode("utf-8")).hexdigest()
    return newPassword


# Passwort wird automatisch gehasht und dann als String zurückgegeben
def input_password(password, prompt="Gib dein Passwort ein: "):
    maxPasswordTries = 3
    passwordTries = 0
    while passwordTries < maxPasswordTries:
        passwordTries += 1
        passwordTry = hashlib.sha256(getpass.getpass(prompt).encode("utf-8")).hexdigest()
        # getpass.getpass(prompt) ist identisch zu input(prompt) nur ohne Zeichendarstellung bei Eingabe
        if passwordTry == password:
            return passwordTry
        else:
            print("Passwort ist falsch, bitte erneut eingeben.)")
            print(f"Du hast noch {maxPasswordTries-passwordTries} Versuche.")
    exit()


# Ändere den Usernamen und gib ihn zurück
def change_username():
    return input("Bitte gib einen neuen Usernamen ein: ")


# User-Anmeldung
# Gibt True zurück wenn erfolgreich, sonst False
def login(username, password):
    userInput = input("Gib deinen Usernamen an: ")
    passwordInput = input_password(password, "Gib dein Passwort an: ")
    if userInput == username and passwordInput == password:
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
# Passwortanforderungen
# Mehrere Benutzer ermöglichen
