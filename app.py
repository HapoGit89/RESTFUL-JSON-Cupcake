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


@app.route("/")
def show_start_page():
    return render_template("start.html")

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
        image = "https://tinyurl.com/demo-cupcake"
    cake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)
    
    db.session.add(cake)
    db.session.commit()
    cake_ser = serialize_cupcake(cake)
    return (jsonify(cupcake=cake_ser), 201)

@app.route("/api/cupcakes/<id>", methods = ["PATCH"])
def update_cupcake(id):
    cake = Cupcake.query.get_or_404(id)
    cake.flavor = request.json["flavor"]
    cake.size = request.json["size"]
    cake.rating = request.json["rating"]
    try:
        cake.image = request.json["image"]
    except:
        cake.image = "https://tinyurl.com/demo-cupcake"
    db.session.add(cake)
    db.session.commit()
    return (jsonify(serialize_cupcake(cake)))

@app.route("/api/cupcakes/<id>", methods = ["DELETE"])
def delete_cake(id):
     cake = Cupcake.query.get_or_404(id)
     db.session.delete(cake)
     db.session.commit()
     return (jsonify({"message": "Deleted"}))

