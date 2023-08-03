---
title: Flaskr
---

The basic blog app built in the Flask
[tutorial](https://flask.palletsprojects.com/tutorial/).

# Install

Activate a virtual environment with Poetry and install the dependencies:

```
$ poetry shell
$ poetry install
```

# Run

```
$ flask --app flaskr init-db
$ flask --app flaskr run --debug
```

Open <http://127.0.0.1:5000> in a browser.

# Test

```
$ pip install '.[test]'
$ pytest
```

Run with coverage report:

```
$ coverage run -m pytest
$ coverage report
$ coverage html  # open htmlcov/index.html in a browser
```
