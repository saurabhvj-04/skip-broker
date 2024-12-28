from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data
items = [
    {"id": 1, "name": "Item 1", "price": 100},
    {"id": 2, "name": "Item 2", "price": 200},
    {"id": 3, "name": "Item 3", "price": 300},
]

# API Endpoints

# GET: Fetch all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Fetch an item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST: Add a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# DELETE: Remove an item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return '', 204

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
