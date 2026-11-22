# Servicio de asistencia de Netheret, paso 01: puesta en marcha

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso arranca el proyecto: una aplicación Flask, un entorno virtual, Git y una estructura de carpetas.

## Qué añade este paso

- `requirements.txt`: las dos bibliotecas que usa la aplicación, con sus versiones
  fijadas para que todo el mundo instale las mismas.
- `helpdesk/__init__.py`: `create_app()`, la función que construye la aplicación.
- `helpdesk/main.py`: una sola página, la de inicio, en un blueprint.
- `.gitignore`: los archivos que Git no debe seguir (el entorno virtual,
  la caché de Python y, más adelante, la base de datos).

## Ejecútalo

Necesitas Python 3.10 o una versión más nueva.

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Abre http://127.0.0.1:5000 y deberías ver "The app is running.".
`--debug` recarga la aplicación cuando guardas un archivo. No lo uses nunca en un servidor real.

## Estructura de carpetas

```
requirements.txt     the libraries to install
helpdesk/            the app itself (a Python package)
  __init__.py        create_app()
  main.py            general pages
```

Los pasos siguientes añaden `helpdesk/templates/` para el HTML, `helpdesk/static/` para el CSS
y el JavaScript, y un archivo de Python por cada funcionalidad.

## En qué fijarse

- Cómo `create_app()` crea la aplicación y registra el blueprint `main`.
- Cómo `@bp.route("/")` une una dirección con una función de Python.

## Aprende este paso

Este es el paso 1 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[Preparar un proyecto Flask](https://mitsurutech.co.uk/resources/t-level/dsd-t2-01-setup).

- Paso siguiente: [paso 02, diseño de página con plantillas Jinja y CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
