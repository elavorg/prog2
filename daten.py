import json

def speichern(animename, erscheinungsjahr, folgenanzahl, beschreibung):
    datei = "dict.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    with open(datei,"w") as open_file:
        json.dump(datei_inhalt, open_file)

