from flask import flash, render_template, make_response, redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask import current_app as app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from .models import db, ShortCodes, User
from .forms import LoginForm, SearchForm
from . import admin, login_manager


# Create customized model view class
class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(CustomModelView(User, db.session))
admin.add_view(CustomModelView(ShortCodes, db.session))
# admin.add_view(ModelView(ShortCodes, db.session))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    For GET requests, display the login form.
    For POSTS, login the current user by processing the form.
    """
    form = LoginForm()
    if form.validate_on_submit():
        admin = User.query.get(form.username.data)
        if admin:
            if check_password_hash(admin.password, form.password.data):
                login_user(admin)
                return redirect(url_for("admin"))
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    logout_user()
    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    # if request.method == 'POST' and form.validate():
    if form.validate_on_submit():
        checkCode = ShortCodes.query.filter_by(full=form.full.data).first()
        if checkCode is None:
            newCode = ShortCodes(full=form.full.data)
            db.session.add(newCode)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            flash("URL already shortened, check the table.")
            return redirect(url_for("index"))
    return render_template("index.html", form=form, codes=ShortCodes.query.all())


@app.route("/<code>", methods=["GET"])
def code(code):
    shortCode = ShortCodes.query.filter_by(short=code).first_or_404(
        description="There is no URL with {} shortcode.".format(code)
    )
    shortCode.clicks += 1
    db.session.commit()
    return redirect(shortCode.full)


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("400.html"), 400)


@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(render_template("500.html"), 500)
