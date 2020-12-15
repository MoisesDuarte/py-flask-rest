# Entrypoint
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initializing app with flask
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) # Base directory

# Setting up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing database
db = SQLAlchemy(app)

# Initializing marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Endpoints
# Index
@app.route('/', methods=['GET'])
def index():
  api_info = {
    "api_online": True,
  }

  return jsonify(api_info)

# Create a product
@app.route('/product', methods=['POST'])
def add_product():
  # Getting request payload
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  # Creating and commiting new product
  new_product = Product(name, description, price, qty)
  db.session.add(new_product)
  db.session.commit()

  # Returning created product as json
  return product_schema.jsonify(new_product)

# Update a product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  # Fetching product
  product = Product.query.get(id);

  # Getting request payload
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  # Updating product values
  product.name = name
  product.description = description
  product.price = price
  product.qty = qty
  
  db.session.commit()

  # Returning created product as json
  return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  # Querying single product
  product = Product.query.get(id)

  # Deleting queried product
  db.session.delete(product)
  db.session.commit()

  # Returning product
  return product_schema.jsonify(product)

# Get all products
@app.route('/product', methods=['GET'])
def get_products():
  # Querying all products
  all_products = Product.query.all()
  result = products_schema.dump(all_products)

  # Returning result array
  return jsonify(result)

# Get single products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  # Querying single product
  product = Product.query.get(id)

  # Returning product
  return product_schema.jsonify(product)

# Running server
# Check if it is entrypoint file
if __name__ == '__main__':
  app.run(debug=True)
