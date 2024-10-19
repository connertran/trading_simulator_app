from flask import Blueprint, flash, g, redirect, render_template, session

from forms.form import RegisterForm
from database.models import db, User

auth_db = Blueprint('auth', __name__)

##############################################################################
# Authentication: signup, login, logout
@auth_db.route('/register', methods=["GET", "POST"])
def show_register():
    """show register page"""
    default_profile_pic = "https://attic.sh/v3jwy6rymkctkjx3e2d1682dhc2l"

    form = RegisterForm()

    return render_template('register.html', form=form)