from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField
from wtforms.validators import InputRequired, Optional, Length

class RegisterForm(FlaskForm):
    """Register Form"""

    username = StringField("Username", validators=[InputRequired(message="What do you want to be called?")])
    password = PasswordField("Password", validators=[
        InputRequired(message="Password cannot be blank!"),
        Length(min=6, message="Password must be at least 6 characters long")])
    email = EmailField("Email", validators=[InputRequired(message="What is your email?")])
    wallet = IntegerField("Wallet", validators=[Optional()],
    default=1000,
    render_kw={"placeholder": "Fake money for trading simulator."}
    )
    profile_pic = StringField("Image", validators=[Optional()],
    render_kw={"placeholder": "Optional"})