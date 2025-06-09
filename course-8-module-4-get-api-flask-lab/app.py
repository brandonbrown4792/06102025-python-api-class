from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({ "message": 'Welcome' })


@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in products if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200


@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((product for product in products if id == product['id']), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({ "message": 'Product not found' }), 404
        

if __name__ == "__main__":
    app.run(debug=True)
