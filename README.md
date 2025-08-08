# 🧪 Flask User Management REST API

A simple REST API built with Flask to perform CRUD operations (Create, Read, Update, Delete) on user data stored in an in-memory dictionary.

---

## 📌 Features

- ✅ Get all users
- ✅ Get a single user by ID
- ✅ Create a new user
- ✅ Update existing user
- ✅ Delete a user

---

## 🛠️ Tools & Technologies

- Python
- Flask
- Postman / curl (for testing)

---

## 🚀 Getting Started

### 1. Clone the Repository or Copy Code

Save the code in a file named `app.py`.

### 2. Install Flask

```bash
pip install flask
```
### 3. Run the App

python app.py

### App will run on:

```
📍 http://127.0.0.1:5000/
```

## 🧪 API Endpoints

| Method | Endpoint       | Description            |
|--------|----------------|------------------------|
| GET    | `/`            | Welcome message        |
| GET    | `/users`       | Get all users          |
| GET    | `/users/<id>`  | Get user by ID         |
| POST   | `/users`       | Create a new user      |
| PUT    | `/users/<id>`  | Update existing user   |
| DELETE | `/users/<id>`  | Delete a user          |
