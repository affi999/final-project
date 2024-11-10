from flask import Flask, jsonify, request
from models import Product  # assuming Product model is in models.py
from app import db  # assuming db is initialized in app.py

app = Flask(__name__)
# service/routes.py

@app.route('/api/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())
# service/routes.py

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        category=data['category'],
        availability=data['availability'],
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201
# service/routes.py

@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data['name']
    product.category = data['category']
    product.availability = data['availability']
    product.price = data['price']
    db.session.commit()
    return jsonify(product.to_dict())
# service/routes.py

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
# service/routes.py

@app.route('/api/products', methods=['GET'])
def list_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])
# service/routes.py

@app.route('/api/products/name/<string:name>', methods=['GET'])
def find_product_by_name(name):
    product = Product.query.filter_by(name=name).first()
    if product:
        return jsonify(product.to_dict())
    return jsonify({'message': 'Product not found'}), 404
# service/routes.py

@app.route('/api/products/category/<string:category>', methods=['GET'])
def find_product_by_category(category):
    products = Product.query.filter_by(category=category).all()
    if products:
        return jsonify([product.to_dict() for product in products])
    return jsonify({'message': 'No products found in this category'}), 404
# service/routes.py

@app.route('/api/products/availability/<bool:availability>', methods=['GET'])
def find_product_by_availability(availability):
    products = Product.query.filter_by(availability=availability).all()
    if products:
        return jsonify([product.to_dict() for product in products])
    return jsonify({'message': 'No products found with the specified availability'}), 404

