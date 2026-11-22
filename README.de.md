# Netheret-Helpdesk, Schritt 01: Einrichtung

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt beginnt das Projekt: eine Flask-Anwendung, eine virtuelle Umgebung, Git und eine Ordnerstruktur.

## Was dieser Schritt hinzufügt

- `requirements.txt`: die beiden Bibliotheken, die die Anwendung verwendet, mit festgelegten
  Versionen, damit alle dieselben installieren.
- `helpdesk/__init__.py`: `create_app()`, die Funktion, die die Anwendung baut.
- `helpdesk/main.py`: eine einzige Seite, die Startseite, in einem Blueprint.
- `.gitignore`: die Dateien, die Git nicht verfolgen soll (die virtuelle Umgebung,
  den Cache von Python und später die Datenbank).

## Starten

Sie brauchen Python 3.10 oder neuer.

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Öffnen Sie http://127.0.0.1:5000, und Sie sollten „The app is running.“ sehen.
`--debug` lädt die Anwendung neu, wenn Sie eine Datei speichern. Verwenden Sie es nie auf einem echten Server.

## Ordnerstruktur

```
requirements.txt     the libraries to install
helpdesk/            the app itself (a Python package)
  __init__.py        create_app()
  main.py            general pages
```

Spätere Schritte fügen `helpdesk/templates/` für HTML, `helpdesk/static/` für CSS
und JavaScript sowie eine Python-Datei pro Funktion hinzu.

## Worauf Sie achten sollten

- Wie `create_app()` die Anwendung erstellt und den Blueprint `main` registriert.
- Wie `@bp.route("/")` eine Adresse mit einer Python-Funktion verbindet.

## Diesen Schritt lernen

Dies ist Schritt 1 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[Ein Flask-Projekt einrichten](https://mitsurutech.co.uk/resources/t-level/dsd-t2-01-setup).

- Nächster Schritt: [Schritt 02, Seitenlayout mit Jinja-Vorlagen und CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
