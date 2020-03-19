from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from werkzeug.security import check_password_hash
from .models import db, User


# Define login and registration forms (for flask-login)
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.InputRequired()])
    password = PasswordField("Password", validators=[validators.InputRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError("Invalid user")

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError("Invalid password")

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", [validators.InputRequired(), validators.Length(min=4, max=25)]
    )
    email = StringField(
        "Email Address",
        [
            validators.InputRequired(),
            validators.Email(),
            validators.Length(min=6, max=35),
        ],
    )
    password = PasswordField(
        "New Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")

    def validate_login(self, field):
        if db.session.query(User).filter_by(username=self.username.data).count() > 0:
            raise validators.ValidationError("Duplicate username")


class SearchForm(FlaskForm):
    full = StringField(
        "URL",
        [
            validators.DataRequired(),
            validators.InputRequired(),
            validators.URL(require_tld=False),
        ],
    )
