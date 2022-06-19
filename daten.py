import json


def speichern(keyword, animename, erscheinungsjahr, folgenanzahl, beschreibung):
    datei = "dict.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(keyword)] = {'Animename': animename,
                                    'Erscheinungsjahr': erscheinungsjahr,
                                    'Folgenanzahl': folgenanzahl,
                                    'Beschreibung': beschreibung}

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def anime_speichern(animename, erscheinungsjahr, folgenanzahl, beschreibung):
    datei_name = "dict_2.json"
    speichern(datei_name, animename, erscheinungsjahr, folgenanzahl, beschreibung)
    return animename, erscheinungsjahr, folgenanzahl, beschreibung

def anime_laden():
    datei_name = "dict_2.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt