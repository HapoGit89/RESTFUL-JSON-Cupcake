"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, redirect
from models import db, connect_db, Cupcake
from flask.json import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

with app.app_context():
    db.create_all()

def serialize_cupcake(cupcake):
    """Serialize cupcake for json parsing"""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }



@app.route("/api/cupcakes", methods = ["GET"])
def list_cupcakes():
    cakes = Cupcake.query.all()
    serialized_cupcakes = [serialize_cupcake(cake) for cake in cakes]
    return jsonify(cupcakes = serialized_cupcakes)

