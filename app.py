from flask import Flask, jsonify, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)
DATABASE = 'app.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT name, email FROM users")
    users = cur.fetchall()
    return render_template('index.html', users=users)



@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json() 
    name = data['name']
    email = data['email']
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    #query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
    #cur.executescript(query)
    db.commit()

    # Fetch all the users as a response
    cur.execute("SELECT name, email FROM users")
    users = cur.fetchall()
    return jsonify(users)


app.run(debug=True)