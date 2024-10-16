import datetime
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

class Stock(db.Model):
    """Stock model."""
    __tablename__ = "stocks"

    stock_code = db.Column(db.Text,
                         primary_key=True,
                         unique=True,
                         nullable=False)
    stock_name = db.Column(db.Text,
                         nullable=False)
    
class Exit(db.Model):
    """Exit model."""
    __tablename__ = "exits"

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    stock_code = db.Column(db.Text, 
                        db.ForeignKey('stocks.stock_code', ondelete="cascade"), 
                        nullable=False)
    user_username = db.Column(db.Text, 
                        db.ForeignKey('users.username', ondelete="cascade"), 
                        nullable=False)
    stock_value = db.Column(db.Text,
                        nullable=False)
    time = db.Column(db.DateTime,
                        nullable=False,
                        default=datetime.datetime.now)


class Enter(db.Model):
    """Enter model."""
    __tablename__ = "enters"

    id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)
    stock_code = db.Column(db.Text, 
                        db.ForeignKey('stocks.stock_code', ondelete="cascade"), 
                        nullable=False)
    user_username = db.Column(db.Text, 
                        db.ForeignKey('users.username', ondelete="cascade"), 
                        nullable=False)
    stock_value = db.Column(db.Text,
                         nullable=False)
    time = db.Column(db.DateTime,
                          nullable=False,
                          default=datetime.datetime.now)
    
class Trade(db.Model):
    """Trade model."""
    __tablename__ = "trades"

    id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)
    user_username = db.Column(db.Text, 
                        db.ForeignKey('users.username', ondelete="cascade"), 
                        nullable=False)
    enter_id = db.Column(db.Integer, 
                        db.ForeignKey('enters.id', ondelete="cascade"), 
                        nullable=False)
    exit_id = db.Column(db.Integer, 
                        db.ForeignKey('exits.id', ondelete="cascade"), 
                        nullable=False)
    
class WishList(db.Model):
    """Wish list model."""
    __tablename__ = "wish_list"

    id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)
    user_username = db.Column(db.Text, 
                        db.ForeignKey('users.username', ondelete="cascade"), 
                        nullable=False)
    stock_code = db.Column(db.Text, 
                        db.ForeignKey('stocks.stock_code', ondelete="cascade"), 
                        nullable=False)