#import os is for the environment variables (are used when deploying)
import os
from flask import Flask, redirect, render_template, session, flash, request, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension

# when the create_app function is not created to wrap the whole code inside
    #run "flask run" to run the flask app
# Run this with "python -m app" in the command line

# def create_app(database_name, testing=False):
app = Flask(__name__)

# on Render, set the DATABASE_URL environment variable to the database connection string gotten from ElephantSQL.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", f"postgresql:///{'trading_db'}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.debug is to turn on or turn off the debug tool bar on the right hand side of the browser.
app.debug = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
#for wtf form testing => will deal with this later ....
# if testing:
#     app.config["WTF_CSRF_ENABLED"] = False
#     app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)


##############################################################################

#homepage
@app.route('/')
def show_homepage():
    """show homepage"""
    return render_template('index.html')

#     return app
# if __name__ == '__main__':
#     app = create_app('trading_db')
#     app.run(debug=True)
##################################################

# from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension

# app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)

# # homepage
# @app.route('/')
# def show_homepage():
#     """show homepage"""
#     return render_template('index.html')