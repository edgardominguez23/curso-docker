from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "testdb")
    )

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": f"User '{name}' added"}), 201

@app.route("/users", methods=["GET"])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = [{"id": id_, "name": name} for id_, name in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)