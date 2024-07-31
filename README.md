# Overview

- Test implementation of MMG in Flask

## Project Structure

```
flask-mmg/
    ├── app.py
    ├── templates/
    │   ├── login.html
    │   └── register.html
    ├── static/
    │   └── img/
    │       └── mmg-logo-small.png
    ├── user_data.csv
    └── requirements.txt
```

## Running it

```
    cd flask_app
    python -m venv .venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    python app.py
```