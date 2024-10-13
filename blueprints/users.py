from flask import Blueprint, flash, g, redirect, render_template, session


users_bp = Blueprint('users', __name__)

##############################################################################

#app user's routes
@users_bp.route('/')
def show_homepage():
    """show homepage"""
    return render_template('homepage.html')