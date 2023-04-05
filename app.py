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
    """Shows List of all cakes"""
    cakes = Cupcake.query.all()
    serialized_cupcakes = [serialize_cupcake(cake) for cake in cakes]
    return (jsonify(cupcakes = serialized_cupcakes),200)

@app.route("/api/cupcakes/<id>")
def list_cupcake(id):
    """ Shows Cupcake of id id"""
    cake = Cupcake.query.get_or_404(id)
    cake_serialized = serialize_cupcake(cake)
    return (jsonify(cupcake = cake_serialized),200)


@app.route("/api/cupcakes", methods = ["POST"])
def create_cupcake():
    """creates cupcake"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    try:
        image = request.json["image"]
    except:
        image = "https://images.eatsmarter.de/sites/default/files/styles/max_size/public/cupcake-mit-rosa-creme-435108.jpg"
   
    cake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)
    
    db.session.add(cake)
    db.session.commit()
    cake_ser = serialize_cupcake(cake)
    return (jsonify(cupcake=cake_ser), 201)

