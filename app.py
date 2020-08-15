#!/usr/bin/python3
###############################################################################
# Script      : app.py
# Author      : David Velez
# Date        : 8/14/2020
# Description : Flask-Login Introduction
###############################################################################

# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def main():
    app = create_app()
    app.run(debug=True)


def create_app():
    app = Flask(__name__)

    db_loc = "C:\\Users\\dvele\\PycharmProjects\\flask-login\\intro\\db\\db.sqlite3"

    app.config["SECRET_KEY"] = "thisisthesecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_loc}"
    db.init_app(app)
    lm = LoginManager()
    lm.login_view = "/login"
    lm.init_app(app)

    from data.users import User

    @lm.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from views import home_view
    from views import account_view

    app.register_blueprint(home_view.blueprint)
    app.register_blueprint(account_view.blueprint)

    return app


if __name__ == "__main__":
    main()
