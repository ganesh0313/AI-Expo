from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "expo.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            college TEXT NOT NULL,
            event TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    college = data.get("college", "").strip()
    event = data.get("event", "").strip()

    if not name or not email or not phone or not college or not event:
        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        }), 400

    try:
        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO registrations
            (name, email, phone, college, event)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, college, event))

        conn.commit()

        registration_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "success": True,
            "message": "Registration successful!",
            "registration_id": registration_id
        })

    except Exception as error:

        print(error)

        return jsonify({
            "success": False,
            "message": "Database error. Please try again."
        }), 500

init_db()

if __name__ == "__main__":

    print("\n======================================")
    print(" AI & DATA SCIENCE EXPO 2026")
    print(" Server started successfully!")
    print("======================================")
    print("Open: http://127.0.0.1:5000")
    print("======================================\n")

    app.run(host="0.0.0.0", port=5000, debug=True)