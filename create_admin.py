#!/usr/bin/env python3
"""Create a new admin user able to view the /reports endpoint."""
from getpass import getpass
import sys

from wsgi import app
from werkzeug.security import generate_password_hash
from app.models import db, User


def user():
    """Main entry point for script."""
    with app.app_context():
        if User.query.all():
            create = input("A user already exists! Create another? (y/n): ")
            if create == "n":
                return

        username = input("Enter username: ")
        password = getpass("Password: ")
        assert password == getpass("Password (again): ")

        if User.query.get(username):
            exists = input("Username already exists, try another one? (y/n): ")
            if exists == "n":
                return
            username = input("Enter username: ")
            password = getpass("Password: ")
            assert password == getpass("Password (again): ")

        admin = User(username=username, password=generate_password_hash(password))
        db.session.add(admin)
        db.session.commit()
        print("User created.")


if __name__ == "__main__":
    sys.exit(user())
