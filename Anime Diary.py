from flask import Flask, render_template, request
import daten

app = Flask("Anime Diary")


#Aufrufen der Seite Hinzufuegen.html damit können neue Animes hinzugefügt werden.
@app.route("/hinzufuegen")
def anime_hinzufuegen():
    return render_template('Hinzufuegen.html', name="Anime Diary")

#hier soll nun die Eingabe des Animes gespeichert werden.
@app.route("/hinzufuegen/", methods=['GET', 'POST'])
def anime_speichern():
    if request.method == 'POST': #Die Post-Methode wird genutzt um die im "name" referierten Daten abzufangen und zu speichern.
        anime_name = request.form['animename']
        anime_erscheinungsjahr = request.form['erscheinungsjahr']
        anzahl_folgen = request.form['folgenanzahl']
        beschreibung = request.form['beschreibung']

        daten.speichern(anime_name, anime_erscheinungsjahr, anzahl_folgen, beschreibung)
        rueckgabe_string = "Der Anime " + anime_name + " wurde gespeichert!"
        return render_template('Hinzufuegen.html', rueckgabe_string=rueckgabe_string)
    else:
        return render_template('Hinzufuegen.html')




#in der Auswahl werden alle gespeicherten Animes angezeigt.
@app.route("/auswahl", methods=['GET', 'POST'])
def anime_auswahl():
    gespeicherte_animes = daten.anime_laden()
    return render_template('Auswahl.html', gespeicherte_animes=gespeicherte_animes)

#hier wird gerechnet wie lange man für den Anime in Stunden benötigt (pfad updaten ist veraltet)
@app.route("/updaten", methods=['GET', 'POST'])
def seriendauer():
    gespeicherte_animes = daten.anime_laden()
    if request.method == 'POST':
        serie = request.form['serie']
        def anzahlfolgen():
            for animename_key, value in gespeicherte_animes.items():
                if animename_key == serie:
                    for key, value2 in value.items():
                        if key == "Folgenanzahl":
                            return value2

        anzahlfolgen = anzahlfolgen()
        watchtime = str((int(anzahlfolgen) * 20)/60)
        watchtime2 = "Diese Serie dauert " + watchtime + " Stunden."
        return render_template('Updaten.html', gespeicherte_animes=gespeicherte_animes, watchtime2=watchtime2)

    liste = []
    for animename_key, value in gespeicherte_animes.items():
        for key, value2 in value.items():
            if key == "Animename":
                liste.append(value2)
    liste = set(liste)
    return render_template('Updaten.html', gespeicherte_animes=gespeicherte_animes, liste=liste)



if __name__ == "__main__":
    app.run(debug=True, port=5000)

