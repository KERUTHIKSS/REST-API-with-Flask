from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user dictionary
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Home route
@app.route("/", methods=["GET"])
def home():
    return "User API is running", 200

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Get a single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({new_id: users[new_id]}), 201

# Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id]["name"] = data.get("name", user["name"])
    users[user_id]["email"] = data.get("email", user["email"])
    return jsonify({user_id: users[user_id]}), 200

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200

if __name__ == "__main__":
    app.run(debug=True)
