# Intro to Flask-Login

*Testing Flask-Login and Flask-Sqlalchemy libraries for my own purposes*

## Getting Started

First, the database and table needs to be created **before** running the program. If you fail to do this, you will need to delete your SQLite database and try again.

Open up python console on the root directory of the program and type the following commands.

```python
>>> from app import db, create_app
>>> db.create_all(app=create_app())
>>> exit()
```

From there, you should be able to run the app and evaluate it.
