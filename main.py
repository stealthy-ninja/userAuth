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
    while input("Wie ist dein altes Passwort: ") != oldPassword:
        print("Passwort stimmt nicht, bitte versuche es erneut!")
    return input("Bitte gib ein neues Passwort ein: ")


# Ändere den Usernamen und gib ihn zurück
def change_username():
    return input("Bitte gib einen neuen Usernamen ein: ")


# User-Anmeldung
# Gibt True zurück wenn erfolgreich, sonst False
def login(username, password):
    userInput = input("Gib deinen Usernamen an: ")
    passwordInput = input("Gib dein Passwort an: ")
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
        password = change_password(password)
    elif choice == "u":  # user
        username = change_username()
    elif choice == "q":  # quit
        save_shadow_file(username, password)
        exit()
    else:
        print("Ich verstehe die Eingabe nicht.")


# TODO
# Verschlüsseln/Hashwert (Passwort)
# Passworteingabe verschleiern (**** statt Klartext)
# Nach X falschen Passworteingaben Programm beenden
# Passwortanforderungen