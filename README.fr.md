# Centre d'assistance Netheret, étape 01 : mise en place

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape lance le projet : une application Flask, un environnement virtuel, Git et une organisation des dossiers.

## Ce que cette étape ajoute

- `requirements.txt` : les deux bibliothèques qu'utilise l'application, avec leurs versions
  épinglées pour que tout le monde installe les mêmes.
- `helpdesk/__init__.py` : `create_app()`, la fonction qui construit l'application.
- `helpdesk/main.py` : une seule page, la page d'accueil, dans un blueprint.
- `.gitignore` : les fichiers que Git ne doit pas suivre (l'environnement virtuel,
  le cache de Python et, plus tard, la base de données).

## Lancer l'application

Il vous faut Python 3.10 ou plus récent.

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Ouvrez http://127.0.0.1:5000 : vous devriez voir « The app is running. ».
`--debug` recharge l'application quand vous enregistrez un fichier. Ne l'utilisez jamais sur un vrai serveur.

## Organisation des dossiers

```
requirements.txt     the libraries to install
helpdesk/            the app itself (a Python package)
  __init__.py        create_app()
  main.py            general pages
```

Les étapes suivantes ajoutent `helpdesk/templates/` pour le HTML, `helpdesk/static/` pour le CSS
et le JavaScript, et un fichier Python par fonctionnalité.

## À regarder

- Comment `create_app()` crée l'application et enregistre le blueprint `main`.
- Comment `@bp.route("/")` relie une adresse à une fonction Python.

## Apprendre cette étape

Voici l'étape 1 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[Mettre en place un projet Flask](https://mitsurutech.co.uk/resources/t-level/dsd-t2-01-setup).

- Étape suivante : [étape 02, mise en page avec les gabarits Jinja et le CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
