from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

#models go below here
class User(db.Model):
    """User model."""
    __tablename__ = "users"

    username = db.Column(db.Text,
                         primary_key=True,
                         unique=True,
                         nullable=False)
    password = db.Column(db.Text,
                         nullable=False)
    email = db.Column(db.String(50),
                      nullable=False)
    wallet = db.Column(db.Float,
                       nullable=False,
                       default=1000)
    is_admin = db.Column(db.Boolean, default=False)