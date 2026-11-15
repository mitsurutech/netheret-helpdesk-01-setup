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

## Learn this step

This is step 1 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[Setting up a Flask project](https://mitsurutech.co.uk/resources/t-level/dsd-t2-01-setup).

- Next step: [step 02, page layout with jinja templates and css](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.

