from flask import Flask, render_template, request

app = Flask("Hello World")

@app.route("/hinzufügen")
def watchlist_empfehlung():
    return render_template('Hinzufügen.html', name="Anime Diary")


@app.route("/hinzufügen", methods=['GET', 'POST'])
def erfassung_ausgeben():
    if request.method == 'GET':
        return render_template('Hinzufügen.html')
    if request.method == 'POST':
        erfasste_eingabe = request.form['Updaten.html']
        rueckgabe_string = "Eingaben für " + erfasste_eingabe + " werden gespeichert und der Filmauswahl hinzugefügt!"
        return rueckgabe_string


@app.route("/auswahl")
def watchlist_vorschlag():
    return render_template('Auswahl.html', vorschlag="Anime auswählen")

@app.route("/updaten")
def status_update():
    return render_template('Updaten.html', vorschlag="Status updaten")


@app.route("/test")
def test():
    return "passt!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)

