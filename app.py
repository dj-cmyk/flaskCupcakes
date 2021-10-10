"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import CupcakeForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'randomString101010'

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route('/api/cupcakes')
def list_cupcakes():
    '''docstring'''
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize_cupcake() for c in cupcakes]
    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    '''docstring'''
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake.serialize_cupcake())



@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    '''docstring'''

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize_cupcake()

    return ( jsonify(cupcake=serialized), 201 )


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    '''docstring'''

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image) 

    db.session.commit()

    return jsonify(cupcake.serialize_cupcake())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    '''docstring'''
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")


@app.route('/', methods=['GET'])
def display_home():
    '''docstring'''
    form = CupcakeForm()
    return render_template('home.html', form=form)