from flask import Flask, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

from .models import db

admin = Admin(name="itsTiny", template_mode="bootstrap3")
migrate = Migrate()
login_manager = LoginManager()


# Create customized index view class that handles login & registration
class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder="templates",
        static_folder="static",
    )

    app.config.from_object("config.ProdConfig")
    db.init_app(app)
    login_manager.init_app(app)

    admin.init_app(app, index_view=CustomAdminIndexView())

    migrate.init_app(app, db)

    with app.app_context():
        from . import routes

        # Create tables for our models
        # db.create_all()

        return app
