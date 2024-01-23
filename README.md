# Network Posts using Flask

This project is an attempt to reproduce a social network, just with posts and seeing the posts right after. The main idea is to remenber some concepts of flask, and how it evolved.

## Requirements

Just for the sake of this readme, install al dependencies.

```
    blinker==1.7.0
    click==8.1.7
    flask==3.0.1
    Flask-Cors==4.0.0
    importlib-metadata==7.0.1
    itsdangerous==2.1.2
    Jinja2==3.1.3
    MarkupSafe==2.1.4
    werkzeug==3.0.1
    zipp==3.17.0
```

## Database

To install the schema, go ahead and run the following code inside db_run/

```
python schema_runner.py
```

No need to install sqlite3, is already build-in.