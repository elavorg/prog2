from flask import Flask, render_template, request
import daten

app = Flask("Anime Diary")

@app.route("/hinzufuegen")
def anime_hinzufuegen():
    return render_template('Hinzufuegen.html', name="Anime Diary")


@app.route("/hinzufuegen/", methods=['GET', 'POST'])
def anime_speichern():
    if request.method == 'POST':
        anime_name = request.form['animename']
        anime_erscheinungsjahr = request.form['erscheinungsjahr']
        anzahl_folgen = request.form['folgenanzahl']
        beschreibung = request.form['beschreibung']

        daten.speichern(anime_name, anime_erscheinungsjahr, anzahl_folgen, beschreibung)
        rueckgabe_string = "Der Anime " + anime_name + " wurde gespeichert!"
        return render_template('Hinzufuegen.html', anzeige=rueckgabe_string)
    else:
        return render_template('Hinzufuegen.html')





@app.route("/auswahl")
def watchlist_vorschlag():
    return render_template('Auswahl.html', vorschlag="Anime auswählen")

@app.route("/updaten")
def status_update():
    return render_template('Updaten.html', vorschlag="Status updaten")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

