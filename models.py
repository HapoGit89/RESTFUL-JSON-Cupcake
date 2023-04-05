"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Cupcake (db.Model):
    """Cupcake"""

    ___tablename___ = "cupcakes"

    def __repr__(self):
        """ Cupcake Info"""
        c = self
        return (f"Cupcake {c.id}, flavor: {c.flavor}, size: {c.size}")

    id = db.Column(db.Integer, primary_key = True,
                   autoincrement = True)
    flavor = db.Column (db.String(30))
    size = db.Column(db.String(30))
    rating = db.Column(db.Float)
    image = db.Column(db.Text, default = "https://tinyurl.com/demo-cupcake")

