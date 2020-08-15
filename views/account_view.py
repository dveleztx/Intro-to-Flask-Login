# Imports
from flask import Blueprint, render_template, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
# Custom Imports
from app import db
from data.users import User

blueprint = Blueprint("account", __name__, template_folder="templates")


@blueprint.route("/account", methods=["GET"])
@login_required
def account_get():
    return render_template("account/account.html", name=current_user.name)


@blueprint.route("/login", methods=["GET"])
def login_get():
    return render_template("account/login.html")


@blueprint.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if not (user and check_password_hash(user.password, password)):
        flash("Login incorrect. Try again.")
        return redirect("/login")

    login_user(user)

    return redirect("/account")


@blueprint.route("/register", methods=["GET"])
def register_get():
    return render_template("account/register.html")


@blueprint.route("/register", methods=["POST"])
def register_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
        flash("This account already exists.")
        return redirect("/register")

    new_user = User(name=name, email=email, password=generate_password_hash(password, method="sha256"))

    db.session.add(new_user)
    db.session.commit()

    return redirect("/login")


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
