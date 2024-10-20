#import os is for the environment variables (are used when deploying)
import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from database.models import db, connect_db

from blueprints.users import users_bp
from blueprints.auth import auth_db

# Run this with "python -m app" in the command line

def create_app(testing=False):
    app = Flask(__name__)

    # on Render, set the DATABASE_URL environment variable to the database connection string gotten from ElephantSQL.
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", f"postgresql://postgres:1234@localhost:5432/trading_db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    # app.debug is to turn on or turn off the debug tool bar on the right hand side of the browser.
    app.debug = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    #for wtf form testing => will deal with this later ....
    if testing:
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    debug = DebugToolbarExtension(app)

    connect_db(app)
    #Migrate will handle creating database tables and update them, if there're changes in models.py
    Migrate(app, db)
    ##############################################################################

    app.register_blueprint(users_bp)
    app.register_blueprint(auth_db)

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)