# Netheret help desk, step 01: setup

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step starts the project: a Flask app, a virtual environment, Git and a
folder layout.

## What this step adds

- `requirements.txt`: the two libraries the app uses, with their versions
  pinned so everybody installs the same ones.
- `helpdesk/__init__.py`: `create_app()`, the function that builds the app.
- `helpdesk/main.py`: one page, the home page, in a blueprint.
- `.gitignore`: the files Git should not track (the virtual environment,
  Python's cache and, later, the database).

## Run it

You need Python 3.10 or newer.

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Open http://127.0.0.1:5000 and you should see "The app is running."
`--debug` reloads the app when you save a file. Never use it on a real server.

## Folder layout

```
requirements.txt     the libraries to install
helpdesk/            the app itself (a Python package)
  __init__.py        create_app()
  main.py            general pages
```

Later steps add `helpdesk/templates/` for HTML, `helpdesk/static/` for CSS
and JavaScript, and one Python file per feature.

## What to look at

- How `create_app()` makes the app and registers the `main` blueprint.
- How `@bp.route("/")` connects an address to a Python function.

<!-- links -->
